import pigpio
import time

pi = pigpio.pi()
pi.bb_i2c_open(2, 3, 100000)

while True:
  result = pi.bb_i2c_zip(2, [4, 0x45, 2, 7, 2, 0x2c, 0x10, 2, 6, 6, 3, 0])
  
  if result[0] == 6:
    temp = -45 + 175 * int.from_bytes(result[1][0:2], 'big') / 65535
    humi = 100 * int.from_bytes(result[1][3:5], 'big') / 65535
    print('temp = {:.1f}, humi = {:.1f}'.format(temp, humi))

  time.sleep(1)
