#
#
#

from __future__ import with_statement

import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import *
from _Framework.SessionComponent import SessionComponent
from _Framework.SliderElement import SliderElement
from _Framework.ButtonElement import ButtonElement
from _Framework.MixerComponent import MixerComponent

import time
import random
from StackSessionComponent import StackSessionComponent
from MIDI_Map import *
#MIDI_NOTE_TYPE = 0
#MIDI_CC_TYPE = 1
#MIDI_PB_TYPE = 2

class StackControlSurface(ControlSurface):
    __doc__ = "Script for Stack"

    _active_instances = []
    def _combine_active_instances():
        track_offset = 0
        scene_offset = 0
        for instance in StackControlSurface._active_instances:
            instance._activate_combination_mode(track_offset, scene_offset)
            track_offset += instance._session.width()
    _combine_active_instances = staticmethod(_combine_active_instances)


    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        #self.set_suppress_rebuild_requests(True)
        with self.component_guard():
            self._note_map = []
            self._ctrl_map = []
            self._load_MIDI_map()
            self._mixer = None
            self._setup_mixer_control()
            self._session = None
            self._setup_session_control()
            self._session.set_mixer(self._mixer)
            self.set_highlighting_session_component(self._session)
            #self.set_suppress_rebuild_requests(False)
        self._do_combine()


    def disconnect(self):
        self._note_map = None
        self._ctrl_map = None
        self._do_uncombine()
        self._session = None
        self._mixer = None
        ControlSurface.disconnect(self)


    def _do_combine(self):
        if self not in StackControlSurface._active_instances:
            StackControlSurface._active_instances.append(self)
            StackControlSurface._combine_active_instances()


    def _do_uncombine(self):
        if ((self in StackControlSurface._active_instances) and StackControlSurface._active_instances.remove(self)):
            StackControlSurface._session.unlink()
            StackControlSurface._combine_active_instances()


    def _activate_combination_mode(self, track_offset, scene_offset):
        if TRACK_OFFSET != -1:
            track_offset = TRACK_OFFSET
        if SCENE_OFFSET != -1:
            scene_offset = SCENE_OFFSET
        self._session.link_with_track_offset(track_offset, scene_offset)


    def _setup_session_control(self):
        is_momentary = True
        self._session = StackSessionComponent(self, 1, 8)
        self._session.name = 'Session_Control'
        self._session.set_select_buttons(self._ctrl_map[SCENEDN], self._ctrl_map[SCENEUP])
        self._session.selected_scene().name = 'Selected_Scene'
        self._session.set_slot_launch_button(self._ctrl_map[SELCLIPLAUNCH])
        self._session.set_slot_gen_button(self._ctrl_map[SELCLIPGEN])
        for scene_index in range(8):
            for track_index in range(8):
                button = self._note_map[CLIPNOTEMAP[scene_index][track_index]]
                self._session.set_pad_button(button)


    def _setup_mixer_control(self):
        is_momentary = True
        self._mixer = MixerComponent(8)
        self._mixer.name = 'Mixer'
        self._mixer.selected_strip().name = 'Selected_Channel_Strip'
        self._mixer.set_select_buttons(self._ctrl_map[TRACKRIGHT], self._ctrl_map[TRACKLEFT])


    def _load_MIDI_map(self):
        is_momentary = True
        for note in range(128):
            button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, BUTTONCHANNEL, note)
            button.name = 'Note_' + str(note)
            self._note_map.append(button)
        self._note_map.append(None) #add None to the end of the list, selectable with [-1]

        for cc in range(128):
            button = ButtonElement(is_momentary, MIDI_CC_TYPE, BUTTONCHANNEL, cc)
            button.name = 'Ctrl_' + str(cc)
            self._ctrl_map.append(button)
        self._ctrl_map.append(None) #add None to the end of the list, selectable with [-1]
        '''

        for ctrl in range(128):
            control = SliderElement(MIDI_CC_TYPE, SLIDERCHANNEL, ctrl)
            control.name = 'Ctrl_' + str(ctrl)
            self._ctrl_map.append(control)
        self._ctrl_map.append(None)
        '''

    #SysEx Functions TO DO: replace them with functions from framework
    def snapshot(self):
        for i in range(1, 5):
            self.fill_screen(rnd=True)
            time.sleep(1/60)
        self.clear_screen()


    def fill_screen(self, char=29, rnd=False):
        for offset in range(0, 136):
            for row in range(0, 4):
                if rnd:
                    char = random.randint(33, 96)
                self._send_midi(SYSEX_START + (24+row, 0, 2, offset, char) + SYSEX_END)


    def print_text(self, text, row=0, offset=0):
        int_letters = tuple([ord(i) for i in list(text)])
        self._send_midi(SYSEX_START + (24+row, offset, len(text)+1, 0) + int_letters + SYSEX_END)


    def clear_screen(self):
        for row in range(0, 4):
            self._send_midi(SYSEX_START + (28 + row, 0, 0) + SYSEX_END)


    def set_pad(self, column, row, color):
        if color == "white":
            PAD_COLOR = (0, 127, 127, 127, 127, 127, 127)
        if color == "red":
            PAD_COLOR = (0, 127, 127, 0, 0, 0, 0)
        self._send_midi(SYSEX_START + (4, 0, 8, column + row*8) + PAD_COLOR + SYSEX_END)
