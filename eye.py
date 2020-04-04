from i2c import *

class Eye():
    def __init__(self, i2c_bus: SMBus, address: int):
        self.bus = i2c_bus
        self.addr = address

    def Read(self):
        d = 0
        try:
            # d = self.bus.read_word_data(self.addr,0)
            d = i2c_read_32bit(self.addr,0)
        except OSError:
            pass
        return d