import wave
import _thread
import pyaudio

def thread_sound(sound, stream, chunk_size, pa):
    
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
    pa.terminate()
    return True

# sound-name = absolute path to .wav file

def play_sound(sound_name):
    pa = pyaudio.PyAudio()
    chunk_size = 1024
    data = wave.open(sound_name, "rb")
    stream = pa.open(format=pa.get_format_from_width(data.getsampwidth()),
                     channels=data.getnchannels(),
                     rate=data.getframerate(),
                     output=True)
    _thread.start_new_thread(thread_sound, (data, stream, chunk_size, pa))
