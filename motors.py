from smbus import SMBus
from datetime import datetime

CMD_FORWARD = 119
CMD_BACKWARD = 115
CMD_LEFT = 97
CMD_RIGHT = 100
CMD_STOP = 32

class Motors_dc2platform:
    def __init__(self, i2c_bus: SMBus, address: int):
        self.bus = i2c_bus
        self.addr = address

    def __get_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    def MoveForward(self):
        cmd = CMD_FORWARD
        self.bus.write_byte(self.addr, cmd)
        print("%s - Sent %x to %x" % (self.__get_time(),cmd,self.addr))

    def MoveBackward(self):
        cmd = CMD_BACKWARD
        self.bus.write_byte(self.addr, CMD_BACKWARD)
        print("%s - Sent %x to %x" % (self.__get_time(),cmd,self.addr))

    def MoveLeft(self):
        cmd = CMD_LEFT
        self.bus.write_byte(self.addr, CMD_LEFT)
        print("%s - Sent %x to %x" % (self.__get_time(),cmd,self.addr))

    def MoveRight(self):
        cmd = CMD_RIGHT
        self.bus.write_byte(self.addr, CMD_RIGHT)
        print("%s - Sent %x to %x" % (self.__get_time(),cmd,self.addr))

    def Stop(self):
        cmd = CMD_STOP
        self.bus.write_byte(self.addr, CMD_STOP)
        print("%s - Sent %x to %x" % (self.__get_time(),cmd,self.addr))

