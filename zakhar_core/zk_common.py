import time
import datetime
from .common_object import CommonObject
from .logging import *

CONFIG_LOG_LEVEL = logging.DEBUG


comm_obj = CommonObject()
log = get_logger("Zakhar (main log)")
log.setLevel(CONFIG_LOG_LEVEL)


def sleep_block(sec, block_common_field: str = None, block_state=None):
    """
    Standart, but block untill block_common_field will not block_state

    Parameters
    ----------
    sec : [type]
        [description]
    block_common_field : str
        [description]
    block_state : [type]
        [description]
    """
    global comm_obj
    time.sleep(sec)
    if comm_obj.get(block_common_field) == None:
        get_logger("Zakhar (sleep_block)").error("There is not field `%s`" %
                                                 block_common_field)
    else:
        if comm_obj[block_common_field] == block_state:
            get_logger("Zakhar (sleep_block)").info(
                    "Sleep for %s sec, then blocked until %s == %s" %
                    (str(sec), block_common_field, str(block_state)))
            while (comm_obj[block_common_field] == block_state):
                time.sleep(0.2)
