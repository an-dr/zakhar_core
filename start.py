from smbus import SMBus
from time import sleep
from datetime import datetime



addr = 0x2a # bus address
val = 0x1
bus = SMBus(1) # indicates /dev/ic2-1
while(1):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bus.write_byte(addr, val) # switch it on
    print("%s - Sent %x to %x" % (current_time,val,addr))
    sleep(1)
    val +=1
