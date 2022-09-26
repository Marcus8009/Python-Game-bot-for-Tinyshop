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

def getcentralpos():
    
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_CTRLDOWN, 0, 0)
    time.sleep(3)  # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_CTRLDOWN, 0, 0)


    win32api.mouse_event(win32con.MOUSEEVENTF_CTRLUP, 0, 0)


def twoclicks(x, y):
    for i in range(2):
        click(x, y)
        time.sleep(0.3)

def fiveclicks(x, y):
    for i in range(5):
        click(x, y)
        time.sleep(0.3)

def fiveclicks(x, y):
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

while keyboard.is_pressed('q') == False:

    #click garden
    click(748, 979)
    time.sleep(0.2)

    #click esc to exit garden
    pyautogui.keyDown('Esc')  # hold down the exit key
    time.sleep(0.1)  # This pauses the script for 0.1 seconds
    pyautogui.keyUp('Esc')  # hold up the exit key

    #Zoom out all the way
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

    #double click all 4 gardening spots
    twoclicks(759, 541)
    time.sleep(0.1)
    twoclicks(853, 587)
    time.sleep(0.1)
    twoclicks(853, 486)
    time.sleep(0.1)
    twoclicks(950, 529)
    time.sleep(0.1)

    #click garden
    click(748, 979)
    time.sleep(0.2)

    #click seeds menu
    click(229, 712)
    time.sleep(0.2)

    #click seeds at spot 1 n drag to 1st spot
    win32api.SetCursorPos((230, 912))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    pyautogui.dragTo(759, 541, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #click seeds at spot 1 n drag to 2nd spot
    win32api.SetCursorPos((230, 912))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    pyautogui.dragTo(853, 587, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #click seeds at spot 1 n drag to 3rd spot
    win32api.SetCursorPos((230, 912))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    pyautogui.dragTo(853, 486, button='left', duration=2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #click seeds at spot 1 n drag to 4th spot
    win32api.SetCursorPos((230, 912))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    pyautogui.dragTo(950, 529, button='left', duration=2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #clear counter here
    fiveclicks(940, 173)
    time.sleep(0.2)

    #click garden
    click(748, 979)
    time.sleep(0.2)

    #click watering can and drag to all 4 garden spots
    win32api.SetCursorPos((1629, 667))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    pyautogui.dragTo(759, 541, button='left', duration=2)
    time.sleep(0.2)
    pyautogui.dragTo(853, 587, button='left', duration=1)
    time.sleep(0.2)
    pyautogui.dragTo(853, 486, button='left', duration=1)
    time.sleep(0.2)
    pyautogui.dragTo(950, 529, button='left', duration=1)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #click esc to exit garden
    pyautogui.keyDown('Esc')  # hold down the exit key
    time.sleep(0.1)  # This pauses the script for 0.1 seconds
    pyautogui.keyUp('Esc')  # hold up the exit key

    #clear counter here
    fiveclicks(940, 173)
    time.sleep(0.2)

    #click market
    click(314, 916)
    time.sleep(0.2)
    #click market favourites
    click(1599, 933)
    time.sleep(0.2)
    #confirm buy market favourites
    click(772, 738)
    time.sleep(0.2)
    #click x to exit market
    click(1740, 63)
    time.sleep(0.2)

    #click storage
    click(188, 968)
    time.sleep(0.3)

    #storage to display
    #storage 1
    win32api.SetCursorPos((212, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(591, 212, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 2
    win32api.SetCursorPos((464, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(700, 240, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 3
    win32api.SetCursorPos((714, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(786, 281, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 4
    win32api.SetCursorPos((964, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(846, 328, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 5
    win32api.SetCursorPos((1214, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.8)
    pyautogui.dragTo(940, 383, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 6
    win32api.SetCursorPos((1464, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.8)
    pyautogui.dragTo(1027, 426, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(2)

    #storage 7
    win32api.SetCursorPos((1714, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.8)
    pyautogui.dragTo(1118, 479, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(2)

    # click anywhere to go back
    click(1703, 96)
    time.sleep(1)

    # click craft
    click(466, 978)
    time.sleep(0.3)
    # enter buy mats menu
    click(1700, 292)
    time.sleep(0.3)



    # buy mats
    fiveclicks(488, 500)
    time.sleep(0.3)
    fiveclicks(746, 500)
    time.sleep(0.3)
    fiveclicks(1011, 500)
    time.sleep(0.3)


    fiveclicks(505, 860)
    time.sleep(0.3)
    fiveclicks(769, 860)
    time.sleep(0.3)
    fiveclicks(1012, 867)
    time.sleep(0.3)



    # click x to exit buy mats menu
    click(1742, 65)
    time.sleep(0.3)

    #clear counter here
    fiveclicks(940, 173)
    time.sleep(0.2)

    #click storage
    click(188, 968)
    time.sleep(0.3)

    #storage to display
    #storage 1
    win32api.SetCursorPos((212, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(591, 212, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 2
    win32api.SetCursorPos((464, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(700, 240, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 3
    win32api.SetCursorPos((714, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(786, 281, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 4
    win32api.SetCursorPos((964, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(846, 328, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 5
    win32api.SetCursorPos((1214, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.8)
    pyautogui.dragTo(940, 383, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 6
    win32api.SetCursorPos((1464, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.8)
    pyautogui.dragTo(1027, 426, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(2)

    #storage 7
    win32api.SetCursorPos((1714, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.8)
    pyautogui.dragTo(1118, 479, button='left', duration=1.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(2)

    # click anywhere to go back
    click(1703, 96)
    time.sleep(1)

    #enter craft menu
    # click craft
    click(466, 978)
    time.sleep(0.2)

    # click  price desc craft cycle 1
    click(707, 335)
    time.sleep(0.2)


    #craft mats cycle 1

    fiveclicks(203, 660)
    time.sleep(0.2)

    fiveclicks(476, 660)
    time.sleep(0.2)

    fiveclicks(690, 660)
    time.sleep(0.2)

    fiveclicks(950, 660)
    time.sleep(0.2)

    fiveclicks(1200, 660)
    time.sleep(0.2)

    fiveclicks(1450, 660)
    time.sleep(0.2)

    fiveclicks(1700, 660)
    time.sleep(0.2)

    # click  price desc craft cycle 2
    click(856, 335)
    time.sleep(0.2)


    #craft mats cycle 2

    fiveclicks(203, 660)
    time.sleep(0.2)

    fiveclicks(476, 660)
    time.sleep(0.2)

    fiveclicks(690, 660)
    time.sleep(0.2)

    fiveclicks(950, 660)
    time.sleep(0.2)

    fiveclicks(1200, 660)
    time.sleep(0.2)

    fiveclicks(1450, 660)
    time.sleep(0.2)

    fiveclicks(1700, 660)
    time.sleep(0.2)


    # click x to exit craft menu
    click(1698, 95)
    time.sleep(0.3)

    time.sleep(1)



    # if (var1 % 4) == 0:
    #     #click exit to phone main menu
    #     click(195, 16)
    #     time.sleep(0.5)

    #     #confirm exit to phone main menu
    #     click(1067, 661)
    #     time.sleep(3)

    #    #click tinyshop to enter game
    #     click(1642, 216)
    #     time.sleep(0.5)

    #    #Wait 90 secs for tinyshop to load.
    #     time.sleep(90)

    #     #Wait click to clear notification when tinyshop has loaded.
    #     click(1347, 199)
    #     time.sleep(0.5)

    # else:
    #     time.sleep(10)
