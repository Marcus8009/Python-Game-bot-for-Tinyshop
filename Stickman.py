from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('stickman.png',confidence=0.8) !=None:
        print("i can see it")
        time.sleep(0.5)
    else:
        print("i cannot see it")
        time.sleep(0.5)

