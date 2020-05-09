from ..common_object import CommonObject
import threading
import multiprocessing
import ctypes
from time import sleep
from .conscious import Conscious
from .responses import Responses
from .subconscious import Subconscious
from ..zk_common import *
from ..zk_programs import *

conscious_thread = None
subconscious_thread = None
responses_thread = None
main_logic_thread = None



def start_mind4():
    oled.dev.oled_license()
    face.dev.cmd(face.CMD_CALM)
    # c = threading.Thread(name='left right', target=prog_left_right_slow, args=[comm_obj])
    c = threading.Thread(name='walk', target=prog_m4_sqwalk_t, args=[comm_obj])
    r = threading.Thread(name='panic', target=prog_m4_panic, args=[comm_obj])
    s = threading.Thread(name='birdmon', target=prog_m4_birdmon_trig, args=[comm_obj])
    s.start()
    c.start()
    r.start()

if __name__ == "__main__":
    start_mind4()