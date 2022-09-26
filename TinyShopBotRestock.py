from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
#Counter location is 691,617
#craft is 466,978
    
#buy mat is 1700,292
#buy 488,500 and 746,500 and 985,500
    #go to craft 1375,973
#craft 203,664 and 695,664 and 927,664
    #x is 1737,128

while keyboard.is_pressed('q') == True:
#click craft
        click(466, 978)
        time.sleep(0.5)
#buy mats menu

        click(1700, 292)
        time.sleep(0.5)
#buy mats
   for i in range(4): 
        click(488, 500)
         time.sleep(0.5)
   for i in range(4): 
        click(746, 500)
        time.sleep(0.5)
   for i in range(4): 
        click(985, 500)
        time.sleep(0.5)

#go to craft menu
        click(1375, 973)
        time.sleep(0.5)

#buy mats
   for i in range(4): 
    click(203, 660)
         time.sleep(0.5)
   for i in range(4): 
    click(695, 660)
         time.sleep(0.5)
   for i in range(4): 
    click(927, 660)
         time.sleep(0.5)

#click x to go back 
        click(1737, 128)
        time.sleep(1)
