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
#   Probably gonna use ffmpeg via pydub
# Or figure out how to fire an mp3 through pyaudio
#   Not sure if I can

class SoundPlayer:
    def __init__(self, chunk_size):
        self.py_audio = pyaudio.PyAudio()
        self.chunk_size = chunk_size

    def get_sound(self, sound_name):
        try:
            data = wave.open(sound_name, 'rb')
        except:
            return (None,None)
        try:
            stream = self.py_audio.open(
                format=self.py_audio.get_format_from_width(
                    data.getsampwidth()),
                channels=data.getnchannels(),
                rate=data.getframerate(),
                output=True)
        except:
            data.close()
            return (None,None)
        return data, stream

    def play_sound(self, sound_name):
        sound, stream = self.get_sound(sound_name)
        if sound is None and stream is None:
            return False
        _thread.start_new_thread(thread_sound, (sound, stream, self.chunk_size))
        return True

    def destroy(self):
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
    print("DONE")
    return True

if __name__ == "__main__":
    my_player = SoundPlayer(1024)
    for _ in range(10):
        my_player.play_sound("file_example_WAV_1MG.wav")
        time.sleep(1)
    for i in range(35):
        print(i)
        time.sleep(1)
    my_player.destroy()
    del my_player
