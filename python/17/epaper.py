import serial
import struct

def CommandFrame(command, parameter = bytes()):
  data = struct.pack('>BHB', 0xA5, 1 + 2 + 1 + len(parameter) + 4 + 1, command) + parameter + b'\xCC\x33\xC3\x3C'
  parity = 0
  for d in data:
    parity ^= d
  data += parity.to_bytes(1, 'little')
  return data

def ClearScreen():
  ser.write(CommandFrame(0x2E))
  ser.read(2)

def Refresh():
  ser.write(CommandFrame(0x0A))
  ser.read(2)

def DrawCircle(x0, y0, r):
  ser.write(CommandFrame(0x27, struct.pack('>HHH', x0, y0, r)))
  ser.read(2)

ser = serial.Serial('/dev/serial0', 115200, timeout = 10)

ClearScreen()
Refresh()
DrawCircle(255, 255, 128)
Refresh()
