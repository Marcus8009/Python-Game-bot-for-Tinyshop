from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#region=(X,Y,Width,Height)

while 1:
    if pyautogui.locateOnScreen('stickman.png',region= (150,175,350,600),grayscale=True,confidence=0.8) !=None:
        print("i can see it")
        time.sleep(0.5)
    else:
        print("i cannot see it")
        time.sleep(0.5)

