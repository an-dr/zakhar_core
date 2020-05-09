from ..i2c import ZakharI2cDevice, bus
from .common import *
from ..logging import *

# CONFIG_LOG_LEVEL = logging.DEBUG
CONFIG_LOG_LEVEL = logging.INFO

ADDR_FACE = 0x2c
CMD_CALM = 0x30
CMD_BLINK = 0x31
CMD_ANGRY = 0x32
CMD_HAPPY = 0x33
CMD_SAD = 0x34

dev = ZakharI2cDevice("Face", bus, ADDR_FACE, CONFIG_LOG_LEVEL)
