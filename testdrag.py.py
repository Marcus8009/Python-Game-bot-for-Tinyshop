from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(3)

while keyboard.is_pressed('q') == False:


    win32api.SetCursorPos((464, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(510, 385, button='left', duration=1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    # #storage to display
    # #storage 1
    # pyautogui.moveTo(212, 855)
    # pyautogui.mouseDown(button='left')
    # pyautogui.moveTo(510, 385, 1)
    # time.sleep(10)
    # time.sleep(0.5)

