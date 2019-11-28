# FILE:     main_back.py
# AUTHOR:   John Marcoux
# DATE:     2019/11/19
# VERSION:  1.0
# PURPOSE:  Main source for front end to interact via

# Import all the libs we need

import time
import glob
import os
import sys
from shutil import copyfile
import pygame
import soundplayer
import fileFunctions
import config
import pydub

"""
Name:       BackEnd
Purpose:    Back End object for all playing and tracking of sounds
Notes:      None
"""

class BackEnd:

    """
    Name:       __init__
    Purpose:    Initializes a BackEnd object
    Arguments:  The chunk size for playing an audio file optionally
    Output:     None
    Modifies:   Creates the aforementioned object
    Returns:    The object
    Assumptions:None
    Bugs:       None
    """

    def __init__(self):
        self.doc_root = os.getcwd()
        fileFunctions.create_directories()
        self.key_config = config.KeyConfig()
        if sys.platform == 'win32':
            self.dirsep = '\\'
        else:
            self.dirsep = '/'
        print(self.doc_root)
        self.sound_names = glob.glob(self.doc_root + self.dirsep + "sounds" +
                                     self.dirsep + "*.wav")
        mp3_names = glob.glob(self.doc_root + self.dirsep + "sounds" +
                             self.dirsep + "*.mp3")
        for name in mp3_names:
            try:
                n_sound = pydub.AudioSegment.from_mp3(name)
                n_name = name.split(".")[:-1]
                n_name.append("wav")
                n_name = ".".join(n_name)
                if not n_name in self.sound_names:
                    n_sound.export(n_name, format="wav")
                    self.sound_names.append(n_name)
            except:
                print("Bad sound:",name)
        for i in range(len(self.sound_names)):
            self.sound_names[i] = self.sound_names[i].split(self.dirsep)[-1]

            if not os.path.exists(self.doc_root + self.dirsep + "configs" + self.dirsep + self.sound_names[i]):
                config_data = [0]*8
                config_data[3] = False
                config_data[5] = False
                config_data[0] = self.sound_names[i]
                fileFunctions.save_sound_config(config_data, config_data[0])

    """
    Name:       play_sound
    Purpose:    Plays a sound via the SoundPlayer object
    Arguments:  The name of the sound
    Output:     None
    Modifies:   Writes to a sound output stream
    Returns:    True on success, False on fail
    Assumptions:None
    Bugs:       None
    """

    def play_sound(self, sound_name):
        if not sound_name in self.sound_names:
            return False
        #print("got here")
        return soundplayer.play_sound(sound_name, self.dirsep)

    """
    Name:       add_sound
    Purpose:    Adds a sound to the list of current sounds
    Arguments:  The path to the new sound
    Output:     None
    Modifies:   Adds the sound to the list of sounds
    Returns:    True on success, False on failure
    Assumptions:None
    Bugs:       None
    """

    def add_sound(self, path_to_new_sound):
        try:
            filename = path_to_new_sound.split(self.dirsep)[-1]

            # Make sure file isn't a dup, if it is make sure it's obvious

            if filename in self.sound_names:
                filename = filename.split('.')
                filename[0] += "(dup)"
                filename = '.'.join(filename)
            if not filename.split('.')[-1] in ["mp3", "wav"]:
                return False
            x = copyfile(path_to_new_sound, self.dirsep.join([self.doc_root,
                                                          "sounds", filename]))
            self.sound_names.append(filename)
            return True
        except:
            return False

    """
    Name:       rem_sound
    Purpose:    Removes a sound from the sound list
    Arguments:  The name of the sound
    Output:     None
    Modifies:   Removes the sound from the list if it is there
    Returns:    True on success, False on failure
    Assumptions:None
    Bugs:       None
    """

    def rem_sound(self, sound_name):
        if not sound_name in self.sound_names:
            return False
        try:
            self.sound_names.remove(sound_name)
            os.remove(self.dirsep.join([self.doc_root, "sounds", sound_name]))
            return True
        except:
            return False

    def add_key_bind(self, key, sound):
        if sound in self.sound_names:
            return self.key_config.add_key_bind(key, sound)
        return False

    def rem_key_bind(self, key):
        return self.key_config.rem_key_bind(key)
