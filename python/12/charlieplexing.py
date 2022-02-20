import wiringpi as pi
import time

WIRE0 = 16
WIRE1 = 20
WIRE2 = 21

def get_wire(num):
    if num == 0:
        return (WIRE0, WIRE1)
    elif num == 1:
        return (WIRE1, WIRE0)
    elif num == 2:
        return (WIRE1, WIRE2)
    elif num == 3:
        return (WIRE2, WIRE1)
    elif num == 4:
        return (WIRE2, WIRE0)
    elif num == 5:
        return (WIRE0, WIRE2)

def init_led():
    pi.wiringPiSetupGpio()
    for wire in (WIRE0, WIRE1, WIRE2):
        pi.pinMode(wire, pi.OUTPUT)
        pi.digitalWrite(wire, pi.LOW)
        pi.pinMode(wire, pi.INPUT)
        pi.pullUpDnControl(wire, pi.PUD_OFF)

def lighton_led(wire):
    pi.pinMode(wire[0], pi.OUTPUT)
    pi.pinMode(wire[1], pi.OUTPUT)
    pi.digitalWrite(wire[0], pi.HIGH)

def lightoff_led(wire):
    pi.digitalWrite(wire[0], pi.LOW)
    pi.pinMode(wire[0], pi.INPUT)
    pi.pinMode(wire[1], pi.INPUT)

init_led()

while True:
    for num in range(6):
        wire = get_wire(num)
        lighton_led(wire)
        time.sleep(0.2)
        lightoff_led(wire)

