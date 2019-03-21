from Stack import Stack

class Sequence:

    def __init__(self, control_surface):
        self._control_surface = control_surface
        self._stacks = []
        for i in range(8):
            self._stacks.append(Stack(control_surface, self, i))


    def initialization(self):
        self.generate()
        for stack in self._stacks:
            stack.initialization()
        self.update()


    def update(self):
        self.print_lcd()


    def generate(self):
        for stack in self._stacks:
            stack.generate()


    def get_stack(self, index):
        return self._stacks[index]


    def get_current_slots(self):
        current_slots = []
        for stack in self._stacks:
            current_slots.append(stack.get_current_slot())
        return current_slots


    def get_pattern(self, track):
        pattern = []
        for slot in self.get_current_slots():
            pattern = pattern + slot.get_pattern(track)
        return pattern


    def print_lcd(self):
        self._control_surface.clear_screen()
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
            self._control_surface.print_text(output_string, track)
