import serial
from PIL import ImageGrab
import pytesseract
import cv2
import numpy as np
import time

COM_PORT = 'COM12'  # 根據連結的Arduino的通訊埠修改設定
BAUD_RATES = 9600
arduinoSerial = serial.Serial(COM_PORT, BAUD_RATES)
oldchoice=""
try:
    while True:
        screen=ImageGrab.grab(bbox=(860,452,1030,491)) #(螢幕左上的點為0,0，前2格為原點的XY後兩格是之後的XY)
        #screen=ImageGrab.grab(bbox=(384,466,552,495)) #(螢幕左上的點為0,0，前2格為原點的XY後兩格是之後的XY)
        #screen.save("screen.png")
        choice=pytesseract.image_to_string(screen,lang="eng")

        #if choice != oldchoice:
        print("type=|",choice[:-1] ,"|")
        if choice is ("LaTare) <0)" or "Latate) <0)" ):
            choice="kinoko"
        if choice is ("fel}" or "Ife}"):
            choice="ido"
        if choice is "Iai areyalal":
            choice="kihonn"
        if choice is "INEM":
            choice="itasikei"
        if choice is "LiF-Tel ge)":
            choice="maguro"
        if choice is "old":
            choice="yoti"
        if choice is "Ceol ge) dolby 4}":
            choice="dourokouzi"
        if choice is "alate le}"  "alate le} ":
            choice="ringo "
        if choice is "Noha e)":
            choice="yotto"
        if choice is "Le.)":
            choice="ika"
        for i in range(len(choice)-1):
            arduinoSerial.write(choice[i].encode())
        
        time.sleep(0.1)
           
        #    oldchoice=choice



except KeyboardInterrupt:
    arduinoSerial.close()    # 清除序列通訊物件
    print('關閉程式')