import pigpio
import time
import queue

TRIG_PIN = 4
ECHO_PIN = 17

echo_time_span_queue = queue.Queue()

def echo_callback_func(gpio, level, tick):
    global echo_start_time
    if level == 1:
        echo_start_time = tick
    else:
        echo_end_time = tick
        echo_time_span = (echo_end_time - echo_start_time) / 1000000
        echo_time_span_queue.put(echo_time_span)

pi = pigpio.pi()

pi.set_mode(TRIG_PIN, pigpio.OUTPUT)
pi.set_mode(ECHO_PIN, pigpio.INPUT)
pi.set_pull_up_down(ECHO_PIN, pigpio.PUD_OFF)

echo_callback = pi.callback(ECHO_PIN, pigpio.EITHER_EDGE, echo_callback_func)

while True:
    pi.gpio_trigger(TRIG_PIN, 10, 1)

    distance = echo_time_span_queue.get() * 340 * 1000 / 2
    print(distance)

    time.sleep(1)
