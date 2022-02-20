import wiringpi as pi
from ctypes import c_short

pi.wiringPiSetupGpio()
fd = pi.wiringPiI2CSetup(0x1D)
pi.wiringPiI2CWriteReg8(fd, 0x2D, 0x08)

while True:
  z = pi.wiringPiI2CReadReg16(fd, 0x36)
  if (z > 32767):
    z -= 65536
  print(z * 2.0 / 2 ** (10 - 1))
  pi.delay(200)
