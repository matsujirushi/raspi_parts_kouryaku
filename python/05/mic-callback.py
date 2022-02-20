import pyaudio
import numpy as np
import math
import time

RATE = 44100
CHANNELS = 1
FORMAT = pyaudio.paInt16
CHUNK = 44100    # number of frames

def calc_rms(ch):
    ch_square = ch.astype(np.int64) ** 2
    return math.sqrt(ch_square.sum() / ch_square.size)

def callback(in_data, frame_count, time_info, status):
    ch1 = np.frombuffer(in_data, dtype=np.int16) # np.ndarray
    print(f'size={len(ch1)}, rms={calc_rms(ch1):.3f}, max={ch1.max()}')
    return (None, pyaudio.paContinue)

p = pyaudio.PyAudio()

stream = p.open(rate=RATE,
                channels=CHANNELS,
                format=FORMAT,
                input=True,
                frames_per_buffer=CHUNK,
                stream_callback=callback)

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
p.terminate()
