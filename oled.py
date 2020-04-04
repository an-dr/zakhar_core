import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess


RST = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

    # disp.setRotation(2)





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


def oled_night():
    "This is for my GF, do not pay attention"

    disp.begin()
    disp.clear()
    disp.display()
    width = disp.width
    height = disp.height

    image1 = Image.new('1', (width, height))
        # Write two lines of text.
    draw = ImageDraw.Draw(image1)
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    padding = -2
    top = padding

    bottom = height-padding
    x = 0
    font = ImageFont.load_default()

    disp.clear()
    disp.display()
    draw.text((x, top),       "Good Night" ,  font=font, fill=255)
    draw.text((x, top+16),    "         Sveta! ",  font=font, fill=255)
    draw.text((x, top+25),    "                 Z.",  font=font, fill=255)

    # Display image.
    disp.image(image1)
    disp.display()
    time.sleep(2)

def oled_license():
    disp.begin()
    disp.clear()
    disp.display()
    width = disp.width
    height = disp.height

    image1 = Image.new('1', (width, height))
        # Write two lines of text.
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


def oled_init2():
    from oled.serial import i2c
    from oled.device import ssd1306, ssd1331, sh1106
    from oled.render import canvas

    # rev.1 users set port=0
    # substitute spi(device=0, port=0) below if using that interface
    serial = i2c(port=1, address=0x3C)

    # substitute ssd1331(...) or sh1106(...) below if using that device
    device = ssd1306(serial)
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((30, 40), "Hello World", fill="white")
