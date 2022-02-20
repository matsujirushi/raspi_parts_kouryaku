import wiringpi as pi

pi.wiringPiSetupGpio()
fd = pi.wiringPiI2CSetup(0x1D)
pi.wiringPiI2CWriteReg8(fd, 0x2D, 0x08)

while True:
  z_low = pi.wiringPiI2CReadReg8(fd, 0x36)
  z_high = pi.wiringPiI2CReadReg8(fd, 0x37)
  z = int.from_bytes([z_low, z_high], "little", signed=True)
  print(z * 2.0 / 2 ** (10 - 1))
  pi.delay(200)
