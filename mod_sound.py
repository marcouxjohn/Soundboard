# FILE:     mod_sound.py
# AUTHOR:   John Marcoux
# DATE:     2019/11/28
# VERSION:  1.0
# PURPOSE:  Sound modification lib

import sys
import os
import sox
from pydub import AudioSegment

"""
Name:       change_by_NDB
Purpose:    Changes the volume of the given audio file by n decibels
Arguments:  The name of the sound, the number of decibels and a redundant
            directory separator
Output:     None
Modifies:   Changes the contents of the audio file on disk
Returns:    True on success False on fail
Assumptions:None
Bugs:       None
"""

def change_by_NDB(sound_name, n, dirsep):
    try:
        sound = AudioSegment.from_wav("sounds" + dirsep + sound_name)
        sound = sound + n
        sound.export("sounds" + dirsep + sound_name, format="wav")
        return True
    except:
        return False

# Not yet implemented functions, to be added in a future release
#
#def fade_out_nms(sound_name, n, dirsep):
#    try:
#        sound = AudioSegment.from_wav("sounds" + dirsep + sound_name)
#        sound = sound.fade_out(n)
#        sound.export("sounds" + dirsep + sound_name, format="wav")
#        return True
#    except:
#        return False
#
#def fade_in_nms(sound_name, n, dirsep):
#    try:
#        sound = AudioSegment.from_wav("sounds" + dirsep + sound_name)
#        sound = sound.fade_in(n)
#        sound.export("sounds" + dirsep + sound_name, format="wav")
#        return True
#    except:
#        return False

"""
Name:       BASS
Purpose:    Adds BASS
Arguments:  The name of the sound file, the amount of bass, and a redundant 
            directory separator
Output:     None
Modifies:   Changes the contents of the file on disk
Returns:    True on success, False on fail
Assumptions:None
Bugs:       None
"""

def BASS(sound_name, n, dirsep):
    try:
        transformer = sox.Transformer()
        transformer.bass(n)
        transformer.build("sounds" + dirsep + sound_name, "sounds" + dirsep + "tmp" + sound_name)
        os.remove("sounds" + dirsep + sound_name)
        os.rename("sounds" + dirsep + "tmp" + sound_name, "sounds" + dirsep + sound_name)
        return True
    except:
        return False

"""
Name:       loop_n
Purpose:    Makes the song loop the given number of times
Arguments:  The sound name, the number of times to loop, and a redundant 
            directory separator
Output:     None
Modifies:   Changes the contents of the file on disk
Returns:    True on sucees, False on fail
Assumptions:None
Bugs:       None
"""

def loop_n(sound_name, n, dirsep):
    try:
        sound = AudioSegment.from_wav("sounds" + dirsep + sound_name)
        sound = sound * n
        sound.export("sounds" + dirsep + sound_name, format="wav")
        return True
    except:
        return False

"""
Name:       concat
Purpose:    Takes the contents of the second sound and appends it to the first
            sound on disk
Arguments:  The names of the two sounds and a redundant directory separator
Output:     None
Modifies:   Changes the contents of the first sound on disk
Returns:    True on success, False on fail
Assumptions:None
Bugs:       None
"""

def concat(sound_name1, sound_name2, dirsep):
    try:
        sound1 = AudioSegment.from_wav("sounds" + dirsep + sound_name1)
        sound2 = AudioSegment.from_wav("sounds" + dirsep + sound_name2)
        sound1 = sound1 + sound2
        sound1.export("sounds" + dirsep + sound_name1, format="wav")
        return True
    except:
        return False

"""
Name:       apply_effects
Purpose:    Applies a set of effects based on the config data collected 
            by chadatonic.py
Arguments:  The sound name and the effects array
Output:     None
Modifies:   Changes the sound as specified by the functions above
Returns:    None
Assumptions:None
Bugs:       None
"""

def apply_effects(sound_name, effects):
    #print(effects)
    if effects[1] != 0:
        change_by_NDB(sound_name, effects[1], "/")
    if effects[2] != 0:
        BASS(sound_name, effects[2], "/")
    if effects[3]:
        loop_n(sound_name, effects[4] + 1, "/")
    if effects[5]:
        #print("Concating")
        concat(sound_name, effects[6], "/")
