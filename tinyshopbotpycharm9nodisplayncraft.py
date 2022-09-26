from turtle import down
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#var1 = random.randint(1, 24)
var1 = random.randint(1, 3)

def main():
    
    initializePyAutoGUI()
    countdownTimer()
    while keyboard.is_pressed('q') == False:
        centerscreenzoomout()
        clearcounter()
        harvestandplant()
        waterplantsbuyseeds()
        clearcounter()
        buymarketfavourites()
        resetfov()
        #filldisplay()
        buycraftmats()
        clearcounter()
        #filldisplay()
        #craftitems()
        clearcounter()

        if (var1 % 4) == 0:
            # #adventurer goes to work
            # #click world menu
            # click(1725, 988)
            # time.sleep(0.5)

            # #collect rewards
            # click(209, 995)
            # time.sleep(0.5)
            # tenclicks(209,995)
            # time.sleep(0.5)

            # #setting correct fov for adventurer
            # #Zoom out all the way
            # win32api.SetCursorPos((1464, 207))
            # pyautogui.keyDown('Ctrl')  # hold down the ctrl key
            # pyautogui.scroll(-200)  # scroll down 100 "clicks"
            # time.sleep(0.4)
            # pyautogui.scroll(-200)  # scroll down 100 "clicks"
            # time.sleep(0.4)
            # pyautogui.scroll(-200)  # scroll down 100 "clicks"
            # time.sleep(0.4)
            # pyautogui.scroll(-200)  # scroll down 100 "clicks"
            # time.sleep(0.4)
            # pyautogui.scroll(-200)  # scroll down 100 "clicks"
            # time.sleep(0.4)
            # pyautogui.scroll(-200)  # scroll down 100 "clicks"
            # time.sleep(0.4)
            # pyautogui.scroll(-200)  # scroll down 100 "clicks"
            # time.sleep(0.4)
            # pyautogui.scroll(-200)  # scroll down 100 "clicks"
            # time.sleep(0.4)
            # pyautogui.keyUp('Ctrl')    # release the ctrl key

            # #scroll to top of adventurer map
            # win32api.SetCursorPos((1346, 226))
            # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            # time.sleep(0.3)
            # pyautogui.dragTo(1252, 963, button='left', duration=2)
            # time.sleep(0.5)
            # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            # time.sleep(0.5)
            # win32api.SetCursorPos((1346, 226))
            # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            # time.sleep(0.3)
            # pyautogui.dragTo(1252, 963, button='left', duration=2)
            # time.sleep(0.5)
            # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            # time.sleep(0.5)

            # adventurerclickanddrag()

            # #in case speed up adventure with gems menu open, click to close menus clear 1000,787
            # click(1125, 788)
            # time.sleep(0.5)
            # #go back to shop
            # click(1708, 978)
            # time.sleep(0.5)

            #click exit to phone main menu
            click(195, 16)
            time.sleep(1)

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
            time.sleep(3)

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True

def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 5):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def twoclicks(x, y):
    for i in range(2):
        click(x, y)
        time.sleep(0.1)

def fiveclicks(x, y):
    for i in range(5):
        click(x, y)
        time.sleep(0.1)

def tenclicks(x, y):
    for i in range(10):
        click(x, y)
        time.sleep(0.1)

def centerscreenzoomout():
    #click garden
    click(748, 979)
    time.sleep(0.3)

    #click esc to exit garden
    pyautogui.keyDown('Esc')  # hold down the exit key
    time.sleep(0.2)  # This pauses the script for 0.1 seconds
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
    pyautogui.scroll(-88)  # scroll down 100 "clicks"
    time.sleep(1)
    pyautogui.scroll(-88)  # scroll down 100 "clicks"
    time.sleep(0.3)
    pyautogui.keyUp('Ctrl')    # release the ctrl key

def clearcounter():
    #clear counter here
    fiveclicks(1021, 111)
    time.sleep(0.2)


def harvestandplant():
    #double click to harvest all 6 gardening spots
    twoclicks(759, 541)
    time.sleep(0.2)
    twoclicks(853, 587)
    time.sleep(0.2)
    twoclicks(853, 486)
    time.sleep(0.2)
    twoclicks(950, 529)
    time.sleep(0.2)
    twoclicks(677, 588)
    time.sleep(0.2)
    twoclicks(759, 628)
    time.sleep(0.2)
    twoclicks(618, 621)
    time.sleep(0.2)

    #click garden
    click(748, 979)
    time.sleep(0.2)

    #click seeds menu
    click(229, 712)
    time.sleep(0.2)

    #click seeds at spot 1 n drag to 1st spot
    win32api.SetCursorPos((230, 912))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(794, 525, button='left', duration=2)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #click seeds at spot 2 n drag to 2nd spot
    win32api.SetCursorPos((463, 894))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(883, 576, button='left', duration=2)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #click seeds at spot 3 n drag to 3rd spot
    win32api.SetCursorPos((669, 912))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(882, 481, button='left', duration=2)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #click seeds at spot 4 n drag to 4th spot
    win32api.SetCursorPos((902, 912))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(967, 523, button='left', duration=2)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #click seeds at spot 1 n drag to 5th spot
    win32api.SetCursorPos((230, 912))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(677, 588, button='left', duration=2)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #click seeds at spot 1 n drag to 6th spot
    win32api.SetCursorPos((463, 894))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(759, 628, button='left', duration=2)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #click seeds at spot 3 n drag to 7th spot
    win32api.SetCursorPos((669, 912))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(618, 621, button='left', duration=2)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #click seeds at spot 4 n drag to 8th spot
    win32api.SetCursorPos((902, 912))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    pyautogui.dragTo(669, 691, button='left', duration=2)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def waterplantsbuyseeds():
    #click garden menu
    click(748, 979)
    time.sleep(0.5)

    #click watering can and drag to peak of garden spots

    win32api.SetCursorPos((1629, 667))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.3)
    pyautogui.dragTo(770, 490, button='left', duration=2)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    win32api.SetCursorPos((1629, 667))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.3)
    pyautogui.dragTo(530, 601, button='left', duration=2)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    win32api.SetCursorPos((1629, 667))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.3)
    pyautogui.dragTo(691, 526, button='left', duration=2)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #click go to botanist
    click(1285, 650)
    time.sleep(0.5)

    #click to buy 4 types of flowers
    fiveclicks(1122, 535)
    time.sleep(0.3)
    fiveclicks(1360, 535)
    time.sleep(0.3)
    fiveclicks(1121, 819)
    time.sleep(0.3)
    fiveclicks(1367, 819)
    time.sleep(0.3)

    #click esc twice to exit botanist and exit city
    pyautogui.keyDown('Esc')  # hold down the exit key
    time.sleep(0.2)  # This pauses the script for 0.1 seconds
    pyautogui.keyUp('Esc')  # hold up the exit key
    time.sleep(0.5)
    pyautogui.keyDown('Esc')  # hold down the exit key
    time.sleep(0.2)  # This pauses the script for 0.1 seconds
    pyautogui.keyUp('Esc')  # hold up the exit key

