import threading
import multiprocessing
import ctypes
import time
from time import sleep
from .conscious import Conscious
from .responses import Responses
from .subconscious import Subconscious

class noneProc:
    def is_alive():
        return False

class Mind(threading.Thread):
    def __init__(self, threadID, name, c_func, s_func, r_func, trig_list):
        threading.Thread.__init__(self)
        self.c_func = c_func
        self.r_func = r_func
        self.s_func = s_func
        self.c = noneProc
        self.s = noneProc
        self.r = noneProc
        self.trig = trig_list

    def routine(self):
        while(1):
            self.allow_subconscious()
            if self.isTriggered():
                self.allow_responses()
            else:
                self.allow_conscious()
            sleep(0.1)

    def isTriggered(self):
        return self.trig[0]

    def c_start(self):
        self.c = multiprocessing.Process(name="Conscious", target=self.c_func, daemon=True)
        self.c.start()

    def s_start(self):
        self.s = multiprocessing.Process(name="Subconscious", target=self.s_func, daemon=True)
        self.s.start()

    def r_start(self):
        self.r = multiprocessing.Process(name="Responses", target=self.r_func, daemon=True)
        self.r.start()

    def allow_conscious(self):
        if self.r.is_alive():
            self.r.terminate()
            while (self.r.is_alive()):
                pass
        if not self.c.is_alive():
            self.c_start()

    def allow_subconscious(self):
        if not self.s.is_alive():
            self.s_start()

    def allow_responses(self):
        if self.c.is_alive():
            self.c.terminate()
            while (self.c.is_alive()):
                pass
        if not self.r.is_alive():
            self.r_start()



    def run(self):
        print("Starting " + self.name)
        r = multiprocessing.Process(target=self.routine, name="Mind Routine")
        r.start()