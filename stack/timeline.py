import time
from threading import Thread, Event

class Timeline(Thread):
    def __init__(self, sequence, push):
        Thread.__init__(self)
        self.playing = Event()
        self.push = push
        self.position = 0
        self.stepDur = 1/16

    def run(self):
        while self.playing.wait():
            self.position = self.position + 1
            if self.position >= 64:
                self.position = 0
            time.sleep(self.stepDur)

    def play(self):
        self.start()
        self.playing.set()

    def pause(self):
        self.playing.clear()

    def stop(self):
        self.playing.clear()
        self.position = 0
