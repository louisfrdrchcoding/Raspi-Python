import Adafruit_SSD1306   #importing Module
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)


disp.begin()
width = disp.width

height = disp.height

image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

padding = 2
shape_width = 0

top = padding
bottom = height-padding
x=0

font = ImageFont.load_default()



