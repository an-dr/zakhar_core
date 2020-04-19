from multiprocessing import Process
from time import sleep
from zakhar_core import *
import click
import atexit




# -----------------------------------------------------------------------------
if __name__ == "__main__":
    atexit.register(zk_programs.zk_stop)
    zk_programs.cli()
    # while(1):
        # pass
    # oled_init()
    # oled_night()
    # dev.oled_license()
    # shiver()
    # zk_programs.reset()
    # input("press enter to start")

    # i2c_write_bytes_to(EYE_ADDR, 0, [0]*8)
    # i2c_write_bytes_to(EYE_ADDR, 2, [0xa2,0xa3,0xa4,0xa5, 0xa6, 0xa7])
    # print(i2c_read_bytes_from(EYE_ADDR,0,8))


    # content = eye_i2c.read_bytes_from(0, 12)
    # print(content)

    # eye_poll2()