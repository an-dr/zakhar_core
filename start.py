from smbus import SMBus
from time import sleep
from datetime import datetime

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess


CMD_FORWARD = 119
CMD_BACKWARD = 115
CMD_LEFT = 97
CMD_RIGHT = 100
CMD_STOP = 32


addr = 0x2a # bus address
bus = SMBus(1) # indicates /dev/ic2-1

def exec_cmd(cmd):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bus.write_byte(addr, CMD_STOP)
    sleep(.2)
    bus.write_byte(addr, cmd)
    print("%s - Sent %x to %x" % (current_time,cmd,addr))

def oled_init():
    RST = 0

    disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
    disp.begin()
    disp.clear()
    disp.display()

    width = disp.width
    height = disp.height

    image1 = Image.new('1', (width, height))

    draw = ImageDraw.Draw(image1)
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    padding = -2
    top = padding

    bottom = height-padding
    x = 0
    font = ImageFont.load_default()

    # Write two lines of text.

    disp.clear()
    disp.display()
    draw.text((x, top),       "Hello! I'm Zakhar!" ,  font=font, fill=255)
    # draw.text((x, top+8),     "About my developer:",  font=font, fill=255)
    draw.text((x, top+16),    "GPLv3 (c) 2020 ",  font=font, fill=255)
    draw.text((x, top+25),    "      Andrei Gramakov",  font=font, fill=255)

    # Display image.
    disp.image(image1)
    disp.display()
    time.sleep(2)

    # if disp.height == 64:
    #    image = Image.open('img1.png').convert('1')
    # else:
    #    image = Image.open('img1.png').convert('1')

    # disp.image(image)
    # disp.display()
    # time.sleep(2)

    # if disp.height == 64:
    #    image = Image.open('img3.jpg').convert('1')
    # else:
    #    image = Image.open('img3.jpg').convert('1')


def random_walk():
    exec_cmd(CMD_FORWARD)
    sleep(1)
    exec_cmd(CMD_RIGHT)
    sleep(.2)
    exec_cmd(CMD_FORWARD)
    sleep(1)
    exec_cmd(CMD_RIGHT)
    sleep(.2)
    exec_cmd(CMD_FORWARD)
    sleep(1)
    exec_cmd(CMD_RIGHT)
    sleep(.2)
    exec_cmd(CMD_FORWARD)
    sleep(1)
    exec_cmd(CMD_RIGHT)
    sleep(.2)
    exec_cmd(CMD_STOP)


# bus.write_byte(addr, CMD_BACKWARD)
# print("%s - Sent %x to %x" % (current_time,CMD_BACKWARD,addr))
# sleep(.3)


if __name__ == "__main__":
    oled_init()
    # random_walk()