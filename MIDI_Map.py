# Brought to you by st4rchild with the help of Hanz Petrov @ http://remotescripts.blogspot.com
# Avoid using tabs for indentation, use spaces.

# Combination Mode offsets
# ------------------------

TRACK_OFFSET = -1 #offset from the left of linked session origin; set to -1 for auto-joining of multiple instances
SCENE_OFFSET = 0 #offset from the top of linked session origin (no auto-join)

# Buttons / Pads
# -------------
# Valid Note/CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments are permitted

BUTTONCHANNEL = 0 #Channel assignment for all mapped buttons/pads; valid range is 0 to 15 ; 0=1, 1=2 etc.
MESSAGETYPE = 1 #Message type for buttons/pads; set to 0 for MIDI Notes, 1 for CCs.
        #When using CCs for buttons/pads, set BUTTONCHANNEL and SLIDERCHANNEL to different values.

SLIDERCHANNEL = 0 #Channel assignment for all mapped CCs;


# Track Navigation
TRACKLEFT = 44 #arrow left
TRACKRIGHT = 45 #arrow right

# Scene Navigation
SCENEUP = 46 #arrow down
SCENEDN = 47 #arrow up

# Clip Launch / Stop
SELCLIPLAUNCH = 85 #Selected clip launch
SELCLIPGEN = 86 #Selected clip generate
STOPALLCLIPS = -1 #Stop all clips

#SysEX Constants (Push 1)
SYSEX_START = (240, 71, 127, 21)
SYSEX_END = (247, )


CHANNEL = 0
KNOBS_AND_SLIDERS = []

# 8x8 Matrix note assignments
# Track no.:     1   2   3   4   5   6   7   8
CLIPNOTEMAP = ((80, 81, 82, 83, 84, 85, 86, 87), #Row 1
               (72, 73, 74, 75, 76, 77, 78, 79), #Row 2
               (64, 65, 66, 67, 68, 69, 70, 71), #Row 3
               (56, 57, 58, 59, 60, 61, 62, 63), #Row 4
               (48, 49, 50, 51, 52, 53, 54, 55), #Row 5
               (40, 41, 42, 43, 44, 45, 46, 47), #Row 6
               (32, 33, 34, 35, 36, 37, 38, 39), #Row 7
               (24, 25, 26, 27, 28, 29, 30, 31), #Row 8
               )
