# from smbus import SMBus
from smbus2 import SMBus
from threading import Lock
bus = SMBus(1)  # indicates /dev/ic2-1
i2c_mutex = Lock()

def i2c_read_byte(addr):
    global i2c_mutex
    with i2c_mutex:
        return bus.read_byte(addr)

def i2c_write_byte(addr, val):
    global i2c_mutex
    with i2c_mutex:
        return bus.write_byte(addr, val)

def i2c_write_byte_data(addr, reg, val):
    global i2c_mutex
    with i2c_mutex:
        bus.write_byte_data(addr, reg, val)

def i2c_write_i2c_block_data(addr, reg, vals):
    global i2c_mutex
    with i2c_mutex:
        bus.write_i2c_block_data(addr, reg, vals)

def i2c_read_byte_from(addr, reg):
    global i2c_mutex
    with i2c_mutex:
        bus.write_byte(addr, reg)
        return bus.read_byte(addr)

def i2c_read_bytes_from(addr, reg, num):
    global i2c_mutex
    with i2c_mutex:
        vals = []
        for i in range(num):
            vals.append(i2c_read_byte_from(addr, i))
        return vals