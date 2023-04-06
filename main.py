import time
import keyboard
import playsound
import base64
import json
from threading import Thread
import os
from random import randint
BACKGROUNDMUSIC = [[3,4,4,3,4,4,3,4,4,3,4,4,3,4,3,4],
                   [5,6,6,5,6,6,5,6,6,5,6,6,5,6,5,6],
                   [7,8,8,7,8,8,7,8,8,7,8,8,7,8,7,8],
                   [9,10,10,9,10,10,9,10,10,9,10,10,9,10,9,10]]

SOUNDEFFECTS = [0, 1, 2, 1]
duration = 0.2
global queue
queue = []
RAND = False
def on_key_event(e):
    global queue
    queue.append(e.scan_code)

def play_sound(folder, index):
    playsound.playsound(os.path.join(folder, str(index)+".mp3"),False)

def background():
    i = 0
    while 1:
        for r_list in BACKGROUNDMUSIC:
            for d in r_list:
                play_sound("track",SOUNDEFFECTS[i%4])
                play_sound("track", d)
                time.sleep(duration)
                i+=1

def feedback():
    global queue
    while 1:
        if len(queue) != 0:
            if RAND:
                play_sound("main", randint(0,31)%32)
            else:
                sound = queue[0]
                play_sound("main", sound%32)
            queue = []
        time.sleep(duration)

def main():
    Thread(target=background).start()
    Thread(target=feedback).start()
    while 1:
        keyboard.on_press(on_key_event)
        time.sleep(10)


if __name__ == "__main__":
    main()


