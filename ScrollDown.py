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

while keyboard.is_pressed('q') == False:

    time.sleep(4)
    
    #click garden
    click(754, 989)
    time.sleep(0.5)

    # #click x to exit garden
    pyautogui.keyDown('Esc')  # hold down the exit key
    time.sleep(0.1)  # This pauses the script for 0.1 seconds
    pyautogui.keyUp('Esc')  # hold up the exit key

    pyautogui.keyDown('Ctrl')  # hold down the ctrl key
    pyautogui.scroll(-88)  # scroll down 100 "clicks"
    time.sleep(0.3)
    pyautogui.scroll(-88)  # scroll down 100 "clicks"
    time.sleep(0.3)
    pyautogui.scroll(-88)  # scroll down 100 "clicks"
    time.sleep(0.3)
    pyautogui.scroll(-88)  # scroll down 100 "clicks"
    time.sleep(0.3)
    pyautogui.keyUp('Ctrl')    # release the ctrl key
