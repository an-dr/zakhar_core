from ..i2c import ZakharI2cDevice, bus
from .common import *
from time import sleep
from ..logging import *
import threading
import collections
import numpy as np
from PIL import Image

# CONFIG_LOG_LEVEL = logging.DEBUG
CONFIG_LOG_LEVEL = logging.INFO

CONFIG_PRINT_HALF_CORR = False
CONFIG_PRINT_WINDOW = False
CONFIG_PRINT_LIGHT = False

ADDR_EYE = 0x2b
REG_VAL_LO = 2
REG_VAL_HI = 3

POLL_PERIOD = 0.01  # sec
WINDOWS_SIZE_SEC = 0.6  # sec
WINDOW_SIZE_ELEMENTS = int(WINDOWS_SIZE_SEC / POLL_PERIOD)
eye_value = 0

l = get_logger("Eye")

class ZakharI2cDeviceEye(ZakharI2cDevice):
    def __init__(self, name: str, i2c_bus, addr: int, log_level):
        super().__init__(name, i2c_bus, addr,log_level)
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
        val = (hi << 8) | lo
        if CONFIG_PRINT_LIGHT:
            l.info("Light : " + hex(val))
        return val

    def __upd_light(self):
        self.light = self._read_light()
        if self.mon_window is not None:
            if self.light != 0 and self.light != 0xffff: # if the value is wrong - don't count it
                self.mon_window.append(self.light)
            if CONFIG_PRINT_WINDOW:
                l.info("h'" + list2strf(list(self.mon_window),5, in_hex=True))

    def _polling(self, freq: int):
        self.poll_freq = freq
        l.info("Polling start")
        while 1:
            self.__upd_light()
            self.__calc_corrcoef()
            sleep(1 / self.poll_freq)
            if not self.polling:
                break
        self.poll_freq = 0
        l.info("Polling end")

    def _init_window(self, size_ms: int):
        win_el_num = int((size_ms/1000) * self.poll_freq)
        l.info("Windows inited, size is %d" % win_el_num)
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
        if not delta:
            return 0
        return delta / lmax

    def round_list(self, l, num):
        new_l = []
        for i in l:
            new_l.append(round(i, num))
        return new_l

    def __calc_corrcoef(self):
        if self.corr_pattern is not None:
            if self.calc_max_deviation(self.mon_window) > 0.05:
                self.corr_coef = np.corrcoef(self.corr_pattern, self.mon_window)[1, 0]
                if self.corr_coef >= self.threshold:
                    l.info("Triggered! Correlation: %f" % self.corr_coef)
                    l.info(self.round_list(self.corr_pattern,1))
                    l.info(self.round_list(list(self.mon_window),1))
                    l.info(" --- ")
                elif self.corr_coef >= self.threshold / 2:
                    if CONFIG_PRINT_HALF_CORR:
                        l.info("Correlation: %f" % self.corr_coef)
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
        l.info("pattern ")
        l.info(self.round_list(self.corr_pattern,2))

    def get_corr_coef(self):
        return self.corr_coef

    def get_trig(self)->bool:
        if self.corr_coef >= self.threshold:
            return True
        else:
            return False

    def get_light(self):
        return self.light

    def start_polling(self, freq: int = 10):
        self.polling = True
        d = threading.Thread(name='[EYE]polling', target=self._polling, args=[freq])
        d.setDaemon(True)
        d.start()

    def stop_polling(self):
        self.polling = False


dev = ZakharI2cDeviceEye("Eye", bus, ADDR_EYE, CONFIG_LOG_LEVEL)






