import serial
ser = serial.Serial('/dev/serial0', 9600, timeout = 0.5)

from micropyGPS import MicropyGPS
gps = MicropyGPS()

import re
gpzda = re.compile('^\$GPZDA,')

while True:
  line = ser.readline()
  if len(line) == 0:
    continue

  print(line)

  linestr = ''
  try:
    linestr = line.decode('ascii')
  except UnicodeDecodeError:
    continue

  for c in linestr:
    gps.update(c)

  if gpzda.match(linestr):
    print(gps.latitude, ' ', gps.longitude, ' ', gps.satellites_used)
