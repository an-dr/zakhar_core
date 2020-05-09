from time import sleep
import click
import numpy as np
from .devices import *
from . import r_giskard
from .zk_common import *
from .zk_programs import *
from . import lizard_mind
import threading
import atexit

@click.group()
def cli():
    atexit.register(zk_stop, comm_obj)
    zk_start(comm_obj)
    pass

""" Commands
   ********************************************************************* """


@cli.command()
def set_face():
    face.dev.cmd(face.CMD_CALM)
    while 1:
        pass


@cli.command()
def sqwalk():
    sqwalk_t()


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
    motors.dev.cmd(motors.CMD_SHIVER)
    sleep(1)
    face.dev.cmd(face.CMD_CALM)
    # while 1:
    #     motors.dev.cmd(motors.CMD_LEFT)
    #     sleep(0.005)
    #     motors.dev.cmd(motors.CMD_RIGHT)
    #     sleep(0.005)


@cli.command()
def lizard():
    lizard_mind.mind.start()


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
    prog_birdmon()

@cli.command()
def birdmon_trig():
    prog_birdmon_trig()


@cli.command()
def test_1():
    d = threading.Thread(name='birdmon', target=prog_birdmon_trig)
    s = threading.Thread(name='left right', target=prog_left_right)
    d.start()
    s.start()


@cli.command()
def liza2():
    m = r_giskard.Mind2(1, "Robot's Mind", sqwalk_t, birdmon_trig, comm_obj=comm_obj)
    m.start()
    # while (1):
        # print(comm_obj.read_trig("main"))
        # sleep(0.01)

@cli.command()
def liza3():
    r_giskard.mind3_start(
        main_func = prog_shiver,
        poll_func=birdmon_trig,
        altern_func=sqwalk_t,
        comm_obj = comm_obj)


@cli.command()
def liza4():
    r_giskard.start_mind4()

@cli.command()
def stop():
    zk_stop()


"""********************************************************************** Commands"""
