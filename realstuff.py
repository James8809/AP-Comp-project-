import numpy as np
import cv2
from PIL import ImageGrab
from PIL import Image
import pyautogui
import time

x_res = 1920
y_res = 1080
box_width = 300
box_height = 300
x_1 = int((x_res - box_width) / 2)
y_1 = int((y_res - box_height) / 2) - 70
x_2 = x_1 + box_width
y_2 = y_1 + box_height



weak = np.array([10, 0, 190])
strong = np.array([50, 30, 250])
while(True):
    img = ImageGrab.grab(bbox=(x_1, y_1, x_2, y_2)) #bbox specifies specific region (bbox= x,y,width,height)
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    mask = cv2.inRange(frame, weak, strong)
    cv2.imshow("1", frame)
    cv2.imshow("2", mask)
    cv2.waitKey(1)
capp = screencap()
capp.destroyAllWindows()

points = cv2.findNonZero(mask)
print(points)
avg = np.mean(points, axis=0)
# assuming the resolutions of the image and screen are the following
resImage = [300, 300]
resScreen = [1920, 1080]
# points are in x,y coordinates
pointInScreen = ((resScreen[0] / resImage[0]) * avg[0], (resScreen[1] / resImage[1]) * avg[1] )