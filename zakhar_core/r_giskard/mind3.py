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

c_o = None # common object


def start_conscious(main_func):
    global conscious_thread
    conscious_thread = threading.Thread(name='Conscious(main)',
                                        target=main_func)
    conscious_thread.start()


def start_subconscious(back_func):
    global subconscious_thread
    subconscious_thread = threading.Thread(name='Subconscious(backgroound)',
                                           target=back_func)
    subconscious_thread.start()


def start_responses(altern_func):
    global responses_thread
    responses_thread = threading.Thread(name='Responses(second_main)',
                                        target=back_func)
    responses_thread.start()

def _mind_logic(main_func, back_func, altern_func):
    global conscious_thread
    global subconscious_thread
    global responses_thread
    global main_logic_thread
    if main_func:
        start_conscious(main_func)
    if back_func:
        start_subconscious(back_func)
    if altern_func:
        start_subconscious(altern_func)



def start_mind_subprocess(main_func, back_func, altern_func):

    main_logic_thread = threading.Thread(name='Mind logic',
                                        target=_mind_logic,
                                        args=(main_func, back_func, altern_func)
                                        )
    main_logic_thread.start()


def mind3_start( main_func=None, back_func=None, altern_func=None, poll_func=None, comm_obj=None ):
    global c_o
    if comm_obj:
        c_o = comm_obj
    start_mind_subprocess(main_func, back_func, altern_func)
    if poll_func:
        poll_func()
