from multiprocessing import Process
from time import sleep
from zakhar_core import *


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