from . import *
from ..i2c import *

ADDR_MOTORS = 0x2a # bus address
CMD_FORWARD = 119
CMD_BACKWARD = 115
CMD_LEFT = 97
CMD_RIGHT = 100
CMD_STOP = 32

dev = ZakharI2cDevice(bus, ADDR_MOTORS)