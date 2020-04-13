from ..i2c import ZakharI2cDevice, bus
from .common import *
from time import sleep
import threading
import collections

ADDR_EYE = 0x2b
REG_VAL_LO = 2
REG_VAL_HI = 3

POLL_PERIOD = 0.05 # sec
WINDOWS_SIZE_SEC = 2 # sec

WINDOW_SIZE_ELEMENTS = int(WINDOWS_SIZE_SEC / POLL_PERIOD)

eye_value = 0

mon_window = collections.deque( [0] * WINDOW_SIZE_ELEMENTS,
                                maxlen=WINDOW_SIZE_ELEMENTS)

dev = ZakharI2cDevice("Eye", bus, ADDR_EYE)


def get_val():
    lo = dev.read_byte_from(REG_VAL_LO)
    hi = dev.read_byte_from(REG_VAL_HI)
    return (hi << 8) | lo


def eye_poll():
    global eye_value
    while True:
        eye_value = get_val()
        mon_window.append(eye_value)
        # print("Light: " + str(list(mon_window)))
        sleep(POLL_PERIOD)


def start_monitor_thread():
    d = threading.Thread(name='daemon', target=eye_poll)
    d.setDaemon(True)
    d.start()
