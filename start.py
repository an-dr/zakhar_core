from smbus import SMBus
from time import sleep
from motors import *
from oled import oled_init
from eye import Eye
from r_giskard import *
from multiprocessing import Process


# -----------------------------------------------------------------------------
# objects and constants
MOTORS_ADDR = 0x2a # bus address
EYE_ADDR = 0x2b
EYE_TRIGGER = 0x300
bus = SMBus(1) # indicates /dev/ic2-1
motors = Motors_dc2platform(bus, MOTORS_ADDR)
eye = Eye(bus, EYE_ADDR)
eye_data = 0
trigger = [False]


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

def eye_poll():
    while(1):
        global eye_data
        global trigger
        eye_data = eye.Read()
        if (eye_data < EYE_TRIGGER):
            trigger[0] = True
        else:
            trigger[0] = False
        sleep(.1)
        print(hex(eye_data)+ " | triggered = " + str(trigger[0]))

# def trigger():
#     while True:
#         if (eye_data > 0x300):
#             break

def freeze():
    while 1:
        motors.Stop()

def shiver():
    while 1:
        motors.MoveLeft()
        sleep(0.05)
        motors.MoveRight()
        sleep(0.05)

def start_mind():
    m = Mind(1, "Robot's Mind", shiver, eye_poll, freeze, trigger)
    m.start()

def reset():
    motors.Stop()

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    oled_init()
    reset()
    input("press enter to start")
    start_mind()
    # shiver()
    # eye_poll()