from time import sleep
import click
import numpy as np
from .devices import *
from .r_giskard import *
from .zk_common import *

lizard_trigger = [False]


def c_sqwalk():
    face.dev.cmd(face.CMD_CALM)
    while (1):
        motors.dev.cmd(motors.CMD_LEFT)
        print("CMD_LEFT")
        sleep(1)
        motors.dev.cmd(motors.CMD_RIGHT)
        print("CMD_RIGHT")
        sleep(1)


def r_shiver():
    face.dev.cmd(face.CMD_SAD)
    while 1:
        motors.dev.cmd(motors.CMD_LEFT)
        sleep(0.005)
        motors.dev.cmd(motors.CMD_RIGHT)
        sleep(0.005)


def s_none():
    while 1:
        sleep(1)


def _u_birdmon():
    np.seterr(divide='ignore', invalid='ignore')
    pattern= [0,0,255,0,0]
    eye.dev.start_polling(freq = 40)
    eye.dev.start_corr_measurements(500, pattern, 0.6)
    while True:
        if eye.dev.get_trig():
            lizard_trigger[0] = True
            sleep(3)
        else:
            lizard_trigger[0] = False

def _u_dark():
    eye.start_monitor_thread()

def u_eyepoll():
    _u_birdmon()
