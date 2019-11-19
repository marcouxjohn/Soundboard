# FILE:     soundPlayer.py
# AUTHOR:   John Marcoux
# DATE:     2019/11/19
# VERSION:  1.0
# PURPOSE:  File for playing and overlaying sounds

import wave
import time
import _thread
import pyaudio

# Might need to add a method for converting mp3's to wavs
# Or figure out how to fire an mp3 through pyaudio

class SoundPlayer:
    def __init__(self, queue_size, chunk_size):
        self.py_audio = pyaudio.PyAudio()
        self.chunk_size = chunk_size
        self.queue_size = queue_size
        self.num_stored = 0
        self.stored = {}

    def get_sound(self, sound_name):
        try:
            data = self.stored[sound_name]
            del self.stored[sound_name]
            self.stored[sound_name] = data
            stream = self.py_audio.open(
                format=self.py_audio.get_format_from_width(data.getsampwidth()),
                channels=data.getnchannels(),
                rate=data.getframerate(),
                output=True)
        except:
            try:
                data = wave.open(sound_name, 'rb')
            except:
                stream.close()
                return None
            try:
                stream = self.py_audio.open(
                    format=self.py_audio.get_format_from_width(
                        data.getsampwidth()),
                    channels=data.getnchannels(),
                    rate=data.getframerate(),
                    output=True)
            except:
                return None
            if self.num_stored == self.queue_size:
                rem = list(self.stored)[0]
                del self.stored[rem]
                self.stored[sound_name] = data
            else:
                self.stored[sound_name] = data
                self.num_stored += 1
        return data, stream

    def play_sound(self, sound_name):
        # Might have to slap this in a thread
        # Might need a global 'play' function to play and overlay anything
        # That gets sent to it, but threading might solve this issue
        sound, stream = self.get_sound(sound_name)
        _thread.start_new_thread(thread_sound, (sound, stream, self.chunk_size))

    def destroy(self):
        del self.stored
        self.py_audio.terminate()

def thread_sound(sound, stream, chunk_size):
    if sound is None:
        return False
    sound.rewind()
    data = sound.readframes(chunk_size)
    while len(data) > 0:
        stream.write(data)
        data = sound.readframes(chunk_size)
    stream.stop_stream()
    stream.close()
    return True

my_player = SoundPlayer(10, 1024)
#my_player.play_sound("SampleAudio_0.4mb.mp3")
my_player.play_sound("file_example_WAV_1MG.wav")
time.sleep(1)
my_player.play_sound("file_example_WAV_1MG.wav")
time.sleep(30)
my_player.destroy()
del my_player
#stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                channels=wf.getnchannels(),
#                rate=wf.getframerate(),
#                output=True)
