import time
import random
import pyautogui
import math
pyautogui.click()
print (pyautogui.size())
time.sleep(3)
def circle(radius = 4.5, accuracy = 180):
    angle = 360/accuracy
    CurAngle = 0
    for i in range(accuracy):
        y = radius*math.sin(math.radians(CurAngle))
        x = radius*math.cos(math.radians(CurAngle))
        CurAngle += angle
        pyautogui.dragRel(x, y, duration=0)
try:
    for i in range(1):
        circle()
        pyautogui.moveRel(102.3, 110, duration=0)
        pyautogui.dragRel(-100, 100, duration=0)
        pyautogui.dragRel(-100, -100, duration=0)
        pyautogui.dragRel(0, -30, duration=0)
        pyautogui.dragRel(40, -40, duration=0)
        pyautogui.dragRel(20, 0, duration=0)
        pyautogui.dragRel(40, 40, duration=0)
        pyautogui.dragRel(40, -40, duration=0)
        pyautogui.dragRel(20, 0, duration=0)
        pyautogui.dragRel(40, 40, duration=0)
        pyautogui.dragRel(0, 30, duration=0)
except KeyboardInterrupt:
    print('\nDone.')