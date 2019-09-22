import keyboard

events = keyboard.record(until="esc")     # recording keyboard until escape is pressed

print(events)                             # printing it
