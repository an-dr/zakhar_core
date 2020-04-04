from i2c import *
from time import sleep
from motors import *
from oled import *
from eye import Eye
from r_giskard import *
from multiprocessing import Process


# -----------------------------------------------------------------------------
# objects and constants
MOTORS_ADDR = 0x2a # bus address
EYE_ADDR = 0x2b
EYE_TRIGGER = 0x170

i2c_bus = SMBus(1) # indicates /dev/ic2-1
eye_i2c = ZakharI2cDevice(i2c_bus, EYE_ADDR)
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

def eye_poll2():
    while(1):
        global eye_data
        global trigger
        global eye_i2c
        eye_data_hi = eye_i2c.read_byte_from(0)
        eye_data_lo = eye_i2c.read_byte_from(1)
        eye_data = eye_data_hi << 8 | eye_data_lo
        if eye_data is not 0:
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
        sleep(0.3)

def shiver():
    while 1:
        motors.MoveLeft()
        sleep(0.05)
        # motors.Stop()
        # sleep(0.5)
        motors.MoveRight()
        sleep(0.05)
        # motors.Stop()

def start_mind():
    m = Mind(1, "Robot's Mind", shiver, eye_poll, freeze, trigger)
    m.start()

def reset():
    motors.Stop()

def send_i2c():
    while True:
        try:
            # bus.write_byte(EYE_ADDR,2)
            bus.write_byte_data(EYE_ADDR, 0,1)
            # bus.write_block_data(EYE_ADDR, 0, [ord('t'),ord('e'),ord('s'),ord('t'),0])
        except OSError:
            pass
        sleep(1)
        print("Sent")

def i2c_read_32bit(addr, reg):
    vals = bus.read_i2c_block_data(addr,reg,4)
    uint32val = (vals[3]<<24) | (vals[2]<<816) | (vals[1]<<8) | vals[0]
    print(hex(uint32val))
    return uint32val

def read_i2c():
    while True:
        try:
            i2c_read_32bit(EYE_ADDR,0)
            # i2c_read_32bit(EYE_ADDR,1)
            # v = bus.read_byte_data()
            # print("Read " + str(bus.read_byte(EYE_ADDR)))
            # print("Read " + str(bus.read_byte_data(EYE_ADDR,2)))
            # print("Read " + str(bus.read_byte_data(EYE_ADDR,0)))
            # bus.write_byte(EYE_ADDR,2)
            # bus.write_block_data(EYE_ADDR, 0, [ord('t'),ord('e'),ord('s'),ord('t'),0])
        except OSError:
            pass
        sleep(1)
        # print("Sent")


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # oled_init()
    # oled_night()
    oled_license()
    # reset()
    # input("press enter to start")

    # i2c_write_bytes_to(EYE_ADDR, 0, [0]*8)
    # i2c_write_bytes_to(EYE_ADDR, 2, [0xa2,0xa3,0xa4,0xa5, 0xa6, 0xa7])
    # print(i2c_read_bytes_from(EYE_ADDR,0,8))


    # content = eye.read_bytes_from(0, 12)
    # print(content)

    eye_poll2()