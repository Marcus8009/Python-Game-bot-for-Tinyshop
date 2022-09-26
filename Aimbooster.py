from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#region=(X,Y,Width,Height)
#color of centre is 255,219,195

time.sleep(3)



def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)  # This pauses the script for 0.5 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region= (679,330,600,400))
    width,height = pic.size

    for x in range(0,width,25):
        for y in range(0,height,25):

            r,g,b = pic.getpixel((x,y))

            if (b == 195 ):
                click(x+679,y+330)
                time.sleep(1)
                break



