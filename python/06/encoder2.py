import pigpio
import time

PHASE_A = 17
PHASE_B = 27
INTERVAL = 0.1


def phase_changed(gpio, level, tick):
    global last_gpio
    global last_level
    global position

    if gpio == last_gpio:
        return

    if gpio == PHASE_A and level == 1:
        position += 1 if last_level == 0 else -1

    last_gpio = gpio
    last_level = level


pi = pigpio.pi()

pi.set_mode(PHASE_A, pigpio.INPUT)
pi.set_mode(PHASE_B, pigpio.INPUT)
pi.set_pull_up_down(PHASE_A, pigpio.PUD_UP)
pi.set_pull_up_down(PHASE_B, pigpio.PUD_UP)

pi.callback(PHASE_A, pigpio.EITHER_EDGE, phase_changed)
pi.callback(PHASE_B, pigpio.EITHER_EDGE, phase_changed)

last_gpio = PHASE_A
last_level = 1
position = 0
try:
    while True:
        print(position)
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    pass

pi.stop()
