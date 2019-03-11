import push
import random

class BinaryPattern:

    def __init__(self, push, track):
        self.push = push
        self.track = track
        self.events = [] #8 events
        self.generate()

    def generate(self):
        self.events.clear();
        c = 0
        while c < 8:
            self.events.append(random.choice([True, False]))
            c = c + 1

    def print(self, offset=0, char=29):
        for flag in self.events:
            if flag:
                self.push.sendSysex([71, 127, 21, 24+self.track, 0, 2, offset, char])
            offset = offset + 1

    def get_events(self):
        return self.events

    def get_event(self, index):
        return self.events[index%8]
