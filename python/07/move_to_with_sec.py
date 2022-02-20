import numpy as np
import pigpio
from time import monotonic
from sys import argv

GPIO_PIN = 18

start_deg = float(argv[1])
end_deg = float(argv[2])
move_sec = float(argv[3])

cal_deg = [1,9,18,28,38,48,59,69,81,92,103,113,123,133,142,151,159,168,176]
cal_width = [710,803,897,990,1084,1177,1271,1365,1458,1552,1645,1739,1832,1926,2020,2113,2207,2300,2394]
deg_to_width = np.poly1d(np.polyfit(cal_deg, cal_width, 3))

pi = pigpio.pi()

start_time = monotonic()
end_time = start_time + move_sec

time_to_deg = np.poly1d(np.polyfit([start_time,end_time], [start_deg,end_deg], 1))

while True:
    now_time = monotonic()
    if now_time >= end_time:
        break
    pi.set_servo_pulsewidth(GPIO_PIN, deg_to_width(time_to_deg(now_time)))
    
pi.set_servo_pulsewidth(GPIO_PIN, deg_to_width(end_deg))
