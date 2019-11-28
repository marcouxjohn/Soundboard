# FILE:     soundPlayer.py
# AUTHOR:   John Marcoux
# DATE:     2019/11/19
# VERSION:  1.1
# PURPOSE:  File for playing and overlaying sounds

import time
import os
import simpleaudio as sa
import _thread

"""
Name:       play_sound
Purpose:    Plays the given sound file if it is present on disk
Arguments:  The name of the sound
Output:     None
Modifies:   Creates a new thread to play the sound
Returns:    False if file does not exist, True otherwise
Assumptions:None
Bugs:       None
"""

def play_sound(sound_name, dirsep):
    if os.path.exists("sounds" + dirsep + sound_name):
        _thread.start_new_thread(thread_sound, (sound_name, dirsep))
        return True
    return False

"""
Name:       thread_sound
Purpose:    Function to pass to a thread to play the sound
Arguments:  The sound file name
Output:     None
Modifies:   Writes to the sound player
Returns:    None
Assumptions:None
Bugs:       None
"""

def thread_sound(file_name, dirsep):
    wave_obj = sa.WaveObject.from_wave_file("sounds" + dirsep + file_name)
    play_obj = wave_obj.play()
    play_obj.wait_done()
