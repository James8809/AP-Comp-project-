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


def screencap():
    # cnt = 0
    # start = time.perf_counter()
    # while(time.perf_counter() - start < 1):
    weak = np.array([10, 0, 190])
    strong = np.array([50, 30, 250])
    while(True):
        img = ImageGrab.grab(bbox=(x_1, y_1, x_2, y_2)) #bbox specifies specific region (bbox= x,y,width,height)
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        # weak = np.array([190, 130, 70])
        # strong = np.array([220, 160, 90])
        mask = cv2.inRange(frame, weak, strong)


        cv2.imshow("1", frame)
        cv2.imshow("2", mask)
        # normtest = test[::-1]
        max = np.argmax(mask)
        # get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
        # print(max)
        idx = np.where(mask == max)
        print(idx)
        # tse = test[max]
        # print(tse)
        # cnt+=1
        cv2.waitKey(1)
    # print(cnt)
cap = screencap()
cap.destroyAllWindows()