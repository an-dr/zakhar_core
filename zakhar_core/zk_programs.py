from time import sleep
import click
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
        motors.dev.Stop()

@cli.command()
def demo():
    face.dev.cmd(face.CMD_CALM)
    motors.dev.cmd(motors.CMD_RIGHT)
    sleep(.4)
    motors.dev.Stop()
    sleep(3)
    motors.dev.cmd(motors.CMD_RIGHT)
    sleep(.4)
    motors.dev.Stop()
    sleep(3)
    motors.dev.cmd(motors.CMD_RIGHT)
    sleep(.4)
    motors.dev.Stop()
    sleep(3)
    motors.dev.cmd(motors.CMD_RIGHT)
    sleep(.4)
    motors.dev.Stop()
    sleep(3)

@cli.command()
def freeze():
    while 1:
        motors.dev.Stop()
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
def test():
    from .i2c import ZakharI2cDevice, bus
    dev = ZakharI2cDevice(bus, 0x2a)
    dev.test_write_byte_to(0, 12)

@cli.command()
def stresstest():
    face.dev.cmd(face.CMD_CALM)
    face.dev.cmd(face.CMD_BLINK)
    face.dev.cmd(face.CMD_CALM)
    face.dev.cmd(face.CMD_SAD)
    face.dev.cmd(face.CMD_ANGRY)
    while 1:
        motors.dev.cmd(motors.CMD_RIGHT)
        motors.dev.cmd(motors.CMD_LEFT)



def zk_stop():
    sleep(0.05)
    motors.dev.cmd(motors.CMD_STOP)
    sleep(0.05)
    face.dev.cmd(face.CMD_CALM)
    sleep(0.1)
    face.dev.cmd(face.CMD_BLINK)

