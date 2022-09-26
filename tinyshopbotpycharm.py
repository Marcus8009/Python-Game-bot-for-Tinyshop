from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(3)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def buymats(x, y):
    for i in range(5):
        click(x, y)
        time.sleep(0.3)

def craftmats(x, y):
    for i in range(10):
        click(x, y)
        time.sleep(0.3)

# Counter location is 691,617
# craft is 466,978
# buy mat is 1700,292
# buy 488,500 and 746,500 and 985,500
# go to craft 1375,973
# craft 203,664 and 695,664 and 927,664
# x is 1737,128

while keyboard.is_pressed('q') == False:

    #use buymats for clearing counter
    buymats(918, 1069)
    time.sleep(0.5)

    # click craft
    click(466, 978)
    time.sleep(0.5)
    # buy mats menu
    click(1700, 292)
    time.sleep(0.5)
    # buy mats
    buymats(488, 500)
    time.sleep(0.5)
    buymats(746, 500)
    time.sleep(0.5
    craftmats(990, 514)
    time.sleep(0.5)
    buymats(505, 860)
    time.sleep(0.5)

    # exit buy mats menu
    click(1703, 96)
    time.sleep(0.5)

    #use buymats for clearing counter
    buymats(918, 1069)
    time.sleep(0.5)

    #enter craft menu
    # click craft
    click(466, 978)
    time.sleep(0.5)

    # buy mats

    craftmats(203, 660)
    time.sleep(0.5)

    craftmats(476, 660)
    time.sleep(0.5)

    craftmats(695, 660)
    time.sleep(0.5)

    craftmats(927, 660)
    time.sleep(0.5)

    # click x to go back
    click(1703, 96)
    time.sleep(1)

    time.sleep(15)
