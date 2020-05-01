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
    eye.start_monitor_thread()
    pattern = ([0] * int(eye.WINDOW_SIZE_ELEMENTS / 2 - 3)) + [
        1, 1, 1, 1, 1, 1
    ] + ([0] * int(eye.WINDOW_SIZE_ELEMENTS / 2 - 3))
    while True:
        c = np.corrcoef(pattern, eye.mon_window)[1, 0]
        if c > 0.6:
            print("Corr: " + str(c))
            lizard_trigger[0] = True
            sleep(3)
        else:
            if c > 0.4:
                print("Corr: " + str(c))
            lizard_trigger[0] = False

def _u_dark():
    eye.start_monitor_thread()

def u_eyepoll():
    _u_birdmon()
