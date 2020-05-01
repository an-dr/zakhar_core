from ..i2c import ZakharI2cDevice, bus
from .common import *
from time import sleep
import threading
import collections
import numpy as np
from PIL import Image

ADDR_EYE = 0x2b
REG_VAL_LO = 2
REG_VAL_HI = 3

POLL_PERIOD = 0.01  # sec
WINDOWS_SIZE_SEC = 0.6  # sec
WINDOW_SIZE_ELEMENTS = int(WINDOWS_SIZE_SEC / POLL_PERIOD)
eye_value = 0

class ZakharI2cDeviceEye(ZakharI2cDevice):
    def __init__(self, name: str, i2c_bus, addr: int):
        super().__init__(name, i2c_bus, addr)
        self.light = 0
        self.polling = False
        self.poll_freq = 0
        self.mon_window = None
        self.corr_pattern = None
        self.corr_coef = 0
        self.threshold = None

    def _read_light(self):
        lo = self.read_byte_from(REG_VAL_LO)
        hi = self.read_byte_from(REG_VAL_HI)
        return (hi << 8) | lo

    def __upd_light(self):
        self.light = self._read_light()
        if self.mon_window is not None:
            self.mon_window.append(self.light)

    def _polling(self, freq: int):
        self.poll_freq = freq
        print("[EYE] : Polling start")
        while 1:
            self.__upd_light()
            self.__calc_corrcoef()
            sleep(1 / self.poll_freq)
            if not self.polling:
                break
        self.poll_freq = 0
        print("[EYE] : Polling end")

    def _init_window(self, size_ms: int):
        win_el_num = int((size_ms/1000) * self.poll_freq)
        print("[EYE] : Windows inited, size is %d" % win_el_num)
        self.mon_window = collections.deque([0] * win_el_num,
                                            maxlen=win_el_num)
        return len(self.mon_window)

    def _deinit_window(self):
        self.mon_window = None

    def __patt_resize(self, in_list, new_size):
        #build rgb
        pat_rgb = []
        for i in in_list:
            pat_rgb.append([i, 0, 0])
        pixels = np.array([pat_rgb])
        #convert to image and resize
        new_image = Image.fromarray(pixels.astype('uint8'), 'RGB')
        image_resized = new_image.resize((new_size, 1))
        # retrieve resized list
        pixels = list(image_resized.getdata())
        l = []
        for i in pixels:
            l.append((i[0]))
        return l

    def calc_max_deviation(self, l):
        lmax = max(l)
        lmin = min(l)
        delta = lmax - lmin
        return delta / lmax

    def __calc_corrcoef(self):
        if self.corr_pattern is not None:
            if self.calc_max_deviation(self.mon_window) > 0.05:
                self.corr_coef = np.corrcoef(self.corr_pattern, self.mon_window)[1, 0]
                if self.corr_coef >= self.threshold:
                    print("Triggered! Correlation: %f" % self.corr_coef)
                    print(self.corr_pattern)
                    print(list(self.mon_window))
                    print(" --- ")
                elif self.corr_coef >= self.threshold / 2:
                    print("Correlation: %f" % self.corr_coef)
            else:
                self.corr_coef = 0

    def norm_minmax(self, a):
        norm_arr = []
        amin, amax = min(a), max(a)
        for i, val in enumerate(a):
            norm_arr.append((val-amin) / (amax-amin))
        return norm_arr

    def start_corr_measurements(self, corr_window_ms: int, pattern: list, threshold):
        win_sz = self._init_window(corr_window_ms)
        p_resized = self.__patt_resize(pattern, win_sz)
        p_norm = self.norm_minmax(p_resized)
        self.corr_pattern = p_norm
        self.threshold = threshold
        print("[EYE] : pattern ")
        print(self.corr_pattern)

    def get_corr_coef(self):
        return self.corr_coef

    def get_trig(self):
        if self.corr_coef >= self.threshold:
            return True
        else:
            return False

    def get_light(self):
        return self.light

    def start_polling(self, freq: int = 10):
        self.polling = True
        d = threading.Thread(name='daemon', target=self._polling, args=[freq])
        d.setDaemon(True)
        d.start()

    def stop_polling(self):
        self.polling = False


dev = ZakharI2cDeviceEye("Eye", bus, ADDR_EYE)






