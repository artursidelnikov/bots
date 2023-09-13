import win32con
import win32api
import win32gui
import win32process
import psutil
import time
import keyboard

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


# //////////////////////////////////////////ДЛЯ ПЕРЕВОДА ЦВЕТА В RGB/////////////////////////////////////////////////////
def set_hex(color):
    r = color & 0xFF
    g = color >> 8 & 0xFF
    b = color >> 16
    col = [r, g, b]
    return col


# ////////////////////////////////////ПЕРЕМЕННЫЕ МЕНЯТЬ ДЛЯ СВОЕГО ЭКРАНА/////////////////////////////////////////////////
lzelx = 1267  # КООРДИНАТА X (ЛЕВЕЕ ОТ КРАСНОЙ ПАЛКИ НА 10 ПИКСЕЛЕЙ)
lzely = 684  # КООРДИНАТА Y


# //////////////////////////////////////////ОСНОВНАЯ ФУНКЦИЯ/////////////////////////////////////////////////////////////
def cod():
    global status
    while status:
        win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
        dc = win32gui.GetWindowDC(hwnd)  # используется для получения контекста устройства для указанного окна
        color = win32gui.GetPixel(dc, lzelx, lzely)
        zvet = set_hex(color)
        if zvet[0] == 126 and zvet[1] == 211 and zvet[2] == 33:  # Проверяем, является ли пиксель зеленым
            print("зеленый")
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x45, 0)  # Нажали E
            time.sleep(0.1)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x45, 0)  # Отпустили E
            # time.sleep(0.1)
        win32gui.ReleaseDC(hwnd, dc)  # удаляем dc (чтобы не лагало)
        win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0)
        time.sleep(0.01)


# //////////////////////////////////////////ДЛЯ СТАРТА И ОКОНЧАНИЯ РАБОТЫ////////////////////////////////////////////////
keyboard.add_hotkey('F5', start)  # при нажатии на F5 Бот ловит
keyboard.add_hotkey('F7', stop)  # при нажатии на F7 Бот доловит рыбу и остановится

# //////////////////////////////////////////ДЛЯ БЕСКОНЕЧНОЙ РАБОТЫ БОТА//////////////////////////////////////////////////
while True:
    cod()
