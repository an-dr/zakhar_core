from smbus import SMBus
from time import sleep
from motors import Motors_dc2platform
from oled import oled_init
from eye import Eye

MOTORS_ADDR = 0x2a # bus address
EYE_ADDR = 0x2b
bus = SMBus(1) # indicates /dev/ic2-1
motors = Motors_dc2platform(bus, MOTORS_ADDR)
eye = Eye(bus, EYE_ADDR)

def random_walk():
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


if __name__ == "__main__":
    # oled_init()
    # # demo()
    # for i in range(5):
    #     random_walk()
    while(1):
        d = eye.Read()
        sleep(.01)
        print(hex(d))