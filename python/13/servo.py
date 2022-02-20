import wiringpi as pi
pi.wiringPiSetupGpio()

pi.pinMode(18, pi.PWM_OUTPUT)
pi.pwmSetMode(pi.PWM_MODE_MS)
pi.pwmSetClock(2)
pi.pwmSetRange(192000)
while True:
  for i in list(range(-90, 90, 10)) + list(range(90, -90, -10)):
    pi.pwmWrite(18, int(((i + 90) / 180 * (2.4 - 0.5) + 0.5) / 20 * 192000))
    pi.delay(200)
