import pyautogui

time.sleep(2)


iml = pyautogui.screenshot(region=(679,330,600,400))
iml.save(r"C:\Users\Admin\PycharmProjects\pythonProject3\savedimage.png")
