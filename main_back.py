# FILE:     main_back.py
# AUTHOR:   John Marcoux
# DATE:     2019/11/19
# VERSION:  1.0
# PURPOSE:  Main source for front end to interact via

import time
import glob
import os
import sys
from shutil import copyfile
import soundplayer
import fileFunctions

class BackEnd:
    def __init__(self, chunk_size=1024):
        self.sound_player = soundplayer.SoundPlayer(chunk_size)
        self.doc_root = os.getcwd()
        fileFunctions.create_directories()
        if sys.platform == 'win32':
            self.dirsep = '\\'
        else:
            self.dirsep = '/'
        self.sound_names = glob.glob(self.doc_root + self.dirsep + "sounds" +
                                     self.dirsep + "*.[mp3|wav]")
        for i in range(len(self.sound_names)):
            self.sound_names[i] = self.sound_names[i].split(self.dirsep)[-1]
    def play_sound(self, sound_name):
        if not sound_name in self.sound_names:
            return False
        return self.sound_player.play_sound(sound_name)
    def add_sound(self, path_to_new_sound):
        try:
            filename = path_to_new_sound.split(self.dirsep)[-1]
            if filename in self.sound_names:
                filename = filename.split('.')
                filename[0] += "(dup)"
                filename = '.'.join(filename)
            if not filename.split('.')[-1] in ["mp3", "wav"]:
                return False
            copyfile(path_to_new_sound, self.dirsep.join([self.doc_root,
                                                          "sounds", filename]))
            self.sound_names.append(filename)
            return True
        except:
            return False
    def rem_sound(self, sound_name):
        if not sound_name in self.sound_names:
            return False
        try:
            self.sound_names.remove(sound_name)
            os.remove(self.dirsep.join([self.doc_root, "sounds", sound_name]))
            return True
        except:
            return False

if __name__ == "__main__":
    back = BackEnd()
    print(back.add_sound("../file_example_WAV_1MG.wav"))
    print(back.play_sound("file_example_WAV_1MG.wav"))
    print(back.add_sound("oaushaouwdoauwnf"))
    print(back.rem_sound("file_example_WAV_1MG.wav"))
    print(back.rem_sound("file_example_WAV_1MG.wav"))
    print(back.play_sound("file_example_WAV_1MG.wav"))
    time.sleep(10)
