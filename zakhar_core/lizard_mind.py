from time import sleep
import click
import numpy as np
from .devices import *
from .r_giskard import *
from .zk_common import *
from .logging import *

lizard_trigger = [False]

def prog_left_right(comm_obj: CommonObject = None):
    l = get_logger("prog_left_right")
    sleep(3)
    while (1):
        l.info("Right")
        motors.dev.cmd(motors.CMD_RIGHT)
        sleep(.5)
        l.info("Left")
        motors.dev.cmd(motors.CMD_LEFT)
        sleep(.5)

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


def prog_birdmon_trig(comm_obj:CommonObject = None):
    pattern = [0, 0, 255, 0, 0]
    eye.dev.start_polling(freq=40)
    eye.dev.start_corr_measurements(500, pattern, 0.7)
    while True:
        eye_trig_state = eye.dev.get_trig()
        if comm_obj:
            comm_obj.set_trig("birdmon", eye_trig_state)
        else:
            sleep(eye.POLL_PERIOD)


def _u_dark():
    eye.start_monitor_thread()

def r_face():
    motors.dev.stop()
    face.dev.cmd(face.CMD_SAD)
    sleep(1)
    face.dev.cmd(face.CMD_CALM)


def none():
    while 1:
        sleep(1)


mind = Mind(threadID=1,
            name="Lisard's Mind",
            c_func=prog_left_right,
            s_func=prog_birdmon_trig,
            r_func=r_shiver,
            trig_list=lizard_trigger)
