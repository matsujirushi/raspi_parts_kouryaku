import pigpio
import datetime
import time

INTERVAL = 60

I2C_INTERFACE = 1

STTS751_ADDRESS = 0x39
STTS751_REG_TEMPERATURE_HIGH = 0x00
STTS751_REG_TEMPERATURE_LOW = 0x02
STTS751_REG_CONFIGURATION = 0x03

S5851A_ADDRESS = 0x48
S5851A_REG_TEMPERATURE = 0x00

AM2322_ADDRESS = 0x5c
AM2322_FUNC_READ_REGISTER = 0x03
AM2322_REG_TEMPERATURE_HIGH = 0x02

ADT7410_ADDRESS = 0x49
ADT7410_REG_TEMPERATURE_HIGH = 0x00
ADT7410_REG_CONFIGURATION = 0x03

SHT31_ADDRESS = 0x45

pi = pigpio.pi()

# STTS751
stts751_h = pi.i2c_open(I2C_INTERFACE, STTS751_ADDRESS)
pi.i2c_write_byte_data(stts751_h, STTS751_REG_CONFIGURATION, 0b10001100)    # 12bits
# S5851A
s5851a_h = pi.i2c_open(I2C_INTERFACE, S5851A_ADDRESS)
# AM2322
am2322_h = pi.i2c_open(I2C_INTERFACE, AM2322_ADDRESS)
# ADT7410
adt7410_h = pi.i2c_open(I2C_INTERFACE, ADT7410_ADDRESS)
pi.i2c_write_byte_data(adt7410_h, ADT7410_REG_CONFIGURATION, 0b10000000)    # 16bits
# SHT31
sht31_h = pi.i2c_open(I2C_INTERFACE, SHT31_ADDRESS)

print('"TIME","STTS751","S5851A","AM2322","ADT7410","SHT31"')
while True:
    # STTS751
    temp_h = pi.i2c_read_byte_data(stts751_h, STTS751_REG_TEMPERATURE_HIGH)
    temp_l = pi.i2c_read_byte_data(stts751_h, STTS751_REG_TEMPERATURE_LOW)
    stts751_temp = int.from_bytes([temp_h, temp_l], 'big', signed=True) / 256
    # S5851A
    (val_count, val) = pi.i2c_read_i2c_block_data(s5851a_h, S5851A_REG_TEMPERATURE, 2)
    s5851a_temp = int.from_bytes(val, 'big', signed=True) / 256
    # AM2322
    try:
        pi.i2c_write_quick(am2322_h, 0)
    except:
        pass
    time.sleep(0.0008)
    pi.i2c_write_quick(am2322_h, 0)
    pi.i2c_write_i2c_block_data(am2322_h, AM2322_FUNC_READ_REGISTER, [AM2322_REG_TEMPERATURE_HIGH, 2])
    time.sleep(0.0015)
    (val_count, val) = pi.i2c_read_device(am2322_h, 2 + 2 + 2)
    am2322_temp = int.from_bytes(val[2:4], 'big', signed=True) / 10
    # ADT7410
    (val_count, val) = pi.i2c_read_i2c_block_data(adt7410_h, ADT7410_REG_TEMPERATURE_HIGH, 2)
    adt7410_temp = int.from_bytes(val, 'big', signed=True) / 128
    # SHT31
    pi.i2c_write_device(sht31_h, [0x24, 0x00])
    time.sleep(0.015)
    (val_count, val) = pi.i2c_read_device(sht31_h, 2 + 1 + 2 + 1)
    sht31_temp = -45 + 175 * int.from_bytes(val[0:2], 'big', signed=False) / 65535

    print(f'{datetime.datetime.now()},{stts751_temp:.4f},{s5851a_temp:.4f},{am2322_temp:.4f},{adt7410_temp:.4f},{sht31_temp:.4f}')
    time.sleep(INTERVAL)
