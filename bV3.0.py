import cv2
import win32con
import win32api
import win32ui
import win32gui
import win32process
import psutil
import pytesseract
import time
import keyboard
from audioplayer import AudioPlayer

#Переменные

filename = 'Image.png'#Картинка для скринов

global kapcha, kapcha_x, kapcha_y,X0_inventar,Y0_inventar,X1_inventar,Y1_inventar,krasn_x,krasn_y,krasn,l_param,krasn_net,krasn_net_x,krasn_net_y,X0_rib,Y0_rib,X1_rib,Y1_rib
# Цвет капчи
kapcha = [29,38,52]

# Цвет клавиши
krasn = [255,0,0]

# Цвет клавиши не нажатой
krasn_net = [204,204,204]

#Расположение красной точки???????????????????????????????????????????????????????????????????????
krasn_x = 1053#
krasn_y = 902#

#Расположение не нажатой клавиши???????????????????????????????????????????????????????????????????????
krasn_net_x = 1070#
krasn_net_y = 902#

#Расположение капчи???????????????????????????????????????????????????????????????????????
kapcha_x = 795#1118#?????????????????????????????????????????????????????
kapcha_y = 448#639#?????????????????????????????????????????????????????

#Расположение инвентаря???????????????????????????????????????????????????????????????????
#Начало
X0_inventar = 1612 #
Y0_inventar = 200#
#Конец
X1_inventar = 1719#
Y1_inventar = 230#

#Расположение рыбы???????????????????????????????????????????????????????????????????
#Начало
X0_rib = 818#
Y0_rib = 1011#
#Конец
X1_rib = 1174#
Y1_rib = 1046#

#ПИШЕМ КООРДИНАТЫ КУДА НАЖИМАТЬ
l_param = win32api.MAKELONG(1777, 309)#?????????????????????????????????????????????????????

#+++++++++++++++++++++++++Возможно нужен поток(покачто делаем один раз+++++++++++++++
#Ищем номер окна по его процессу
notepads = [item for item in psutil.process_iter() if item.name() == 'GTA5.exe']
pid = next(item for item in psutil.process_iter() if item.name() == 'GTA5.exe').pid
def enum_window_callback(hwnd, pid):
    tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid == current_pid and win32gui.IsWindowVisible(hwnd):
        windows.append(hwnd)
windows = []
win32gui.EnumWindows(enum_window_callback, pid)
a = [win32gui.GetWindowText(item) for item in windows]
#НАХОДИМ ОКНО
hwnd = win32gui.FindWindow(None, a[0])#"RAGE Multiplayer")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#-----------------------Функции----------------------------------------------------

#СКРИН
def background_screenshot(hwnd,X0,Y0, width, height):
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0),(width, height) , dcObj, (X0,Y0), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, filename)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

# Для старта и окончания работы бота
status = False
def start():
    global status
    status = True
def stop():
    global status
    status = False

#Находим цвет пикселя (ПОКА ЧТО НЕ РАБОТАЕТ, ХОТЯ РАНЬШЕ РАБОТАЛОООООООО СУК)
def set_hex(color):
    r = color & 0xFF
    g = color >> 8 & 0xFF
    b = color >> 16
    col=[r,g,b]
    return col

# Чекаем капчу есть она лили нет и если есть вкл музыку
def kapcha_opoveshenie():
    #global status
    # Получаем пиксель с экрана
    win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
    time.sleep(0.2)
    color = win32gui.GetPixel(win32gui.GetWindowDC(hwnd),kapcha_x, kapcha_y)
    zvet = set_hex(color)
    if (kapcha[0] == zvet[0] and kapcha[1] == zvet[1] and kapcha[2] == zvet[2]):
        AudioPlayer("kapcha.mp3").play(block=True)
        kapcha_naydena()
        #status = False

# Чекаем капчу есть она лили нет и если есть вкл музыку
def kapcha_naydena():
    #global status
    # Получаем пиксель с экрана
    while True:
        win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
        color = win32gui.GetPixel(win32gui.GetWindowDC(hwnd),kapcha_x, kapcha_y)
        zvet = set_hex(color)
        if (kapcha[0] != zvet[0] and kapcha[1] != zvet[1] and kapcha[2] != zvet[2]):
            break


