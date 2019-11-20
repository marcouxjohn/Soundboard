# FILE:     soundPlayer.py
# AUTHOR:   John Marcoux
# DATE:     2019/11/19
# VERSION:  1.1
# PURPOSE:  File for playing and overlaying sounds

# Imports of all the libs we need

import wave
import time
import _thread
import pyaudio

# Might need to add a method for converting mp3's to wavs
#   Probably gonna use ffmpeg via pydub

"""
Name:       SoundPlayer
Purpose:    Allows playing sounds from disk
Notes:      Has issues if more than ~30 sounds are playing at once
"""

class SoundPlayer:

    """
    Name:       __init__
    Purpose:    Initializes a SoundPlayer object
    Arguments:  The chunk size for playing an audio file
    Output:     None
    Modifies:   Creates the aforementioned object
    Returns:    The object
    Assumptions:None
    Bugs:       None
    """

    def __init__(self, chunk_size):
        self.py_audio = pyaudio.PyAudio()
        self.chunk_size = chunk_size

    """
    Name:       get_sound
    Purpose:    Creates the sound output stream and wave file stream
    Arguments:  The name of the sound
    Output:     None
    Modifies:   Creates the aforementioned objects
    Returns:    The objects, or (None, None) on fail
    Assumptions:None
    Bugs:       None
    """

    def get_sound(self, sound_name):
        
        # Get the audio
        
        try:
            data = wave.open(sound_name, 'rb')
        except:
            return (None,None)
        
        # Set up the output stream
        
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

    """
    Name:       play_sound
    Purpose:    Plays the given sound file if it is present on disk
    Arguments:  The name of the sound
    Output:     None
    Modifies:   Creates a new thread to play the sound
    Returns:    False on fail True on success
    Assumptions:None
    Bugs:       None
    """

    def play_sound(self, sound_name):
        sound, stream = self.get_sound(sound_name)
        
        # Make sure the sound was grabbed properly
        
        if sound is None and stream is None:
            return False
        _thread.start_new_thread(thread_sound, (sound, stream, self.chunk_size))
        return True

    """
    Name:       destroy
    Purpose:    Destroys the current object
    Arguments:  None
    Output:     None
    Modifies:   Destroys the object
    Returns:    None
    Assumptions:None
    Bugs:       None
    """

    def destroy(self):
        self.py_audio.terminate()



"""
Name:       thread_sound
Purpose:    Function to pass to a thread to play the sound
Arguments:  The sound file stream, the output stream, and the chunk size
Output:     None
Modifies:   Writes to the output stream
Returns:    False on fail, True on success
Assumptions:None
Bugs:       None
"""

def thread_sound(sound, stream, chunk_size):
    
    # Make sure sound is there
    
    if sound is None:
        return False

    # Play the sound reading "chunk_size" bytes at a time

    data = sound.readframes(chunk_size)
    while len(data) > 0:
        stream.write(data)
        data = sound.readframes(chunk_size)
    stream.stop_stream()
    stream.close()
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
