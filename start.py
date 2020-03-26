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
bus = SMBus(1) # indicates /dev/ic2-1
motors = Motors_dc2platform(bus, MOTORS_ADDR)
eye = Eye(bus, EYE_ADDR)
eye_data = 0


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
        eye_data = eye.Read()
        sleep(.5)
        print(hex(eye_data))

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # oled_init()
    # # demo()
    # for i in range(5):
    #     random_walk()
    motors.Stop()
    input("press enter to start")
    c = Conscious(1, "test", random_walk)
    s = Subconscious(1, "test2", eye_poll)

    # c = Process(target=random_walk, daemon=True)
    # s = Process(target=eye_poll, daemon=True)

    c.start()
    s.start()