import random
import time
import mido
import zope.event

from mido import Message
from mido.ports import MultiPort

class Push:
    initMessages = [
         [71,127,21,99,0,1,5] #set toush strip mode
        ,[71,127,21,92,0,1,1] #set channel aftertouch
        ,[71,127,21,1,1] #no idea
        ,[126,0,6,1] #no idea
        ,[71,127,21,
            87,0,20,0,0,13,7,0,3,14,8,0,0,12,8,0,0,0,0,0,0,12,8] #set calibration
        ,[71,127,21,
            93,0,32,0,0,11,14,0,0,13,2,0,0,0,1,4,12,0,8,0,0,0,1,
            13,4,12,0,0,0,0,0,14,10,6,0] #set all pads sensitivity
        ,[71,127,21,98,0,1,1] #user mode
    ]

    def __init__(self):
        #MIDI OUT
        outports = []
        for id in mido.get_output_names():
            #Push User Port
            if "Ableton Push" in id and "2" in id:
                outports.append(mido.open_output(id))
        #Open MIDI Ports - avoiding multiple devices conflict
        self.output = MultiPort(outports)
        #Push initialization routine
        for msg in Push.initMessages:
            self.sendSysex(msg)
        #MIDI IN
        inports = []
        for id in mido.get_input_names():
            #Push User Port
            if "Ableton Push" in id and "2" in id:
                inports.append(mido.open_input(
                    id,
                    callback = self.midi_input_responder
                ))
        #Open MIDI Ports - avoiding multiple devices conflict
        self.input = MultiPort(inports)

    #Text Snapshot
    def snapshot(self):
        for i in range(1, 5):
            blink = random.choice([True, True, False]) # 1:3 chance
            if blink:
                self.fill_screen(char=29)
            else:
                self.fill_screen(rnd=True)
            time.sleep(1/60)

    #MIDI System Exclusive Methods
    def print_text(self, text, row=0, offset=0):
        int_letters = [ord(i) for i in list(text)]
        self.sendSysex([71, 127, 21, 24+row, offset, len(text)+1, 0] + int_letters)

    def fill_screen(self, char=29, rnd=False):
        for offset in range(0, 68):
            for row in range(0, 4):
                if rnd:
                    char = random.randint(0, 127)
                self.sendSysex([71, 127, 21, 24 + row, 0, 2, offset, char])

    def clear_screen(self):
        for row in range(0, 4):
            self.sendSysex([71, 127, 21, 28 + row, 0, 0])

    def clear_pads(self):
        for i in range(0, 72):
            self.sendSysex([71, 127, 21, 4, 0, 8, i, 0, 0, 0, 0, 0, 0, 0])

    def sendSysex(self, data):
        msg = Message(type='sysex', data=data)
        self.output.send(msg)

    #MIDI Input Responder
    def midi_input_responder(self, message):
        event = PushEvent(message)
        zope.event.notify(event)

class PushEvent:
    def __init__(self, message):
        self.message = message
