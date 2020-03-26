import threading
import time

class Subconscious (threading.Thread):
   def __init__(self, threadID, name, function):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.main_function = function

   def run(self):
      print ("Starting " + self.name)
      self.main_function()
