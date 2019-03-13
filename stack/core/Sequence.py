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
        sequence = []
        for slot in self.get_current_slots():
            sequence = sequence + slot.get_pattern(track)
        pattern = ""
        for event in sequence:
            if event:
                pattern = pattern + chr(29)
            else:
                pattern = pattern + ' '
        return pattern

    def print(self):
        self.push.clear_screen()
        track = 0
        for track in range(4):
            print(self.get_pattern(track))
            self.push.print_text(
                self.get_pattern(track),
                track
            )



'''
    def get_text_offset(self):
        offset = 0
        i = 0
        while (i < self.column):
            if i%2 == 0 and i != 0:
                offset = offset + 9
            else:
                offset = offset + 8
            i = i + 1
        return offset
'''
