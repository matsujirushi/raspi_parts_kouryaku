import pigpio
import time

PHASE_A = 17
PHASE_B = 27
INTERVAL = 0.1


def phase_changed(gpio, level, tick):
    global position
    position += 1 if pi.read(PHASE_B) == 1 else -1


pi = pigpio.pi()

pi.set_mode(PHASE_A, pigpio.INPUT)
pi.set_mode(PHASE_B, pigpio.INPUT)
pi.set_pull_up_down(PHASE_A, pigpio.PUD_UP)
pi.set_pull_up_down(PHASE_B, pigpio.PUD_UP)

pi.callback(PHASE_A, pigpio.FALLING_EDGE, phase_changed)

position = 0
try:
    while True:
        print(position)
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    pass

pi.stop()
