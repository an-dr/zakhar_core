from .i2c import *
from ..logging import *
from time import sleep

REG_CMD = 0
REG_MODE = 1

CMD_NONE = 0xFF
CMD_DONE = 0x00
CMD_STOP = 0xA0

CONFIG_MAX_RETRY = 16

CONFIG_DEFAULT_LOG_LEVEL = logging.DEBUG

class ZakharI2cDevice:
    def __init__(self, name: str, i2c_bus: SMBus, addr: int, log_level=CONFIG_DEFAULT_LOG_LEVEL):
        self.name = name
        self.l = get_logger("%s (i2c_dev)" % self.name)
        self.l.setLevel(log_level)
        self.bus = i2c_bus
        self.address = addr

    def _read(self):
        attempts = CONFIG_MAX_RETRY
        while attempts:
            attempts -= 1
            try:
                byte_ = i2c_read_byte(self.address)
                return byte_
            except OSError:
                self.l.error("[%s] Fault (on _read %d/%d)" % (self.name,(CONFIG_MAX_RETRY - attempts),CONFIG_MAX_RETRY))
        raise error("After %d attempts" % CONFIG_MAX_RETRY)

    def _write(self, byte_):
        attempts = CONFIG_MAX_RETRY
        while attempts:
            attempts -= 1
            try:
                i2c_write_byte(self.address, byte_)
                return
            except OSError:
                self.l.error("[%s] Fault (on _write %d/%d)" % (self.name,(CONFIG_MAX_RETRY - attempts),CONFIG_MAX_RETRY))
        raise error("After %d attempts" % CONFIG_MAX_RETRY)

    def _write_to(self, reg_, byte_):
        attempts = CONFIG_MAX_RETRY
        while attempts:
            attempts -= 1
            try:
                i2c_write_byte_data(self.address, reg_, byte_)
                return
            except OSError:
                self.l.error("[%s] Fault (on _write -> reg %d/%d)" % (self.name,(CONFIG_MAX_RETRY - attempts),CONFIG_MAX_RETRY))
        raise error("After %d attempts" % CONFIG_MAX_RETRY)

    def write_byte_to(self, reg, val):
        # while True:
        #     try:
        #         self.bus.write_byte_data(self.address, reg, val)
        #         break
        #     except OSError:
        #         print("[%s] Fault (on write_byte_to): %s" % (self.name,str(OSError)))f
        self._write_to(reg,val)

    def write_byte_and_verify(self, reg, val):
        attempts = CONFIG_MAX_RETRY
        while attempts:
            attempts -= 1
            try:
                self.write_byte_to(reg, val)
                assert(val == self.read_byte_from(reg))
                sleep(0.1)
                # if self.read_byte_from(REG_CMD) != CMD_NONE:
                #     LOGW("Can't clear the CMD_REG")
                # else:
                #     return
            except (OSError,AssertionError):
                self.l.error("[%s] Fault (on write_byte_and_verify reg %d/%d)" % (self.name,(CONFIG_MAX_RETRY - attempts),CONFIG_MAX_RETRY))
        raise OSError("After %d attempts" % CONFIG_MAX_RETRY)



    def read_byte_from(self, reg):
        self._write(reg)
        return self._read()

    def read_bytes_from(self, reg, num):
        vals = []
        for i in range(num):
            vals.append(self.read_byte_from(i))
        return vals

    def cmd(self, val):
        # result = False
        # clear state
        # self.write_byte_to(REG_CMD, CMD_NONE)
        # if self.read_byte_from(REG_CMD) != CMD_NONE:
        #     raise error("Can't clear the CMD_REG")
        # write cmd
        self.l.debug("Send a command :%s" % hex(val) )
        self.write_byte_to(REG_CMD,val)
        # wait until done
        # cmd = 0xFF
        # while ( cmd != CMD_DONE):
        #     cmd = self.read_byte_from(REG_CMD)
        #     sleep(0.01) # wait

    def mode(self):
        s = self.read_byte_from(REG_MODE)
        return s

    def stop(self):
        self.cmd(0xA0)

