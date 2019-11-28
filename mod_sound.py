# FILE:     mod_sound.py
# AUTHOR:   John Marcoux
# DATE:     2019/11/28
# VERSION:  1.0
# PURPOSE:  Sound modification lib

import sys
import os
import sox
from pydub import AudioSegment

# Changes sound volume by n decibels

def change_by_NDB(sound_name, n, dirsep):
    try:
        sound = AudioSegment.from_wav("sounds" + dirsep + sound_name)
        sound = sound + n
        sound.export("sounds" + dirsep + sound_name, format="wav")
        return True
    except:
        return False

# Not yet implemented functions, to be added in a future release

"""
def fade_out_nms(sound_name, n, dirsep):
    try:
        sound = AudioSegment.from_wav("sounds" + dirsep + sound_name)
        sound = sound.fade_out(n)
        sound.export("sounds" + dirsep + sound_name, format="wav")
        return True
    except:
        return False

def fade_in_nms(sound_name, n, dirsep):
    try:
        sound = AudioSegment.from_wav("sounds" + dirsep + sound_name)
        sound = sound.fade_in(n)
        sound.export("sounds" + dirsep + sound_name, format="wav")
        return True
    except:
        return False
"""

# Adds n units of BASS to the sound

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

# Make the song loop n more times

def loop_n(sound_name, n, dirsep):
    try:
        sound = AudioSegment.from_wav("sounds" + dirsep + sound_name)
        sound = sound * n
        sound.export("sounds" + dirsep + sound_name, format="wav")
        return True
    except:
        return False

# Concatenates the second sound to the end of the first

def concat(sound_name1, sound_name2, dirsep):
    try:
        sound1 = AudioSegment.from_wav("sounds" + dirsep + sound_name1)
        sound2 = AudioSegment.from_wav("sounds" + dirsep + sound_name2)
        sound1 = sound1 + sound2
        sound1.export("sounds" + dirsep + sound_name1, format="wav")
        return True
    except:
        return False

# Applies any effects given by the config list

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

