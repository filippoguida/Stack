from GeneratedSlot import GeneratedSlot

class Stack:
    def __init__(self, control_surface, sequence, column):
        self._control_surface = control_surface
        self._column = column
        self._slots = []
        for raw in range(8):
            self._slots.append(GeneratedSlot(sequence, self))
        self._current_slot = self._slots[0]


    def initialization(self):
        for row in range(8):    #set pads
            self._control_surface.set_pad(self._column, row, "white")
        self._control_surface.set_pad(self._column, self.get_current_slot_row(), "red")


    def generate(self):
        for slot in self._slots:
            slot.generate()


    def get_current_slot(self):
        return self._current_slot


    def get_slot_row(self, slot):
        return self._slots.index(slot)

    def get_slot(self, row):
        return self._slots[row]

    def get_slot_midi_nn(self, midi_nn):
        row = ((midi_nn - 24) - stack._column)/8
        return self._slots[row]

    def get_current_slot_row(self):
        return self.get_slot_row(self._current_slot)

    def set_current_slot(self, slot):
        self._current_slot = slot
        self.initialization()

    def set_current_slot_midi_nn(self, midi_nn):
        self.set_current_slot(self.get_slot_midi_nn(midi_nn))
