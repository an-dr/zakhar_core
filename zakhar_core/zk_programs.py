from time import sleep
import click
from .devices import *
from .r_giskard import *
from .zk_common import *

@click.command()
def random_walk():
    while(1):
        motors.MoveForward()
        sleep(1)
        motors.MoveRight()
        sleep(.2)
        motors.MoveForward()
        sleep(1)
        motors.MoveRight()
        sleep(.2)
        motors.MoveForward()
        sleep(1)
        motors.MoveRight()
        sleep(.2)
        motors.MoveForward()
        sleep(1)
        motors.MoveRight()
        sleep(.2)
        motors.Stop()

@click.command()
def demo():
    motors.MoveRight()
    sleep(.4)
    motors.Stop()
    sleep(3)
    motors.MoveRight()
    sleep(.4)
    motors.Stop()
    sleep(3)
    motors.MoveRight()
    sleep(.4)
    motors.Stop()
    sleep(3)
    motors.MoveRight()
    sleep(.4)
    motors.Stop()
    sleep(3)

@click.command()
def freeze():
    while 1:
        motors.Stop()
        sleep(0.3)

@click.command()
def shiver():
    while 1:
        motors.MoveLeft()
        sleep(0.05)
        motors.MoveRight()
        sleep(0.05)

@click.command()
def start_mind():
    m = Mind(1, "Robot's Mind", shiver, eye_poll, freeze, trigger)
    m.start()

@click.command()
def reset():
    motors.Stop()
