from stack.matrix import Matrix

class Sequence:
    def __init__(self, push):
        self.matrix = Matrix(push)
        self.push = push
        self.print()

    def print(self):
        self.push.clear_screen()
        self.matrix.print_current_slots()

    def get_pattern(self, index):
        sequence = []
        for slot in self.matrix.get_current_slots():
            sequence = sequence + slot.get_pattern(index)
        return sequence
