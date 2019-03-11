class Stack:
    def __init__(self, push, column):
        self.push = push
        self.column = column
        self.currentSlot = 0
        self.slots = []
        for raw in range(0, 8):
            self.slots.append(Slot(push, self, raw))

    def print(self, offset):
        #current slot on screen
        self.slots[self.currentSlot].print(offset)
        #slots on pads
        for row in range(8):
            self.push.sendSysex([71, 127, 21, 4, 0, 8,
                self.column + row*8,
                0, 127, 127, 127, 127, 127, 127 #white
            ])
        #current slot red
        self.push.sendSysex([71, 127, 21, 4, 0, 8,
            self.column + self.currentSlot*8,
            0, 127, 127, 0, 0, 0, 0 #red
        ])

    def get_current_slot(self):
        return self.slots[self.currentSlot]
