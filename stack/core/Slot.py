import zope.event

from .binarypattern import BinaryPattern

class Slot:

    instances = []

    def __init__(self, push, stack, raw):
        self.push = push
        self.stack = stack
        self.raw = raw
        #Set MIDI IN callback function
        self.status = 'disabled'
        zope.event.subscribers.append(self.change_status)
        #Evaluate pattern
        self.patterns = []
        for i in range(0, 4):
            self.patterns.append(BinaryPattern(push, i))
        #Store instance
        Slot.instances.append(self)

    def print(self, offset):
        for pattern in self.patterns:
            pattern.print(offset)

    def get_pattern(self, index):
        return self.patterns[index].get_events()

    def get_midiNN(self):
        #TODO: make 36 a constant
        return 36 + self.stack.column + self.raw*8

    def change_status(self, event):
        if event.message.type == 'note_on':
            if event.message.note ==  self.get_midiNN():
                if self.status == 'disabled':
                    #Disable all slots in the same stack
                    for slot in Slot.instances:
                        if slot.stack == self.stack:
                            slot.status == 'disabled'
                    #Enable the this slot
                    self.push.clear_screen();
                    self.status == 'enabled'
                    self.stack.currentSlot = self.raw
                    self.stack.print(self.raw)
