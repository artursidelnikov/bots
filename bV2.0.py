# This is a sample Python script.
import pyautogui as pg
import time
import numpy as np
from mss import mss
import keyboard
#import threading
import pyautogui
import time
import numpy as np
import cv2
import os
import pyscreenshot as ImageGrab
import pytesseract
#import pywin32
import keyboard
import time



# Для старта и окончания работы бота
status = False
def start():
    global status
    status = True
def stop():
    global status
    status = False


filename = 'Image.png'
start_time = time.time()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Цвет карасной клавиши
klavisha = [0,0,255,255]
mss = mss()
#Расположение красной точки
monitor = {
    "left": 1053,
    "top": 902,
    "width": 1,
    "height": 1,
}
#для работы цикла повтора
flag1 = True

def cod():
    while status:
        pg.hotkey('i') #Открыть инвентарь
        # Делаем скрин экрана области
        screen = np.array(ImageGrab.grab(bbox=(1618, 318, 1717, 343)))#Координатыi инвентаря(2262, 383, 2357, 408)
        cv2.imwrite(filename, screen)
        #Узнаем вес нашего инвентаря
        img = cv2.imread('Image.png')
        pytesseract.pytesseract.tesseract_cmd = r"A:\proba\teseract\tesseract.exe"
        text = pytesseract.image_to_string(img, config='--psm 11')
        text = text[:4]
        print(text)
        print(status)
        vesInv = int(float(text) * 100)
        time.sleep(2)
        pg.hotkey('i')  # Закрыть инвентарь
        # Возможный цикл
        while vesInv < 950 and status:
        #for number in range(2):#Начало работы
            pg.hotkey('5')# пикаем на удочку
            vesInv = vesInv - 1
            print("Вес инвентаря: ", vesInv/100)
            time.sleep(10)
            nekras = True
            # Ждем пока станет красной0000000000000000000000000000000000000000000000000000000ii
            while nekras:
                # Получаем пиксель с экрана
                img = mss.grab(monitor)
                # Преобразуем ег в массив в матрицу
                img_arr = np.array(img)
                item = img_arr[0][0]
                if (klavisha[0] == item[0] and klavisha[1] == item[1] and klavisha[2] == item[2]):
                    nekras = False
            kras = True
            time.sleep(0.1)
            k = 400
            p = 200
            # Первый раз стала красной1111111111111111111111111111111111111111111111111111111
            while kras:
                # Получаем пиксель с экрана
                img = mss.grab(monitor)
                # Преобразуем ег в массив в матрицу
                img_arr = np.array(img)
                item = img_arr[0][0]
                if (klavisha[0] == item[0] and klavisha[1] == item[1] and klavisha[2] == item[2]):
                    # Кликаем
                    pg.click()
                    #Двигаемся
                    pg.moveTo(k,p,duration = 0.1)
                    k = k + 10
                    p = p + 10
                    continue
                if (klavisha[0] != item[0] or klavisha[1] != item[1] or klavisha[2] != item[2]):
                    kras = False
            #Следующие нажатия
            while flag1:
                #pg.click(k,p)
                k = 400
                p = 200
                # Пирс
                #time.sleep(1.9)
                # Море
                time.sleep(1.3)
                # Получаем пиксель с экрана
                img = mss.grab(monitor)
                # Преобразуем ег в массив в матрицу
                img_arr = np.array(img)
                item = img_arr[0][0]
                if (klavisha[0] == item[0] and klavisha[1] == item[1] and klavisha[2] == item[2]):
                    kras = True
                    while kras:
                        # Получаем пиксель с экрана
                        img = mss.grab(monitor)
                        # Преобразуем ег в массив в матрицу
                        img_arr = np.array(img)
                        item = img_arr[0][0]
                        if (klavisha[0] == item[0] and klavisha[1] == item[1] and klavisha[2] == item[2]):
                            # Кликаем
                            pg.click()
                            # Двигаемся
                            pg.moveTo(k, p, duration=0.1)
                            k = k + 10
                            p = p + 10
                        else:
                            kras = False
                        # if (klavisha[0] != item[0] or klavisha[1] != item[1] or klavisha[2] != item[2]):
                        #     kras = False
                else:
                    break
            # Делаем скрин экрана области
            time.sleep(0.6)
            screen = np.array(ImageGrab.grab(bbox=(834, 1017, 1061, 1039)))#Координаты выловленной рыбы
            cv2.imwrite(filename, screen)
            # Узнаем Рыбу
            img = cv2.imread('Image.png')
            pytesseract.pytesseract.tesseract_cmd = r"A:\proba\teseract\tesseract.exe"
            riba = pytesseract.image_to_string(img, config='--psm 11')
            riba = riba.split(' ')[2]
            print(riba)
            if riba[0] == "C" and riba[1] == "r":
                print(riba)
                vesInv = vesInv + 30
                print(vesInv/100)
            if riba[0] == "J" and riba[1] == "l":
                print(riba)
                vesInv = vesInv + 30
                print(vesInv/100)
            if riba[0] == "O" and  riba[1] == "c":
                print(riba)
                vesInv = vesInv + 30
                print(vesInv/100)
            # if riba == "Вы поймали: Чёрный Амур":
            #     vesInv = vesInv + 0.4
            # if riba == "Вы поймали: Скат":
            #     vesInv = vesInv + 0.4
            # if riba == "Вы поймали: Мальма":
            #     vesInv = vesInv + 0.4
            # if riba == "Вы поймали: Тунец":
            #     vesInv = vesInv + 0.4
            # if riba == "Вы поймали: Фугу":
            #     vesInv = vesInv + 0.5

# recorded_events = keyboard.record("F5")
# keyboard.send(cod())
# Press the green button in the gutter to run the script.
# keyboard.add_hotkey("F5", lambda: cod())
# keyboard.add_hotkey("F6", lambda: print("ctrl+alt+j was pressed"))
keyboard.add_hotkey('F5', start)  # при нажатии на b цикл попадает в блок if и печатает
keyboard.add_hotkey('F7', stop)  # при нажатии на e цикл попадает в блок else и ждет

while True:
    #Пауза перед началом работы
    # keyboard.add_hotkey("F6", lambda: print("ctrl+alt+j was pressed"))
    # keyboard.play(events)
    cod()

