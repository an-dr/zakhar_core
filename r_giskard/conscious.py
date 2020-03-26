import threading
import time

class Conscious (threading.Thread):
   def __init__(self, threadID, name, function):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.main_function = function

   def run(self):
      print ("Starting " + self.name)
      try:
          self.main_function()
        finaly:
            print("Terminated " + self.name)

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')