from BinaryPattern import BinaryPattern

class GeneratedSlot:

    instances = []

    def __init__(self, sequence, stack, n_tracks = 4):
        self._sequence = sequence
        self._stack = stack
        self._status = 'disabled'
        self._patterns = []
        for i in range(n_tracks):
            self._patterns.append(BinaryPattern())
        GeneratedSlot.instances.append(self)


    def generate(self):
        for pattern in self._patterns:
            pattern.generate()


    def get_pattern(self, track):
        return self._patterns[track].get_events()


    def get_midi_nn(self):
        #c = self._stack.column
        #r = self._stack.get_slot_row(self)
        return 24
        # + c + r*8  #24 = first pad (bottom/left)


    def change_status(self):
        if self._status == 'disabled':
            for slot in GeneratedSlot.instances:
                if slot.stack == self.stack:
                    slot._status == 'disabled'
            self._status == 'enabled'
            self._stack.set_current_slot(self)
            self._sequence.print_lcd()
