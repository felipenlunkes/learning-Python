#!/usr/bin/python3
#
# Created by Felipe Miguel Nery Lunkes (10/07/2022)
#
# pip install pyautogui
# apt install scrot

import pyautogui

print('PySShot v1.0 - Created by Felipe Miguel Nery Lunkes (10/07/2022)\n')
myScreen=pyautogui.screenshot()
myScreen.save(r'Screen.jpg')
