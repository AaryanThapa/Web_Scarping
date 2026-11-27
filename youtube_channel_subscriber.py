import pyautogui
import time
import webbrowser

channel_name = pyautogui.prompt(text="", title="Enter the channel name")
print(channel_name)

webbrowser.open("https://www.youtube.com/")
time.sleep(5)

x, y = pyautogui.locateCenterOnScreen("search.png", confidence=0.9)
pyautogui.moveTo(x, y, 1)
pyautogui.click()
time.sleep(1)

pyautogui.write(channel_name)
pyautogui.press("enter")

time.sleep(4)
# x, y = pyautogui.locateCenterOnScreen("channel_img.png", confidence=0.6)
# pyautogui.moveTo(x, y, 1)
# pyautogui.click()
# time.sleep(1)

x, y = pyautogui.locateCenterOnScreen("subscribe_but.png", confidence=0.9)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

