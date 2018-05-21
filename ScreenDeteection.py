
import time
from PIL import ImageGrab
from PIL import Image
from os import environ
while True:
    time.sleep(0.5)
    t = str(time.time()).replace('.','-')
    tt = time.time()
    img=ImageGrab.grab()
    img = img.resize((800,600))
    img.save(''.join(['img\\',t,'.png']))
    print (time.time() - tt)