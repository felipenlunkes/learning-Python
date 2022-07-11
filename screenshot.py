#!/usr/bin/python3
#
# Created by Felipe Miguel Nery Lunkes (10/07/2022)
#
# pip install pyautogui
# apt install scrot

import pyautogui

myScreen=pyautogui.screenshot()
myScreen.save(r'./Screen.jpg')
