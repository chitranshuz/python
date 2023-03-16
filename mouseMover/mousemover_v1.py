# Size(width=1920, height=1080)

import pyautogui
import random
import time


def mouse_mover(width, height):
    try:
        while True:
            pyautogui.moveTo(random.randint(0, width), random.randint(0, height), duration=1)
            print({pyautogui.position()})
            # change this to 120 seconds
            time.sleep(10)
    except:
        print("Stopping Due to Interruption")


if __name__ == '__main__':
    pyautogui.FAILSAFE == True
    width, height = pyautogui.size()
    mouse_mover(width, height)
