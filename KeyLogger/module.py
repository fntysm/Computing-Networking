# with the help of a tutorial made by Tech with Tim on youtube
import pynput
# Listener is what is going to listen to a key event
from pynput.keyboard import Key, Listener

def typed(key):
    print('the {0} was clicked'.format(key))
def released(key):
    if key==Key.esc:
        return False
with Listener(on_press=typed, on_release=released) as listener:
    listener.join()