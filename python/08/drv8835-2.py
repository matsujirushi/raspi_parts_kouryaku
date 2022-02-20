import pigpio
import time

ROTATION = 2
STEP_PER_ROTATE = 200
MICROSTEP = 2

AIN1 = 26
AIN2 = 19
BIN1 = 13
BIN2 = 6
PINS = [AIN1, BIN1, AIN2, BIN2]

WAIT = 0.005

STEPS = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

pi = pigpio.pi()

for pin in PINS:
    pi.set_mode(pin, pigpio.OUTPUT)
    pi.write(pin, 0)

for i in range(int(STEP_PER_ROTATE * MICROSTEP * ROTATION)):
    step = STEPS[i % len(STEPS)]
    for pin in range(len(PINS)):
        pi.write(PINS[pin], step[pin])
    time.sleep(WAIT)
