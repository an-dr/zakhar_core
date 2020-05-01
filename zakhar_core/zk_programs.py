from time import sleep
import click
import numpy as np
from .devices import *
from . import r_giskard
from .zk_common import *
from . import lizard_mind


@click.group()
def cli():
    face.dev.cmd(face.CMD_CALM)
    sleep(.5)
    pass


@cli.command()
def set_face():
    face.dev.cmd(face.CMD_CALM)
    while 1:
        pass


@cli.command()
def sqwalk():
    while (1):
        motors.dev.cmd(motors.CMD_FORWARD)
        sleep(1)
        motors.dev.cmd(motors.CMD_RIGHT)
        sleep(.2)
        motors.dev.cmd(motors.CMD_FORWARD)
        sleep(1)
        motors.dev.cmd(motors.CMD_RIGHT)
        sleep(.2)
        motors.dev.cmd(motors.CMD_FORWARD)
        sleep(1)
        motors.dev.cmd(motors.CMD_RIGHT)
        sleep(.2)
        motors.dev.cmd(motors.CMD_FORWARD)
        sleep(1)
        motors.dev.cmd(motors.CMD_RIGHT)
        sleep(.2)
        motors.dev.stop()


@cli.command()
def demo():
    face.dev.cmd(face.CMD_CALM)
    motors.dev.cmd(motors.CMD_RIGHT)
    sleep(.4)
    motors.dev.stop()
    sleep(3)
    face.dev.cmd(face.CMD_HAPPY)
    motors.dev.cmd(motors.CMD_RIGHT)
    sleep(.4)
    motors.dev.stop()
    sleep(3)
    face.dev.cmd(face.CMD_ANGRY)
    motors.dev.cmd(motors.CMD_RIGHT)
    sleep(.4)
    motors.dev.stop()
    sleep(3)
    face.dev.cmd(face.CMD_ANGRY)
    motors.dev.cmd(motors.CMD_RIGHT)
    sleep(.4)
    motors.dev.stop()
    sleep(3)


@cli.command()
def freeze():
    while 1:
        motors.dev.stop()
        sleep(0.3)


@cli.command()
def shiver():
    face.dev.cmd(face.CMD_SAD)
    while 1:
        motors.dev.cmd(motors.CMD_LEFT)
        sleep(0.005)
        motors.dev.cmd(motors.CMD_RIGHT)
        sleep(0.005)


@cli.command()
def lizard():
    m = r_giskard.Mind(1, "Robot's Mind", lizard_mind.c_sqwalk,
                       lizard_mind.u_eyepoll, lizard_mind.r_shiver,
                       lizard_mind.lizard_trigger)
    m.start()


@cli.command()
def start_mind():
    m = r_giskard.Mind(1, "Robot's Mind", shiver, eye_poll, freeze, trigger)
    m.start()


@cli.command()
def reset():
    motors.dev.cmd(CMD_STOP)


@cli.command()
def stresstest():
    def faces_test():
        face.dev.cmd(face.CMD_CALM)
        face.dev.cmd(face.CMD_BLINK)
        face.dev.cmd(face.CMD_CALM)
        face.dev.cmd(face.CMD_SAD)
        face.dev.cmd(face.CMD_ANGRY)

    faces_test()
    faces_test()
    eye.start_monitor_thread()
    while 1:
        motors.dev.cmd(motors.CMD_RIGHT)
        motors.dev.cmd(motors.CMD_LEFT)


@cli.command()
def eyepoll():
    eye.dev.start_polling(10)
    for i in range(5):
        print(hex(eye.dev.get_light()))
        sleep(1)
    eye.dev.stop_polling()
    for i in range(5):
        print(hex(eye.dev.get_light()))
        sleep(1)


@cli.command()
def birdmon():
    pattern= [0,0,255,0,0]
    eye.dev.start_polling(freq = 40)
    eye.dev.start_corr_measurements(500, pattern, 0.7)
    while True:
        if eye.dev.get_trig():
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


# ----------------------------------------------------------------------------
def zk_start():
    face.dev.cmd(face.CMD_CALM)


def zk_stop():
    sleep(0.05)
    motors.dev.cmd(motors.CMD_STOP)
    sleep(0.05)
    face.dev.cmd(face.CMD_CALM)
    sleep(0.1)
    face.dev.cmd(face.CMD_BLINK)
