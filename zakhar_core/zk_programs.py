from time import sleep
import click
import numpy as np
from .devices import *
from .r_giskard import *
from .zk_common import *


@click.group()
def cli():
    face.dev.cmd(face.CMD_CALM)
    sleep(.5)
    pass

@cli.command()
def random_walk():
    while(1):
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
    motors.dev.cmd(motors.CMD_RIGHT)
    sleep(.4)
    motors.dev.stop()
    sleep(3)
    motors.dev.cmd(motors.CMD_RIGHT)
    sleep(.4)
    motors.dev.stop()
    sleep(3)
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
def birdmon():
    eye.start_monitor_thread()
    pattern = ([0]*int(eye.WINDOW_SIZE_ELEMENTS/2-1)) + [1, 1,] + ([0]*int(eye.WINDOW_SIZE_ELEMENTS/2-1))
    while True:
        c = np.corrcoef(pattern, eye.mon_window)[1, 0]
        if c >0.7:
            print ("Corr: "+str(c))
            face.dev.cmd(face.CMD_SAD)
            motors.dev.cmd(motors.CMD_RIGHT)
            motors.dev.cmd(motors.CMD_LEFT)
            motors.dev.cmd(motors.CMD_RIGHT)
            motors.dev.cmd(motors.CMD_LEFT)
            motors.dev.cmd(motors.CMD_RIGHT)
            motors.dev.cmd(motors.CMD_LEFT)
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

