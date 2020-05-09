
class CommonObject(dict):
    def __init__(self, *arg, **kw):
        super(CommonObject, self).__init__(*arg, **kw)

    def set_trig(self, name: str, state: bool):
        self["trigger_" + name] = state

    def read_trig(self, name: str):
        return self["trigger_" + name]

def change(o: CommonObject):
    o.set_trig("test", True)


if __name__ == "__main__":
    o = CommonObject({"trig": False})
    o.set_trig("test", True)
    o.set_trig("test", False)
    change(o)
    print(o)