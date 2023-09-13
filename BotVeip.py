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


# //////////////////////////////////////////ОСНОВНАЯ ФУНКЦИЯ/////////////////////////////////////////////////////////////
def cod():
    kolvo = 0
    global status
    while status:
        win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
        dc = win32gui.GetWindowDC(hwnd)  # используется для получения контекста устройства для указанного окна
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0X35, 0)  # Нажали 5
        time.sleep(0.01)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0X35, 0)  # Отпустили 5
        time.sleep(10)
        kolvo = kolvo + 1
        print(kolvo)
        win32gui.ReleaseDC(hwnd, dc)  # удаляем dc (чтобы не лагало)


# //////////////////////////////////////////ДЛЯ СТАРТА И ОКОНЧАНИЯ РАБОТЫ////////////////////////////////////////////////
keyboard.add_hotkey('F5', start)  # при нажатии на F5 Бот ловит
keyboard.add_hotkey('F7', stop)  # при нажатии на F7 Бот доловит рыбу и остановится

# //////////////////////////////////////////ДЛЯ БЕСКОНЕЧНОЙ РАБОТЫ БОТА//////////////////////////////////////////////////
while True:
    cod()
