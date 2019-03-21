from .slot import Slot

class SlotStack:
    def __init__(self, push, sequence, column):
        self.push = push
        self.column = column
        self.slots = []
        for raw in range(8):
            self.slots.append(Slot(sequence, self))
        self.currentSlot = self.slots[0]

    def get_current_slot(self):
        return self.currentSlot

    def get_slot_row(self, slot):
        return self.slots.index(slot)

    def get_current_slot_row(self):
        return self.get_slot_row(self.currentSlot)

    def set_current_slot(self, slot):
        self.currentSlot = slot
        #slots on pads
        for row in range(8):
            self.push.sendSysex([71, 127, 21, 4, 0, 8,
                self.column + row*8,
                0, 127, 127, 127, 127, 127, 127 #white
            ])
        #current slot red
        self.push.sendSysex([71, 127, 21, 4, 0, 8,
            self.column + self.get_current_slot_row()*8,
            0, 127, 127, 0, 0, 0, 0 #red
        ])
