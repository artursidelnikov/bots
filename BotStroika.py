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


filename = 'Image.png'  # Картинка для скринов

# ///////////////////////////////////ИЩЕМ НОМЕР ОКНА ПО ЕГО ПРОЦЕССУ/////////////////////////////////////////////////////
notepads = [item for item in psutil.process_iter() if item.name() == 'GTA5.exe']
pid = next(item for item in psutil.process_iter() if item.name() == 'GTA5.exe').pid

def enum_window_callback(hwnd, pid):
    tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid == current_pid and win32gui.IsWindowVisible(hwnd):
        windows.append(hwnd)


windows = []
win32gui.EnumWindows(enum_window_callback, pid)
a = [win32gui.GetWindowText(item) for item in windows]
hwnd = win32gui.FindWindow(None, a[0])  # "RAGE Multiplayer") # НАШЛИ ОКНО
print(hwnd)

# //////////////////////////////////////////ДЛЯ СТАРТА И ОКОНЧАНИЯ РАБОТЫ////////////////////////////////////////////////
status = False


def start():
    global status
    status = True
    print("Я работаю")


def stop():
    global status
    status = False
    print("Я на паузе")

Z1 = 1093 #Зеленый
Z2 = 675

# Расположение инвентаря???????????????????????????????????????????????????????????????????
# Начало
X0_inventar = 1612  #
Y0_inventar = 200  #
# Конец
X1_inventar = 1719  #
Y1_inventar = 230  #

def set_hex(color):
    r = color & 0xFF
    g = color >> 8 & 0xFF
    b = color >> 16
    col = [r, g, b]
    return col

def background_screenshot(hwnd, X0, Y0, width, height):
    win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (width, height), dcObj, (X0, Y0), win32con.SRCCOPY)
    win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0)
    dataBitMap.SaveBitmapFile(cDC, filename)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


# //////////////////////////////////////////ОСНОВНАЯ ФУНКЦИЯ/////////////////////////////////////////////////////////////
def cod():
    global status
    while status:
        win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
        dc = win32gui.GetWindowDC(hwnd)  # используется для получения контекста устройства для указанного окна
        color3 = win32gui.GetPixel(dc, Z1, Z2)
        zvet3 = set_hex(color3)
        if zvet3[0] == 126 and zvet3[1] == 211 and zvet3[2] == 33:  # Проверяем, является ли пиксель зеленым
            print("зеленый")
            background_screenshot(hwnd, X0_inventar, Y0_inventar, X1_inventar - X0_inventar, Y1_inventar - Y0_inventar)
            img = cv2.imread('Image.png')
            pytesseract.pytesseract.tesseract_cmd = r"F:\cod\gtaРЫБАЛКА\teseract\tesseract.exe"
            Ves_inventar = pytesseract.image_to_string(img, config='--psm 11')
            print(Ves_inventar)

            if zvet[0] == 81 and zvet[1] == 67 and zvet[2] == 67:  # Проверяем, является ли пиксель зеленым
                print("f")
                win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x46, 0)  # Нажали F
                win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x46, 0)  # Отпустили F
                # time.sleep(0.1)
            if zvet1[0] == 0 and zvet1[1] == 0 and zvet1[2] == 0:  # Проверяем, является ли пиксель зеленым
                print("e")
                win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x45, 0)  # Нажали E
                win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x45, 0)  # Отпустили E
                # time.sleep(0.1)
            if zvet2[0] == 0 and zvet2[1] == 0 and zvet2[2] == 0:  # Проверяем, является ли пиксель зеленым
                print("y")
                win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x59, 0)  # Нажали Y)
                win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x59, 0)  # Отпустили

        win32gui.ReleaseDC(hwnd, dc)  # удаляем dc (чтобы не лагало)
        win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0)
        time.sleep(0.1)

# //////////////////////////////////////////ДЛЯ СТАРТА И ОКОНЧАНИЯ РАБОТЫ////////////////////////////////////////////////
keyboard.add_hotkey('F5', start)  # при нажатии на F5 Бот ловит
keyboard.add_hotkey('F7', stop)  # при нажатии на F7 Бот доловит рыбу и остановится

# //////////////////////////////////////////ДЛЯ БЕСКОНЕЧНОЙ РАБОТЫ БОТА//////////////////////////////////////////////////
while True:
    cod()