#--------------Основная функция бота---------------------------------------------
def cod():
    global status
    while status:
        kapcha_opoveshenie()
        time.sleep(2)
        win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0X49, 0)# Нажали I
        time.sleep(0.1)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0X49, 0)# Отпустили I
        time.sleep(1)
        background_screenshot(hwnd, X0_inventar, Y0_inventar, X1_inventar-X0_inventar, Y1_inventar-Y0_inventar)
        img = cv2.imread('Image.png')
        pytesseract.pytesseract.tesseract_cmd = r"A:\proba\teseract\tesseract.exe"
        Ves_inventar = pytesseract.image_to_string(img, config='--psm 11')
        print(Ves_inventar)
        Ves_inventar = Ves_inventar[:4]
        print(Ves_inventar)
        if (Ves_inventar[3] == "/"):
            Ves_inventar = Ves_inventar[:3]
            print(Ves_inventar)
            Ves_inventar = float(Ves_inventar)/100
            print(Ves_inventar)
        Ves_inventar = int(float(Ves_inventar) * 100)
        print(Ves_inventar)
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0X49, 0)  # Нажали I
        time.sleep(0.1)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0X49, 0)  # Отпустили I
        if Ves_inventar > 950:  #Если инвентарь полон, то стоп
            AudioPlayer("in_ful.mp3").play(block=True)
            status = False
        # Цикл начала ловли
        while Ves_inventar < 950 and status:
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0X35, 0)  # Нажали 5
            time.sleep(0.1)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0X35, 0)  # Отпустили 5
            time.sleep(4)
            kapcha_opoveshenie()
            Ves_inventar = Ves_inventar - 1
            print("Вес инвентаря: ", Ves_inventar / 100)
            time.sleep(5)
            nekras = True
            # Ждем пока станет красной первый раз
            while nekras:
                win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
                time.sleep(0.2)
                color = win32gui.GetPixel(win32gui.GetWindowDC(hwnd),krasn_x, krasn_y)
                zvet = set_hex(color)
                if (krasn[0] == zvet[0] and krasn[1] == zvet[1] and krasn[2] == zvet[2]):
                    nekras = False
            kras = True
            time.sleep(0.1)
            # Первый раз стала красной1111111111111111111111111111111111111111111111111111111
            while kras:
                win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
                time.sleep(0.1)
                color = win32gui.GetPixel(win32gui.GetWindowDC(hwnd), krasn_x, krasn_y)
                zvet = set_hex(color)
                color = win32gui.GetPixel(win32gui.GetWindowDC(hwnd), krasn_net_x, krasn_net_y)
                zvet_k = set_hex(color)
                if (krasn[0] == zvet[0] and krasn[1] == zvet[1] and krasn[2] == zvet[2]):
                    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l_param)
                    time.sleep(0.05)
                    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, l_param)
                    time.sleep(0.1)
                if (krasn_net[0] != zvet_k[0] and krasn_net[1] != zvet_k[1] and krasn_net[2] != zvet_k[2]):
                    kras = False
            time.sleep(3)
            background_screenshot(hwnd, X0_rib, Y0_rib, X1_rib - X0_rib, Y1_rib - Y0_rib )
            img = cv2.imread('Image.png')
            pytesseract.pytesseract.tesseract_cmd = r"A:\proba\teseract\tesseract.exe"
            riba = pytesseract.image_to_string(img, lang="rus", config='--psm 11')
            print("Рыба: ", riba)
            riba = riba.split(' ')[2]
            print("Рыба - : ", riba)
            if (riba[0] == "С" and riba[1] == "т"):
                # не адаптировано
                print("По буквам тоже понятно")
                Ves_inventar = Ves_inventar + 30
            if (riba[0] == "Л" and riba[1] == "о"):
                # не адаптировано
                print("По буквам тоже понятно")
                Ves_inventar = Ves_inventar + 30
            if (riba[0] == "О" and  riba[1] == "с"):
                # не адаптировано
                print("По буквам тоже понятно")
                Ves_inventar = Ves_inventar + 30
            if riba[0] == "Ч" and riba[1] == "ё":
                # не адаптировано
                print("По буквам тоже понятно")
                Ves_inventar = Ves_inventar + 40
            if (riba[0] == "С" and riba[1] == "к"):
                # не адаптировано
                print("По буквам тоже понятно")
                Ves_inventar = Ves_inventar + 40
            if (riba[0] == "М" and riba[1] == "а"):
                # не адаптировано
                print("По буквам тоже понятно")
                Ves_inventar = Ves_inventar + 40
            if (riba[0] == "Т" and riba[1] == "у"):
                # не адаптировано
                print("По буквам тоже понятно")
                Ves_inventar = Ves_inventar + 40
            if riba[0] == "Ф" and riba[1] == "у":
                # не адаптировано
                print("По буквам тоже понятно")
                Ves_inventar = Ves_inventar + 50
            print('---------------------------------------------------------------')
            time.sleep(1)
#--------------------------------------------------------------------------------


keyboard.add_hotkey('F5', start)  # при нажатии на F5 Бот ловит
keyboard.add_hotkey('F7', stop)  # при нажатии на F7 Бот доловит рыбу и остановится



















#--------Цикл бота без остановки работает-----------------------------
while True:
    cod()