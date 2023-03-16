# Size(width=1920, height=1080)
# import random
import pyautogui
import time


def current_position(width):
    _x, _y = pyautogui.position()
    if _x == width:
        return _x - 1, _y
    else:
        return _x + 1, _y


def mouse_mover(width):
    try:
        while True:
            _x, _y = current_position(width)
            pyautogui.moveTo(_x, _y, duration=1)
            print({pyautogui.position()})
            # change this to 120 seconds
            time.sleep(120)
    except:
        print("Stopping Due to Interruption")


if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    width, height = pyautogui.size()
    mouse_mover(width - 1)