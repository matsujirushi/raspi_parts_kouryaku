import serial
ser = serial.Serial('/dev/serial0', 9600, timeout = 0.5)

import binascii
import time

while True:
  ser.write(b'\x22\x00\x00\x22')
  data = ser.read(4)
  print(binascii.b2a_hex(data), ' -> ', end = '')
  distance = int.from_bytes(data[1:3], byteorder = 'big')
  print(distance, '[cm]')
  time.sleep(0.5)
