# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import Live
from StackControlSurface import StackControlSurface

def create_instance(c_instance):
    ' Creates and returns the APC20 script '
    return StackControlSurface(c_instance)


# local variables:
# tab-width: 4
