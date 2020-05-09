from time import sleep, process_time
import datetime
import click
import numpy as np
from .devices import *
from . import r_giskard
from .zk_common import *
from . import lizard_mind
import threading
from .logging import *


def zk_stop(comm_obj: CommonObject = None):
    sleep(1)
    motors.dev.cmd(motors.CMD_STOP)
    sleep(0.1)
    motors.dev.cmd(motors.CMD_STOP)
    sleep(0.1)
    face.dev.cmd(face.CMD_BLINK)
    sleep(0.1)
    face.dev.cmd(face.CMD_BLINK)
    if comm_obj:
        comm_obj["started"] = False
        comm_obj["stop time"] = str(datetime.datetime.now())
    pass


def zk_start(comm_obj: CommonObject = None):
    start_time = datetime.datetime.now() - datetime.timedelta(seconds=time.process_time())
    log.info("Started at %s" % str(start_time))
    if comm_obj:
        comm_obj["started"] = True
        comm_obj["start time"] = str(start_time)
    motors.dev.cmd(motors.CMD_STOP)
    face.dev.cmd(face.CMD_CALM)
    sleep(.5)


def sqwalk_t(comm_obj:CommonObject = None):
    def cmd_stop(cmd, exec_time, stop_time):
        motors.dev.cmd(cmd)
        sleep_block(exec_time, "stop_consience", True)
        motors.dev.cmd(motors.CMD_STOP)
        sleep_block(stop_time, "stop_consience", True)

    while (1):
        cmd_stop(motors.CMD_FORWARD, 0.5,1)
        cmd_stop(motors.CMD_RIGHT, 0.2,1)


def prog_left_right(comm_obj: CommonObject = None):
    l = get_logger("prog_left_right")
    while (1):
        l.info("Right")
        motors.dev.cmd(motors.CMD_RIGHT)
        sleep_block(.5, "stop_consience", True)
        l.info("Left")
        motors.dev.cmd(motors.CMD_LEFT)
        sleep_block(.5, "stop_consience", True)

def prog_left_right_slow(comm_obj: CommonObject = None):
    l = get_logger("prog_left_right")
    while (1):
        l.info("Right")
        motors.dev.cmd(motors.CMD_RIGHT)
        sleep_block(.5, "stop_consience", True)
        motors.dev.cmd(motors.CMD_STOP)
        sleep_block(3, "stop_consience", True)
        l.info("Left")
        motors.dev.cmd(motors.CMD_LEFT)
        sleep_block(.5, "stop_consience", True)
        motors.dev.cmd(motors.CMD_STOP)
        sleep_block(3, "stop_consience", True)

def prog_birdmon(comm_obj:CommonObject = None):
    pattern = [0, 0, 255, 0, 0]
    eye.dev.start_polling(freq=40)
    eye.dev.start_corr_measurements(500, pattern, 0.7)
    while True:
        eye_trig_state = eye.dev.get_trig()
        if comm_obj:
            comm_obj.set_trig("birdmon", eye_trig_state)
        if eye_trig_state:
            # print("Corr: " + str(c))
            face.dev.cmd(face.CMD_SAD)
            motors.dev.cmd(motors.CMD_RIGHT)
            motors.dev.cmd(motors.CMD_LEFT)
            motors.dev.cmd(motors.CMD_RIGHT)
            motors.dev.cmd(motors.CMD_LEFT)
            motors.dev.cmd(motors.CMD_RIGHT)
            motors.dev.cmd(motors.CMD_LEFT)
            motors.dev.cmd(motors.CMD_STOP)
            motors.dev.cmd(motors.CMD_STOP)
            face.dev.cmd(face.CMD_CALM)
        else:
            sleep(eye.POLL_PERIOD)


def prog_birdmon_trig(comm_obj:CommonObject = None):
    pattern = [0, 0, 255, 0, 0]
    eye.dev.start_polling(freq=40)
    eye.dev.start_corr_measurements(500, pattern, 0.7)
    while True:
        eye_trig_state = eye.dev.get_trig()
        if eye_trig_state:
            if comm_obj:
                comm_obj.set_trig("birdmon", eye_trig_state)
                comm_obj["stop_consience"] = True
            print(">> waiting start")
            sleep(5)
            print(">> Continue")
            comm_obj["stop_consience"] = False
        else:
            sleep(eye.POLL_PERIOD)


def prog_shiver(comm_obj: CommonObject = None):
    def shiver_loop():
        face.dev.cmd(face.CMD_SAD)
        motors.dev.cmd(motors.CMD_SHIVER)
        sleep(1)
        face.dev.cmd(face.CMD_CALM)

    l = get_logger("shiver")
    while 1:
        if (comm_obj and comm_obj['stop_consience']):
            l.info("Shiver started")
            while comm_obj['stop_consience']:
                shiver_loop()
            l.info("Shiver stopped")
        elif not comm_obj:
            shiver_loop()
        else:
            sleep(0.5)


def prog_m4_panic(comm_obj: CommonObject = None):
    def shiver():
        motors.dev.cmd(motors.CMD_SHIVER)
        sleep(1)

    def flee():
        bright_light = eye.dev.get_light()
        dark_light = int(bright_light*1.5)
        light = bright_light
        motors.dev.cmd(motors.CMD_FORWARD)
        time.sleep(0.1)
        motors.dev.cmd(motors.CMD_FORWARD)
        log.info("Bright light: %x" % bright_light)
        log.info("Dark light: %x" % dark_light)
        while light <= dark_light:
            light = eye.dev.get_light()
            time.sleep(0.1)
            # log.info("Current light: %x" % light)
        motors.dev.cmd(motors.CMD_STOP)

    def wait_after():
        sleep(2)
        face.dev.cmd(face.CMD_CALM)
        sleep(1)

    l = get_logger("shiver")
    while 1:
        if (comm_obj and comm_obj.get_stop_consience()):
            l.info("Panic started")
            face.dev.cmd(face.CMD_SAD)
            shiver()
            flee()
            wait_after()
            face.dev.cmd(face.CMD_CALM)
            shiver()

            comm_obj.set_stop_consience(False)
            l.info("Shiver stopped")
        elif not comm_obj:
            shiver_loop()
        else:
            sleep(0.5)


def prog_m4_birdmon_trig(comm_obj:CommonObject = None):
    pattern = [0, 0, 255, 0, 0]
    eye.dev.start_polling(freq=40)
    eye.dev.start_corr_measurements(500, pattern, 0.7)
    while True:
        eye_trig_state = eye.dev.get_trig()
        if eye_trig_state:
            if comm_obj:
                comm_obj.set_trig("birdmon", eye_trig_state)
                comm_obj.set_stop_consience(True)
        else:
            sleep(eye.POLL_PERIOD)

def prog_m4_sqwalk_t(comm_obj:CommonObject = None):
    def cmd_stop(cmd, exec_time, stop_time):
        motors.dev.cmd(cmd)
        sleep_block(exec_time, "stop_consience", True)
        motors.dev.cmd(motors.CMD_STOP)
        sleep_block(stop_time, "stop_consience", True)

    cmd_stop(motors.CMD_FORWARD, 3,1)
    while (1):
        cmd_stop(motors.CMD_FORWARD, 0.5,1)
        cmd_stop(motors.CMD_RIGHT, 0.2,1)