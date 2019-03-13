from .stack import Stack

class Sequence:
    def __init__(self, push):
        self.push = push
        self.stacks = []
        for i in range(0, 8):
            self.stacks.append(Stack(push, self, i))
        self.print()

    def get_current_slots(self):
        current_slots = []
        for stack in self.stacks:
            current_slots.append(stack.get_current_slot())
        return current_slots

    def get_pattern(self, track):
        pattern = []
        for slot in self.get_current_slots():
            pattern = pattern + slot.get_pattern(track)
        return pattern

    def print(self):
        self.push.clear_screen()
        track = 0
        for track in range(4):
            pattern = self.get_pattern(track)

            output_string = ""
            i = 0
            for event in pattern:
                if i == 8 or i == 24 or i == 40 or i == 56:
                    output_string = output_string + ' '
                if event:
                    output_string = output_string + chr(29)
                else:
                    output_string = output_string + ' '
                i = i + 1
            self.push.print_text(output_string, track)
            print(output_string)
