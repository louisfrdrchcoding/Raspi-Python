# how to print Speedtest results on Adafruit 128x32 display

# first download:
   # pip install speedtest-cli 




import speedtest
import time                 # importing modules
import Adafruit_SSD1306   

servers = []             

threads = None

s = speedtest.Speedtest()     
s.get_servers(servers)
s.get_best_server()            # making Speedtest
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

result_dict = s.results.dict()      # list with Speedtest results in variable result_dict


import time
from PIL import Image                  
from PIL import ImageDraw      # importing display modules
from PIL import ImageFont


disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()
disp.clear()                   # preparing display for usage
disp.display()

image = Image.new('1', (128, 32))  # new image

draw = ImageDraw.Draw(image)

font = ImageFont.load_default()
fontN = ImageFont.truetype('FreeSans.ttf', 30)

result = result_dict['ping']         # getting Ping results from the list 'result_dict'

# download_result = result_dict['download']      # for getting download result
# upload_result = result_dict['upload']          # for getting upload result

res = '%d' % (result)                  # changing Ping in decimal 

# download = '%d' % (download_result)  # changing download in decimal
# upload = '%d' % (upload_result)      # changing upload in decimal


while True:
# for printing download and upload results
# draw.text((17, 3), "Upload:" + upload, font=fontN, fill=255)
# draw.text(17, 6), "Download:" + download, font=fontN, fill=255)
  draw.text((17, 3), "Ping: " + res, font=fontN, fill=500)
  disp.image(image)
  disp.display()                     # printing Ping 
  time.sleep(3)                      # updating Ping result every 3 Seconds
  disp.clear()
  disp.display()




