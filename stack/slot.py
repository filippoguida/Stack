import zope.event
from .binarypattern import BinaryPattern

class Slot:

    instances = []

    def __init__(self, sequence, stack, n_tracks=4):
        self.sequence = sequence
        self.stack = stack
        #Set MIDI IN callback function
        self.status = 'disabled'
        zope.event.subscribers.append(self.change_status)
        #Evaluate pattern
        self.patterns = []
        for i in range(n_tracks):
            self.patterns.append(BinaryPattern())
        #Store instance
        Slot.instances.append(self)

    def get_pattern(self, track):
        return self.patterns[track].get_events()

    def get_midiNN(self):
        #TODO: make 36 a constant (first pad bottm/left)
        c = self.stack.column
        r = self.stack.get_slot_row(self)*8
        return 36 + c + r

    def change_status(self, event):
        if event.message.type == 'note_on':
            if event.message.note ==  self.get_midiNN():
                if self.status == 'disabled':
                    #Disable all slots in the same stack
                    for slot in Slot.instances:
                        if slot.stack == self.stack:
                            slot.status == 'disabled'
                    #Enable the this slot
                    self.status == 'enabled'
                    self.stack.set_current_slot(self)
                    self.sequence.print()
