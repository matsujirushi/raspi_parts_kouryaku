import pigpio
import time

TRIG_PIN = 4
ECHO_PIN = 17

pi = pigpio.pi()

pi.set_mode(TRIG_PIN, pigpio.OUTPUT)
pi.set_mode(ECHO_PIN, pigpio.INPUT)
pi.set_pull_up_down(ECHO_PIN, pigpio.PUD_OFF)

while True:
    pi.gpio_trigger(TRIG_PIN, 10, 1)

    while pi.read(ECHO_PIN) != 1:
        pass
    echo_start_time = time.time()

    while pi.read(ECHO_PIN) != 0:
        pass
    echo_end_time = time.time()

    distance = (echo_end_time - echo_start_time) * 340 * 1000 / 2
    print(distance)

    time.sleep(1)
