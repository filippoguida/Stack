from .stack import Stack

class Matrix:
    def __init__(self, push):
        self.push = push
        self.stacks = []
        for i in range(0, 8):
            self.stacks.append(Stack(push, i))

    def print_current_slots(self):
        self.push.clear_screen()
        self.push.clear_pads()
        offset = 0
        i = 0
        for stack in self.stacks:
            stack.print(offset)
            if i%2 == 0 and i != 0:
                offset = offset + 9
            else:
                offset = offset + 8
            i = i + 1

    def get_current_slots(self):
        current_slots = []
        for stack in self.stacks:
            current_slots.append(stack.get_current_slot())
        return current_slots
