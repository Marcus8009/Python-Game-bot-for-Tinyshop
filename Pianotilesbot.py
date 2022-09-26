from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Tile 1 Pos :X:  650 Y:  650 RGB: (159, 164, 231)
# Tile 2 Pos :X:  700 Y:  650 RGB: (155, 161, 231)
# Tile 3 Pos :X:  780 Y:  650 RGB: (154, 159, 230)
# Tile 4 Pos :X:  880 Y:  650 RGB: (253,  18,   1)



def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(650, 650)[0] == 0:
        click(650, 650)
    if pyautogui.pixel(700, 650)[0] == 0:
        click(700, 650)
    if pyautogui.pixel(770, 650)[0] == 0:
        click(770, 650)
    if pyautogui.pixel(880, 650)[0] == 0:
        click(880, 650)
