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

# Переменные(менять)
ovoshiX = 1477
ovoshiY = 465
vodaX = 1395
vodaY = 473
venchikX = 1123
venchikY = 759
gotovkaX = 1127
gotovkaY = 859
OGONX = 930
OGONY = 610
sterx = 1174
stery = 318

ovoshi = win32api.MAKELONG(ovoshiX, ovoshiY)
voda = win32api.MAKELONG(vodaX, vodaY)
venchik = win32api.MAKELONG(venchikX, venchikY)
gotovka = win32api.MAKELONG(gotovkaX, gotovkaY)
ster = win32api.MAKELONG(sterx, stery)
OGON = win32api.MAKELONG(OGONX, OGONY)

# Ищем номер окна по его процессу
notepads = [item for item in psutil.process_iter() if item.name() == 'GTA5.exe']
pid = next(item for item in psutil.process_iter() if item.name() == 'GTA5.exe').pid


def enum_window_callback(hwnd, pid):
    tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid == current_pid and win32gui.IsWindowVisible(hwnd):
        windows.append(hwnd)


windows = []
win32gui.EnumWindows(enum_window_callback, pid)
a = [win32gui.GetWindowText(item) for item in windows]
# НАХОДИМ ОКНО
hwnd = win32gui.FindWindow(None, a[0])  # "RAGE Multiplayer")
print(hwnd)
status = False


def start():
    global status
    status = True
    print("Я работаю")


def stop():
    global status
    status = False
    print("Отдыхаю")


# //////////////////////////////////////////ОСНОВНАЯ ФУНКЦИЯ/////////////////////////////////////////////////////////////
def cod():
    global status
    while status:
        win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
        dc = win32gui.GetWindowDC(hwnd)  # используется для получения контекста устройства для указанного окн
        # Смузиииии
        # Нажатие на овощи
        time.sleep(1)
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, ovoshi)
        time.sleep(0.1)
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONUP, None, ovoshi)
        # Нажатие на воду
        time.sleep(1)
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, voda)
        time.sleep(0.1)
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONUP, None, voda)
        # Нажатие на венчик
        time.sleep(1)
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, venchik)
        time.sleep(0.1)
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONUP, None, venchik)
        # Нажатие на Enter
        time.sleep(1)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, gotovka)
        time.sleep(0.1)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, gotovka)  # Отпустили enter
        win32gui.ReleaseDC(hwnd, dc)  # удаляем dc (чтобы не лагало)
        time.sleep(6)

    '''        #       # Стерлядь
        time.sleep(1)
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, ster)
        time.sleep(0.1)
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONUP, None, ster)
        # Нажатие на венчик
        time.sleep(1)
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, OGON)
        time.sleep(0.1)
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONUP, None, OGON)
        # Нажатие на Enter
        time.sleep(1)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, gotovka)
        time.sleep(0.1)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, gotovka)  # Отпустили enter
        win32gui.ReleaseDC(hwnd, dc)  # удаляем dc (чтобы не лагало)
        # win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0)
        time.sleep(6)
'''


#

# //////////////////////////////////////////ДЛЯ СТАРТА И ОКОНЧАНИЯ РАБОТЫ////////////////////////////////////////////////
keyboard.add_hotkey('F5', start)  # при нажатии на F5 Бот ловит
keyboard.add_hotkey('F7', stop)  # при нажатии на F7 Бот доловит рыбу и остановится

# //////////////////////////////////////////ДЛЯ БЕСКОНЕЧНОЙ РАБОТЫ БОТА//////////////////////////////////////////////////
while True:
    cod()
