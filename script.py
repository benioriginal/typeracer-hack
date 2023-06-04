import cv2
import numpy as np
import pyautogui
import time
import pytesseract
import keyboard as kbd
pytesseract.pytesseract.tesseract_cmd = r'where you have tesseract.exe path'
import cv2
import numpy as np 
from pynput import mouse
screenshot = pyautogui.screenshot()
screenshot.save(f"pathtosave")
img = cv2.imread(r"thescreenshotpath aka pathtosave", 1)
click1 = False
point1 = (0,0)
def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    time.sleep(1)
    kbd.write(f"{chestie}", 0.01)
    time.sleep(10000)
    if not pressed:
        # Stop listener
        return False
def click(event,x,y,flags, params):
        global click1, point1
        if event == cv2.EVENT_LBUTTONDOWN:
                # daca apesi salvezi chestii xy bbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                click1 = True
                point1 = (x,y)
        elif event == cv2.EVENT_MOUSEMOVE and click1:
                #deseneaza aia rosie
                img_copy = img.copy()
                cv2.rectangle(img_copy, point1, (x,y), (0,0,255),2)
                cv2.imshow("Image", img_copy)
        elif event == cv2.EVENT_LBUTTONUP:
                #face poza 
                click1 = False
                sub_img = img[point1[1]:y,point1[0]:x]
                cv2.imshow("subimg", sub_img)
                cv2.imwrite('final.jpg', sub_img)
                imgggggggggg = cv2.imread('final.jpg')
                bruuhhhhhhhhhhhhhhhhhhhhh = str(pytesseract.image_to_string(imgggggggggg))
                print(bruuhhhhhhhhhhhhhhhhhhhhh)
                global chestie
                chestie = bruuhhhhhhhhhhhhhhhhhhhhh.replace('\n', ' ')
                time.sleep(2)
                print("time done")
                with mouse.Listener(
                        on_click=on_click
                        ) as listener:
                  listener.join()

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", click)
cv2.imshow("Image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()