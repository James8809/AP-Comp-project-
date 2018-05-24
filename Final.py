import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui
from pynput import keyboard

from pynput.mouse import Listener
from scipy import stats
from PIL import Image
import time


# x_res = 1920
# y_res = 1080
# box_width = 300
# box_height = 300

strx_res = input("type your monitor's width resolution")
stry_res = input("type your monitor's height resolution")
strbox_width = input("your box's width: ")
strbox_height = input("your box's height: ")

if ValueError :
    print("please input NUMBERS")
    exit()

x_res = int(strx_res)
y_res = int(stry_res)
box_width = int(strbox_width)
box_height = int(strbox_height)


x_1 = int((x_res - box_width) / 2)
y_1 = int((y_res - box_height) / 2) - 70
x_2 = x_1 + box_width
y_2 = y_1 + box_height
# print(x_1, y_1, x_2, y_2)
weak = np.array([50, 29, 143])
strong = np.array([130, 69, 203])


while(True):
    img = ImageGrab.grab(bbox=(x_1, y_1, x_2, y_2)) #bbox specifies specific region (bbox= x,y,width,height)
    img_np = np.array(img)
    norm = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    detect = cv2.inRange(norm, weak, strong)
    # bitand = cv2.bitwise_and(img_np, img_np, mask = detect)
    # cv2.imshow("1", norm)
    # cv2.imshow("2", detect)
    # cv2.imshow("bit", bitand)
    cv2.waitKey(1)

    points = cv2.findNonZero(detect)

    if points is not None:
        print(points)
        avg = np.mean(points, axis=1)
        cal = np.mean(avg, axis=0)
        pointInScreen = (x_1 + cal[0], y_1 + cal[1])
        # print(cal)
        #improvement - if leftmouseclick then access the moveTo
        #it will lower the frame rate cuz one less line
        pyautogui.moveTo(pointInScreen)
    # if (keyboard.is_pressed ('m')):
    #     print("pause")
    #             break

cap = screencap()
cap.destroyAllWindows()
