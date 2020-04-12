from ..i2c import ZakharI2cDevice, bus
from .common import *

ADDR_EYE = 0x2b
dev = ZakharI2cDevice(bus, ADDR_EYE)

eye_data = 0

class Eye():
    def __init__(self, i2c_bus, address: int):
        self.bus = i2c_bus
        self.addr = address

    def Read(self):
        d = 0
        try:
            pass
            # d = self.bus.read_word_data(self.addr,0)
            # d = i2c_read_32bit(self.addr,0)
        except OSError:
            pass
        return d

eye = Eye(bus, ADDR_EYE)


def eye_poll():
    while(1):
        global eye_data
        global trigger
        eye_data = eye.Read()
        if (eye_data < EYE_TRIGGER):
            trigger[0] = True
        else:
            trigger[0] = False
        sleep(.1)
        print(hex(eye_data)+ " | triggered = " + str(trigger[0]))

def eye_poll2():
    while(1):
        global eye_data
        global trigger
        global dev_eye
        eye_data_hi = dev_eye.read_byte_from(0)
        eye_data_lo = dev_eye.read_byte_from(1)
        eye_data = eye_data_hi << 8 | eye_data_lo
        if eye_data is not 0:
            if (eye_data < EYE_TRIGGER):
                trigger[0] = True
            else:
                trigger[0] = False
            sleep(.1)
            print(hex(eye_data)+ " | triggered = " + str(trigger[0]))