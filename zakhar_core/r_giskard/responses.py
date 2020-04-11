from . import base_part

class Responses (base_part.BasePart):
    # def __init__(self, threadID, name, function, cons, subc):
    def __init__(self, threadID, name, function):
        super().__init__(threadID, name, function)
        # self.conscious = cons
        # self.subconscious = subc