def buymarketfavourites():
    
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

def resetfov():
    
    #get lost to find yourself, below is to fix any issues with fov getting lost after faulty click drags. 
    #need to force a recenter of screen onto garden plots, can only be done if garden plot is way out of field of view. 

    #going out of fov
    win32api.SetCursorPos((1346, 226))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.3)
    pyautogui.dragTo(1252, 963, button='left', duration=2)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.5)
    win32api.SetCursorPos((1346, 226))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.3)
    pyautogui.dragTo(1252, 963, button='left', duration=2)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.5)

    #forcing reset of fov by entering and exiting garden menu
    #click garden
    click(748, 979)
    time.sleep(0.3)

    #click esc to exit garden
    pyautogui.keyDown('Esc')  # hold down the exit key
    time.sleep(0.2)  # This pauses the script for 0.1 seconds
    pyautogui.keyUp('Esc')  # hold up the exit key


def filldisplay():

    #click storage
    click(188, 968)
    time.sleep(0.5)

    #storage to display
    #storage 1
    win32api.SetCursorPos((212, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(593, 181, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 2
    win32api.SetCursorPos((464, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(719, 221, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 3
    win32api.SetCursorPos((714, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(799, 259, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 4
    win32api.SetCursorPos((964, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(864, 316, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 5
    win32api.SetCursorPos((1214, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(953, 363, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 6
    win32api.SetCursorPos((1464, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(1026, 420, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 7
    win32api.SetCursorPos((1714, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(1139, 448, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(1)

    #storage 8
    win32api.SetCursorPos((212, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(679, 136, button='left', duration=2.5)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    # #storage 9
    # win32api.SetCursorPos((464, 855))
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # time.sleep(1)
    # pyautogui.dragTo(812, 167, button='left', duration=2)
    # time.sleep(0.2)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    # #storage 10
    # win32api.SetCursorPos((714, 855))
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # time.sleep(1)
    # pyautogui.dragTo(892, 207, button='left', duration=2.5)
    # time.sleep(0.2)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 11
    win32api.SetCursorPos((964, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(961, 267, button='left', duration=2.5)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 12
    win32api.SetCursorPos((1214, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(1046, 311, button='left', duration=2.5)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 13
    win32api.SetCursorPos((1464, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(1139, 355, button='left', duration=2.5)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #storage 14
    win32api.SetCursorPos((1714, 855))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(1212, 399, button='left', duration=2.5)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(1)

    # click anywhere to go back
    click(1703, 96)
    time.sleep(1)

def buycraftmats():
     # click craft
    click(466, 978)
    time.sleep(0.5)
    # enter buy mats menu
    click(1700, 292)
    time.sleep(0.5)
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

def craftclicking():
    tenclicks(306, 667)
    time.sleep(0.2)

    tenclicks(476, 660)
    time.sleep(0.2)

    tenclicks(690, 660)
    time.sleep(0.2)

    tenclicks(950, 660)
    time.sleep(0.2)

    tenclicks(1200, 660)
    time.sleep(0.2)

    tenclicks(1450, 660)
    time.sleep(0.2)

    tenclicks(1700, 660)
    time.sleep(0.2)
def craftitems():
    #enter craft menu
    # click craft
    click(466, 978)
    time.sleep(0.5)
    # click  consumables
    click(707, 335)
    time.sleep(0.3)
    craftclicking()
    # click  gear
    click(856, 335)
    time.sleep(0.3)
    craftclicking()
    # click x to exit craft menu
    click(1698, 95)
    time.sleep(1.3)

def adventurerclickanddrag():
    #click and drag adventurer to many spots(go on adventure by luck)
    win32api.SetCursorPos((225, 981))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(643, 768, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


    win32api.SetCursorPos((225, 981))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(1036, 677, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    win32api.SetCursorPos((225, 981))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(1058, 872, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


    win32api.SetCursorPos((225, 981))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(1053, 274, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


    win32api.SetCursorPos((225, 981))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(1354, 625, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


    win32api.SetCursorPos((225, 981))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(1046, 867, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    win32api.SetCursorPos((225, 981))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    pyautogui.dragTo(1425, 615, button='left', duration=2)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

if __name__ == "__main__":
    main()