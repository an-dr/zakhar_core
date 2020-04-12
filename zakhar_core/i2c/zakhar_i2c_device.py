from .i2c import *
from time import sleep

REG_CMD = 0
REG_MODE = 1

CMD_NONE = 0xFF
CMD_DONE = 0x00
CMD_STOP = 0xA0

class ZakharI2cDevice:
    def __init__(self, i2c_bus: SMBus, addr: int):
        self.bus = i2c_bus
        self.address = addr

    def try_to(self, times, error, func, *args):
        try_no = 0
        while(try_no<times):
            try:
                return func(args)
            except error:
                print("Fault %d of %d tries" % (try_no+1, times))
            try_no+=1
        raise error("After %d tries" % times)


    def write_byte_to(self, reg, val):
        while True:
            try:
                self.bus.write_byte_data(self.address, reg, val)
                break
            except OSError:
                print("Fault: %s" % str(OSError))

    def test_write_byte_to(self, reg, val):
        self.try_to(5,OSError, self.bus.write_byte_data, reg, val)


    def write_byte_and_verify(self, reg, val):
        result = False
        self.write_byte_to(reg, val)
        while (self.read_byte_from(reg) != val):
            self.write_byte_to(reg,val)
            sleep(0.01) # wait

    def write_bytes_to(self, reg, vals):
        try:
            self.bus.write_i2c_block_data(self.address, reg, vals)
            return True
        except OSError:
            return False

    def cmd(self, val):
        result = False
        # clear state
        self.write_byte_and_verify(REG_CMD, CMD_NONE)
        # write cmd
        self.write_byte_to(REG_CMD,val)
        # wait until done
        cmd = 0xFF
        while ( cmd != CMD_DONE):
            cmd = self.read_byte_from(REG_CMD)
            sleep(0.01) # wait


    def stop(self):
        self.cmd(0xA0)

    def read_byte_from(self, reg):
        while True:
            try:
                self.bus.write_byte(self.address, reg)
                break
            except OSError:
                print("Fault: %s" % str(OSError))
        return self.bus.read_byte(self.address)

    def read_bytes_from(self, reg, num):
        vals = []
        for i in range(num):
            vals.append(self.read_byte_from(i))
        return vals