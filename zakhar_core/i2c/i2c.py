# from smbus import SMBus
from smbus2 import SMBus
from threading import Lock
from time import sleep
bus = SMBus(1)  # indicates /dev/ic2-1
i2c_mutex = Lock()
from ..logging import *

# CONFIG_LOG_LEVEL = logging.DEBUG
CONFIG_LOG_LEVEL = logging.INFO

l = get_logger("I2C")
l.setLevel(CONFIG_LOG_LEVEL)

def i2c_read_byte(addr):
    global i2c_mutex
    with i2c_mutex:
        b = bus.read_byte(addr)
        l.debug('Read byte %s from %s' % (hex(b), hex(addr)))
        return b

def i2c_write_byte(addr, val):
    global i2c_mutex
    with i2c_mutex:
        bus.write_byte(addr, val)
        l.debug('Wrote byte %s to %s' % (hex(val),hex(addr)))

def i2c_write_byte_data(addr, reg, val):
    global i2c_mutex
    with i2c_mutex:
        bus.write_byte_data(addr, reg, val)
        l.debug('Wrote byte %s from %s:%s' % (hex(val), hex(addr), hex(reg)))

def i2c_read_byte_from(addr, reg):
    global i2c_mutex
    with i2c_mutex:
        bus.write_byte(addr, reg)
        b = bus.read_byte(addr)
        l.debug('Read byte %s from %s:%s' % (hex(b), hex(addr), hex(reg)))
        return b

# def i2c_read_bytes_from(addr, reg, num):
#     global i2c_mutex
#     with i2c_mutex:
#         vals = []
#         for i in range(num):
#             vals.append(i2c_read_byte_from(addr, i))
#         return vals