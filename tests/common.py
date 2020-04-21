import unittest
import inspect
import logging
from time import sleep, time
from zakhar_core import devices, __version__
from zakhar_core import zk_programs

STRESSTEST_CYCLES = 32


def LOGD(message):
    logging.getLogger().debug(message)

def LOGI(message):
    logging.getLogger().info(message)

def LOGW(message):
    logging.getLogger().warning(message)

def LOGE(message):
    logging.getLogger().error(message)


def get_commands(obj):
    members = inspect.getmembers(obj)
    results = []
    for i in members:
        pref = i[0][0:4]
        if pref == "CMD_":
            results.append(i)
    return results
