# from smbus import SMBus
from smbus2 import SMBus
bus = SMBus(1) # indicates /dev/ic2-1

def i2c_read_byte(addr):
    return bus.read_byte(addr)

def i2c_write_byte_to(addr, reg, val):
    bus.write_byte_data(addr, reg, val)

def i2c_write_bytes_to(addr, reg, vals):
    bus.write_i2c_block_data(addr, reg, vals)

def i2c_read_byte_from(addr, reg):
    bus.write_byte(addr, reg)
    return bus.read_byte(addr)

def i2c_read_bytes_from(addr, reg, num):
    vals = []
    for i in range(num):
        vals.append(i2c_read_byte_from(addr, i))
    return vals