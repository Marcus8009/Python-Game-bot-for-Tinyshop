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
    for i in range(100000000):
        click(x, y)
        time.sleep(0.3)

# Counter location is 691,617
# craft is 466,978
# buy mat is 1700,292
# buy 488,500 and 746,500 and 985,500
# go to craft 1375,973
# craft 203,664 and 695,664 and 927,664
# x is 1737,128
#storage 1st item 212,855 next add 250 to 212



while keyboard.is_pressed('q') == False:

    #use buymats for clearing counter
    craftmats(966, 150)
    time.sleep(0.5)

    