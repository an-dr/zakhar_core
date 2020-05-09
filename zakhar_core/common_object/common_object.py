
class CommonObject(dict):
    __default_dict = {
    "stop_consience": False,
    }

    def __init__(self, *arg, **kw):
        super(CommonObject, self).__init__(*arg, **kw)
        self.update(CommonObject.__default_dict)

    def set_trig(self, name: str, state: bool):
        self["trigger_" + name] = state

    def read_trig(self, name: str):
        return self.get("trigger_" + name)

    def set_stop_consience(self, state:bool):
        self["stop_consience"] = state

    def get_stop_consience(self):
        return self.get('stop_consience')