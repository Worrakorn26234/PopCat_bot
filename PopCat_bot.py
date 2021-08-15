import pyautogui as pg
import time
import keyboard

##############################

##position(x=722, y=388)

def clickmouse(x=722, y=388, repeat=100,
               sleep=0.5, clicks = 10):
    t1 = time.time()
    pg.moveTo(x,y)

    for i in range(repeat):
        pg.click(clicks=clicks)
        time.sleep(sleep)

    t2 = time.time()
    print ('Time: ',t2-t1)

clickmouse()

