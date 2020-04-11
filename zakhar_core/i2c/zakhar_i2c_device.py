from .i2c import *

class ZakharI2cDevice:
    def __init__(self, i2c_bus: SMBus, addr: int):
        self.bus = i2c_bus
        self.address = addr

    def write_byte_to(self, reg, val):
        self.bus.write_byte_data(self.address, reg, val)

    def write_byte_and_verify(self, reg, val):
        self.write_byte_to(reg, val)
        while (self.read_byte_from(reg) != val):
            self.write_byte_to(reg, val)
            sleep(0.01) # wait

    def write_bytes_to(self, reg, vals):
        self.bus.write_i2c_block_data(self.address, reg, vals)

    def send_cmd(self, val):
        # clear state
        self.write_byte_and_verify(REG_CMD, CMD_NONE)
        # write cmd
        self.write_byte_to(REG_CMD,val)
        # wait until done
        while (self.read_byte_from(REG_CMD) != CMD_DONE):
            sleep(0.01) # wait


    def read_byte_from(self, reg):
        self.bus.write_byte(self.address, reg)
        return self.bus.read_byte(self.address)

    def read_bytes_from(self, reg, num):
        vals = []
        for i in range(num):
            vals.append(self.read_byte_from(i))
        return vals