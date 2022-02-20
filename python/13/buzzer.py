import wiringpi as pi
pi.wiringPiSetupGpio()

pi.pinMode(18, pi.OUTPUT)
while True:
    pi.digitalWrite(18, pi.HIGH)
    pi.delayMicroseconds(500)
    pi.digitalWrite(18, pi.LOW)
    pi.delayMicroseconds(500)
