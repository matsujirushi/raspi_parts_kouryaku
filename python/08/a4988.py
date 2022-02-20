import pigpio
import time

ROTATION = 2
STEP_PER_ROTATE = 200
MICROSTEP = 16

ENABLE = 10
MS1 = 9
MS2 = 11
MS3 = 5
RESET = 6
SLEEP = 13
STEP = 19
DIR = 26

WAIT = 0.005

pi = pigpio.pi()

for pin in [ENABLE, MS1, MS2, MS3, RESET, SLEEP, STEP, DIR]:
    pi.set_mode(pin, pigpio.OUTPUT)

pi.write(RESET, 0)

pi.write(SLEEP, 1)

pi.write(MS1, 1)
pi.write(MS2, 1)
pi.write(MS3, 1)
pi.write(DIR, 0)
pi.write(STEP, 0)

pi.write(ENABLE, 0)

time.sleep(0.001)
pi.write(RESET, 1)

for i in range(STEP_PER_ROTATE * MICROSTEP * ROTATION):
    pi.write(STEP, 1)
    time.sleep(WAIT / 2)
    pi.write(STEP, 0)
    time.sleep(WAIT / 2)
