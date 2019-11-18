# FILE:     soundPlayer.py
# AUTHOR:   John Marcoux
# DATE:     2019/11/18
# VERSION:  1.0
# PURPOSE:  File for playing and overlaying sounds

# imports for sounddevice and other stuff

class sound_player:
    def __init__(self, sound_device, queue_size):
        self.sound_device = sound_device
        self.queue_size = queue_size
        self.stored = {}

    def get_sound(self, sound_name):
        try:
            out = self.stored[sound_name]
            del self.stored[sound_name]
            self.stored[sound_name] = out
        except:
            out = sound_from_file(sound_name)
            rem = list(self.stored)[0]
            del self.stored[rem]
            self.stored[sound_name] = out
        return out

def sound_from_file(sound_name):
    

def play_sound(sound_name):


