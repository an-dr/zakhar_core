import threading
import ctypes
import time
from .conscious import Conscious
from .responses import Responses
from .subconscious import Subconscious


class Mind(threading.Thread):
    def __init__(self, threadID, name, c_func, s_func, r_func, trig_val):
        threading.Thread.__init__(self)
        self.c_func = c_func
        self.r_func = r_func
        self.s_func = s_func
        self.c = Conscious(1, "Conscious", c_func)
        self.s = Subconscious(2, "Subconscious", s_func)
        self.r = Responses(3, "Responses", r_func)
        self.trig = trig_val

    def routine(self):
        while(1):
            self.allow_subconscious()
            if self.isTriggered():
                self.allow_responses()
            else:
                self.allow_conscious()

    def isTriggered(self):
        return self.trig[0]

    def c_start(self):
        self.c = Conscious(1, "Conscious", self.c_func)
        self.c.start()

    def s_start(self):
        self.s = Subconscious(2, "Subconscious", self.s_func)
        self.s.start()

    def r_start(self):
        self.r = Responses(3, "Responses", self.r_func)
        self.r.start()

    def allow_conscious(self):
        if self.r.isAlive():
            self.r.stop()
            while (self.r.isAlive()):
                pass
        if not self.c.isAlive():
            self.c_start()

    def allow_subconscious(self):
        if not self.s.isAlive():
            self.s_start()

    def allow_responses(self):
        if self.c.isAlive():
            self.c.stop()
            while (self.c.isAlive()):
                pass
        if not self.r.isAlive():
            self.r_start()



    def run(self):
        print("Starting " + self.name)
        self.routine()