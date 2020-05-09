from ..common_object import CommonObject
import threading
import multiprocessing
import ctypes
from time import sleep
from .conscious import Conscious
from .responses import Responses
from .subconscious import Subconscious

class Mind2:
    def __init__(self, threadID, name, c_func, s_func, comm_obj: CommonObject):
        self.common = comm_obj
        self.common.set_trig(name="main", state=False)
        self.c_func = c_func
        self.s_func = s_func
        self.main_proc = None # type: threading.Thread or NoneType
        self.c = None # type: threading.Thread or NoneType
        self.s = None # type: threading.Thread or NoneType
        self.r = None # type: threading.Thread or NoneType
        # self.r = threading.Thread(3, "Responses", r_func)

    def new_c(self):
        if self.c is None:
            self.c = threading.Thread(name="Conscious", target=self.c_func, args=[self.common])

    def new_s(self):
        if self.s is None:
            self.s = threading.Thread(name="Subconscious", target=self.s_func, args=[self.common])

    def start_c(self):
        if self.c is not None:
            print("-> Starting Conscious")
            self.c.start()

    def start_s(self):
        if self.s is not None:
            print("-> Starting Subconscious")
            self.s.start()

    # def stop_c(self):
    #     if self.c is not None:
    #         print("-> Stopping Conscious")
    #         self.c.terminate()
    #         while self.c.is_alive():
    #             pass
    #         self.c = None

    # def stop_s(self):
    #     if self.s is not None:
    #         print("-> Stopping Subconscious")
    #         self.s.terminate()
    #         while self.s.is_alive():
    #             pass
    #         self.s = None

    def main_thread(self):
        self.new_c()
        self.new_s()
        self.start_c()
        self.start_s()
            # sleep(0.1)



    def start(self):
        print("Starting Mind's Main Process")
        self.main_thread()


    # def stop(self):
    #     print("Stopping Mind's Main Process")
    #     self.main_proc.terminate()
    #     while self.main_proc.is_alive():
    #         pass

