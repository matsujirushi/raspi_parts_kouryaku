import pyaudio
import numpy as np
import math

RATE = 44100
CHANNELS = 1
FORMAT = pyaudio.paInt16
CHUNK = 44100   # number of frames

def calc_rms(ch):
    ch_square = ch.astype(np.int64) ** 2
    return math.sqrt(ch_square.sum() / ch_square.size)

audio = pyaudio.PyAudio()

stream = audio.open(rate=RATE,
                    channels=CHANNELS,
                    format=FORMAT,
                    input=True,
                    frames_per_buffer=CHUNK)

try:
    while True:
        buffer = stream.read(CHUNK)                 # bytes
        ch1 = np.frombuffer(buffer, dtype=np.int16) # np.ndarray
        print(f'size={len(ch1)}, rms={calc_rms(ch1):.3f}, max={ch1.max()}')

except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
audio.terminate()
