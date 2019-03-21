import random

class BinaryPattern:

    def __init__(self):
        self._events = []
        for i in range(8):
            self._events.append(False)


    def generate(self):
        for i in range(len(self._events)):
            self._events[i] = random.choice([True, False])


    def get_events(self):
        return self._events


    def get_event(self, index):
        return self._events[index%8]
