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
#storage 1st item 212,855 next add 250 to 212

var1 = random.randint(1, 24)
#var1 = 3

while keyboard.is_pressed('q') == False:

    #use buymats for clearing counter
    buymats(1209, 219)
    time.sleep(0.5)

    #click market
    click(314, 916)
    time.sleep(0.5)

    #click market favourites
    click(1599, 933)
    time.sleep(0.5)
    #confirm buy market favourites
    click(772, 738)
    time.sleep(0.5)
    #click x to exit market
    click(1740, 63)
    time.sleep(0.5)

    #click storage
    click(188, 968)
    time.sleep(0.5)

    #storage to display
    #storage 1
    win32api.SetCursorPos((212, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(463, 350, button='left', duration=1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 2
    win32api.SetCursorPos((464, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(617, 256, button='left', duration=1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 3
    win32api.SetCursorPos((714, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(685, 416, button='left', duration=1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 4
    win32api.SetCursorPos((212, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(825, 502, button='left', duration=1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 5
    win32api.SetCursorPos((464, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.8)
    pyautogui.dragTo(1114, 514, button='left', duration=1.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 6
    win32api.SetCursorPos((714, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.8)
    pyautogui.dragTo(969, 594, button='left', duration=1.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(2)

    # click x to go back
    click(1703, 96)
    time.sleep(1)


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
    time.sleep(0.5)
    buymats(1011, 500)
    time.sleep(0.5)


    buymats(505, 860)
    time.sleep(0.5)
    buymats(769, 860)
    time.sleep(0.5)
    craftmats(1012, 867)
    time.sleep(0.5)



    # click x to exit buy mats menu
    click(1742, 65)
    time.sleep(0.5)

    #use buymats for clearing counter
    buymats(1209, 219)
    time.sleep(0.5)

    #click storage
    click(188, 968)
    time.sleep(0.5)

    #storage to display
    #storage 1
    win32api.SetCursorPos((212, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(463, 350, button='left', duration=1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 2
    win32api.SetCursorPos((464, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(617, 256, button='left', duration=1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 3
    win32api.SetCursorPos((714, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(685, 416, button='left', duration=1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 4
    win32api.SetCursorPos((212, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(825, 502, button='left', duration=1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 5
    win32api.SetCursorPos((464, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.8)
    pyautogui.dragTo(1114, 514, button='left', duration=1.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 6
    win32api.SetCursorPos((714, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.8)
    pyautogui.dragTo(969, 594, button='left', duration=1.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(2)

    # click x to go back
    click(1703, 96)
    time.sleep(1)

    #enter craft menu
    # click craft
    click(466, 978)
    time.sleep(0.5)

    # click  price desc craft
    click(1009, 441)
    time.sleep(0.5)


    #craft mats

    craftmats(203, 660)
    time.sleep(0.5)

    craftmats(476, 660)
    time.sleep(0.5)

    craftmats(690, 660)
    time.sleep(0.5)

    craftmats(950, 660)
    time.sleep(0.5)

    craftmats(1200, 660)
    time.sleep(0.5)

    craftmats(1450, 660)
    time.sleep(0.5)

    craftmats(1700, 660)
    time.sleep(0.5)


    # click x to exit craft menu
    click(1698, 95)
    time.sleep(1)

    time.sleep(3)



    if (var1 % 4) == 0:
        #click exit to phone main menu
        click(195, 16)
        time.sleep(0.5)

        #confirm exit to phone main menu
        click(1067, 661)
        time.sleep(3)

       #click tinyshop to enter game
        click(1642, 216)
        time.sleep(0.5)

       #Wait 90 secs for tinyshop to load.
        time.sleep(90)

        #Wait click to clear notification when tinyshop has loaded.
        click(1347, 199)
        time.sleep(0.5)

    else:
        time.sleep(10)
