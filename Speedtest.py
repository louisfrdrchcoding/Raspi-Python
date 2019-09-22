import speedtest
import time
import Adafruit_SSD1306
servers = []

threads = None

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

result_dict = s.results.dict()



import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()
disp.clear()
disp.display()

width = disp.width
heigth = disp.height

image = Image.new('1', (width, heigth))

draw = ImageDraw.Draw(image)

font = ImageFont.load_default()
fontN = ImageFont.truetype('FreeSans.ttf', 30)
result = result_dict['ping']
res = '%d' % (result)

while True:

  draw.text((17, 3), "Ping: " + res, font=fontN, fill=500)
  disp.image(image)
  disp.display()
  time.sleep(3)
  disp.clear()
  disp.display()




