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


class ZakharI2cDevice:
    def __init__(self, i2c_bus: SMBus, addr: int):
        self.bus = i2c_bus
        self.address = addr

    def write_byte_to(self, reg, val):
        self.bus.write_byte_data(self.address, reg, val)

    def write_bytes_to(self, reg, vals):
        self.bus.write_i2c_block_data(self.address, reg, vals)

    def read_byte_from(self, reg):
        self.bus.write_byte(self.address, reg)
        return self.bus.read_byte(self.address)

    def read_bytes_from(self, reg, num):
        vals = []
        for i in range(num):
            vals.append(self.read_byte_from(i))
        return vals
