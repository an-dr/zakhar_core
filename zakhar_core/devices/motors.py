from . import *
from ..i2c import *
from ..logging import *

# CONFIG_LOG_LEVEL = logging.DEBUG
CONFIG_LOG_LEVEL = logging.INFO

ADDR_MOTORS = 0x2a  # bus address
CMD_FORWARD = 119
CMD_BACKWARD = 115
CMD_LEFT = 97
CMD_RIGHT = 0x64
CMD_STOP = 32
CMD_SHIVER = 0x71

dev = ZakharI2cDevice("Motors", i2c_bus=bus, addr=ADDR_MOTORS, log_level=CONFIG_LOG_LEVEL)
