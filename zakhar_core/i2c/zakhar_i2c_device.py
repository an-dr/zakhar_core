from .i2c import *

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