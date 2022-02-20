from l6470 import l6470
import time

ROTATION = 2
STEP_PER_ROTATE = 200
MICROSTEP = 128


def WaitWhileBusy():
    while True:
        status = device.updateStatus()
        print(status)
        if status["BUSY"] == 0:
            break
        time.sleep(0.001)


device = l6470.Device(0, 0)
device.resetDevice()

device.setParam(l6470.ACC, [0, 64])         # 931[step/s^2] * 250[ns]^2 / 2^-40
device.setParam(l6470.DEC, [0, 64])         # 931[step/s^2] * 250[ns]^2 / 2^-40
device.setParam(l6470.MAX_SPEED, [0, 16])   # x[step/s] * 250[ns] / 2^-18
device.setParam(l6470.MIN_SPEED, [0, 1])    # 0.2[step/s] * 250[ns] / 2^-24
device.setParam(l6470.KVAL_HOLD, [88])      # 5[V] / 14.5[V] * 256
device.setParam(l6470.KVAL_RUN, [150])      # 8.5[V] / 14.5[V] * 256
device.setParam(l6470.KVAL_ACC, [150])      # 8.5[V] / 14.5[V] * 256
device.setParam(l6470.KVAL_DEC, [150])      # 8.5[V] / 14.5[V] * 256
device.setParam(l6470.OCD_TH, [1])          # 700[mA] / 375[mA] - 1

device.goTo([int(i) for i in (STEP_PER_ROTATE * MICROSTEP * ROTATION).to_bytes(3, byteorder="big")])
WaitWhileBusy()
