import random

class BinaryPattern:

    def __init__(self):
        self.events = [] #8 events
        self.generate()

    def generate(self, n_events=8):
        self.events.clear();
        i = 0
        for i in range(n_events):
            self.events.append(random.choice([True, False]))

    def get_events(self):
        return self.events

    def get_event(self, index):
        return self.events[index%8]
