import VL53L1X
import signal
import time

tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open()

tof.start_ranging(1)    # 1:short, 2:medium, 3:long

running = True

def exit_handler(signal, frame):
    global running
    running = False

signal.signal(signal.SIGINT, exit_handler)

while running:
    distance = tof.get_distance()
    print(distance)

    time.sleep(1)

tof.stop_ranging()
