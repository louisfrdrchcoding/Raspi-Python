# How to print Hello World on a Adafruit 128x32 Display

# first install:
  # sudo apt-get update
  # sudo apt-get install build-essential python-dev python-pip
  # sudo pip install RPi.GPIO
  # sudo apt-get install python-imaging python-smbus
  # sudo apt-get install git
  # git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
  # cd  Adafruit_Python_SSD1306
  # sudo python3 setup.py install

# turn off Raspberry pi
# connect GND with Pin 6
# connect VCC with Pin 1
# connect SCL or SDK with Pin 5
# connect SDA with Pin 3




import Adafruit_SSD1306          # importing Modules
import time                      
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)     # declaring variable disp

disp.begin()            # initializing diplay

disp.clear()            # clearing display
                           
disp.display()          # displaying on display

image = Image.new('1', (128, 32))    # generating new image

draw = ImageDraw.Draw(image)         # drawing on image

font = ImageFont.load_default()      # loading font

draw.text((13, 10), "Hello World!", font=font, fill=255)   # printing text on display

disp.image(image)    # imaging on display

disp.display()       # displaying display

time.sleep(10)       # waiting 10s

disp.clear()         # clearing display
disp.display()       # displaying display


