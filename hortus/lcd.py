#-*- coding: utf-8 -*-

import time

import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def status(relay):
    if (relay == True):
        return "ON"
    else:
        return "OFF"

def lcd(dht, precip, capacity, relay1, relay2, relay3, relay4, auto):
    # Raspberry Pi pin configuration:
    RST = None     # on the PiOLED this pin isnt used

    disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
    #disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
    # Initialize library.
    disp.begin()

    # Clear display.
    disp.clear()
    disp.display()

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
    padding = -2
    top = padding
    bottom = height-padding
    # Move left to right keeping track of the current x position for drawing shapes.
    x = 0
    # Load default font.
    font = ImageFont.load_default()
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    draw.text((x, top),       " | T: " + str(dht[0]) + "°C | H: " + str(dht[1]) + "% |" ,  font=font, fill=255)
    draw.text((x, top+8),     " | Pluie : " + str(precip) + "% |",  font=font, fill=255)
    draw.text((x, top+16),    " | Cuve:" + str(round(capacity)) + "% | Auto:" + str(auto), font=font, fill=255)
    draw.text((x, top+24),    " | P1: " + status(relay1) + " | P2:" + status(relay2) + " |", font=font, fill=255)
    draw.text((x, top+32),    " | Puit:" + str(round(capacity)) + "% |", font=font, fill=255)
    draw.text((x, top+40),    " | P3: " + status(relay3) + " | P4:" + status(relay4) + " |" , font=font, fill=255)
    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)