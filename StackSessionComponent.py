# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-
import Live
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonElement import ButtonElement
from Sequence import Sequence

class StackSessionComponent(SessionComponent):

    __module__ = __name__


    def __init__(self, control_surface, num_tracks, num_scenes):
        SessionComponent.__init__(self, num_tracks, num_scenes)
        self._sequence = Sequence(control_surface)
        self._control_surface = control_surface
        self._slot_gen_button = None
        self._slot_launch_button = None


    def disconnect(self):
        SessionComponent.disconnect(self)
        if (self._slot_launch_button != None):
            self._slot_launch_button.remove_value_listener(self._slot_launch_value)
            self._slot_launch_button = None
        if (self._slot_gen_button != None):
            self._slot_gen_button.remove_value_listener(self._slot_gen_value)
            self._slot_gen_button = None


    def link_with_track_offset(self, track_offset, scene_offset):
        assert (track_offset >= 0)
        assert (scene_offset >= 0)
        if self._is_linked():
            self._unlink()
        self.set_offsets(track_offset, scene_offset)
        self._link()


    def unlink(self):
        if self._is_linked():
            self._unlink()


    def set_slot_launch_button(self, button):
        assert ((button == None) or isinstance(button, ButtonElement))
        if (self._slot_launch_button != button):
            if (self._slot_launch_button != None):
                self._slot_launch_button.remove_value_listener(self._slot_launch_value)
            self._slot_launch_button = button
            if (self._slot_launch_button != None):
                self._slot_launch_button.add_value_listener(self._slot_launch_value)
            self.update()


    def _slot_launch_value(self, value):
        assert (value in range(128))
        assert (self._slot_launch_button != None)
        if self.is_enabled():
            if ((value != 0) or (not self._slot_launch_button.is_momentary())):
                if (self.song().view.highlighted_clip_slot != None):
                    self.song().view.highlighted_clip_slot.fire()


    def set_slot_gen_button(self, button):
        assert ((button == None) or isinstance(button, ButtonElement))
        if (self._slot_gen_button != button):
            if (self._slot_gen_button != None):
                self._slot_gen_button.remove_value_listener(self._slot_gen_value)
            self._slot_gen_button = button
            if (self._slot_gen_button != None):
                self._slot_gen_button.add_value_listener(self._slot_gen_value)
            self.update()


    def _slot_gen_value(self, value):
        assert (value in range(128))
        assert (self._slot_gen_button != None)
        if self.is_enabled():
            if ((value != 0) or (not self._slot_gen_button.is_momentary())):
                if (self.song().view.highlighted_clip_slot != None):
                    self._control_surface.snapshot()
                    self._sequence.initialization()


    def set_slot_gen_button(self, button):
        assert ((button == None) or isinstance(button, ButtonElement))
        if (self._slot_gen_button != button):
            if (self._slot_gen_button != None):
                self._slot_gen_button.remove_value_listener(self._slot_gen_value)
            self._slot_gen_button = button
            if (self._slot_gen_button != None):
                self._slot_gen_button.add_value_listener(self._slot_gen_value)
            self.update()


    def _pad_value(self, a, b):
        assert (value in range(128))
        for column in range(8):
            stack = self._sequence.get_stack(column)
            for row in range(8):
                slot = stack.get_slot(row)
                if slot.get_midi_nn() == value:
                    #stack.set_current_slot(slot)
                    self._sequence.update()
        self._control_surface.print_text()



    def set_pad_button(self, button):
        assert ((button == None) or isinstance(button, ButtonElement))
        button.add_value_listener(self._pad_value)
        self.update()
