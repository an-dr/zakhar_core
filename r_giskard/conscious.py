from . import base_part

class Conscious (base_part.BasePart):
    def __init__(self, threadID, name, function):
        super().__init__(threadID, name, function)
