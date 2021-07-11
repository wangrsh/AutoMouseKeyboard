import pyautogui
import time
import os

wh = pyautogui.size()

print(wh)

# 调取鼠标工具
# pyautogui.mouseInfo()

for i in range(100):
    pyautogui.moveTo(100, 100, duration=0.5)
    pyautogui.moveTo(100, 800, duration=0.5)

# while True:
#     p = pyautogui.position()
#     print(p)
#     time.sleep(0.2)

# b = pyautogui.locateOnScreen('111.png')
# print(b)

# app_dir = r'D:\Program Files (x86)\Well Logging DAU App Beta\logging_app.exe'
# os.startfile(app_dir)
# time.sleep(2)
#
# fw = pyautogui.getActiveWindow()
# print(fw.title)
#
# fw = pyautogui.getAllTitles()
# for item in fw:
#     if '井场一体化' in item:
#         print(item)
#         break
# fw1 = pyautogui.getWindowsWithTitle(item)[0]
# print('NEW' + fw1.title)
#
# time.sleep(2)
# fw1.maximize()
#
# pyautogui.moveTo(1362, 699, duration=0.5)
# pyautogui.click(1362, 699)
# pyautogui.write("yangy_cj")
# pyautogui.click(1362, 733)
# pyautogui.write("123")
# pyautogui.click(1339, 789)