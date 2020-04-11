from time import sleep
import click
from . import devices
from .r_giskard import *
from .zk_common import *


@click.group()
def cli():
    pass

@cli.command()
def random_walk():
    while(1):
        devices.motors.MoveForward()
        sleep(1)
        devices.motors.MoveRight()
        sleep(.2)
        devices.motors.MoveForward()
        sleep(1)
        devices.motors.MoveRight()
        sleep(.2)
        devices.motors.MoveForward()
        sleep(1)
        devices.motors.MoveRight()
        sleep(.2)
        devices.motors.MoveForward()
        sleep(1)
        devices.motors.MoveRight()
        sleep(.2)
        devices.motors.Stop()

@cli.command()
def demo():
    devices.face.send_cmd(devices.CMD_FACE_CALM)
    devices.motors.MoveRight()
    sleep(.4)
    devices.motors.Stop()
    sleep(3)
    devices.motors.MoveRight()
    sleep(.4)
    devices.motors.Stop()
    sleep(3)
    devices.motors.MoveRight()
    sleep(.4)
    devices.motors.Stop()
    sleep(3)
    devices.motors.MoveRight()
    sleep(.4)
    devices.motors.Stop()
    sleep(3)

@cli.command()
def freeze():
    while 1:
        devices.motors.Stop()
        sleep(0.3)

@cli.command()
def shiver():
    while 1:
        devices.motors.MoveLeft()
        sleep(0.05)
        devices.motors.MoveRight()
        sleep(0.05)

@cli.command()
def start_mind():
    m = r_giskard.Mind(1, "Robot's Mind", shiver, eye_poll, freeze, trigger)
    m.start()

@cli.command()
def reset():
    devices.motors.Stop()

def zk_stop():
    devices.motors.Stop()
    devices.face.send_cmd(devices.CMD_FACE_BLINK)
