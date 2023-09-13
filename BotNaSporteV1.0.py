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


# //////////////////////////////////////////ОСНОВНАЯ ФУНКЦИЯ/////////////////////////////////////////////////////////////
def cod():
    global status
    while status:
        # //////////////////////////////////////////МЕНЯТЬ ДЛЯ СВОЕГО КОМПА//////////////////////////////////////////////
        line_length = 170  # Длина линии (количество пикселей от левой части до правой)
        line_x = 1080  # Начальная координата X линии (левая координата линии по которой ищем пиксель)
        line_y = 1130  # Координата Y линии (которая не изменяется)
        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
        green_pixel_x = 0  # Координата X найденного зеленого пикселя
        win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
        dc = win32gui.GetWindowDC(hwnd)  # используется для получения контекста устройства для указанного окна
        flag = True
        while flag and status:
            time.sleep(0.2)
            for i in range(line_length):
                pixel_x = line_x + i
                color = win32gui.GetPixel(dc, pixel_x, line_y)
                zvet = set_hex(color)
                if zvet[0] < zvet[1] and zvet[2] < zvet[1] and zvet[1] > 100:  # Проверяем, является ли пиксель зеленым
                    green_pixel_x = pixel_x
                    print("зеленый")
                    flag = False
                    break
            if green_pixel_x > 0:
                break
            time.sleep(0.01)

        flag = True
        while flag and status:  # Ждем пока пиксель (который был зеленый) станет белым
            green_pixel_x1 = green_pixel_x - 3
            for i in range(5):
                green_pixel_x1 = green_pixel_x1 + 1
                color = win32gui.GetPixel(dc, green_pixel_x1, line_y)
                zvet = set_hex(color)
                if (zvet[0] == 255 and zvet[1] == 255 and zvet[2] == 255):
                    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0X20, 0)  # Нажали пробел
                    time.sleep(0.1)
                    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0X20, 0)  # Отпустили пробел
                    time.sleep(0.1)
                    print("белый")
                    flag = False
                    break
        win32gui.ReleaseDC(hwnd, dc)  # удаляем dc (чтобы не лагало)e
        time.sleep(0.01)


# //////////////////////////////////////////ДЛЯ СТАРТА И ОКОНЧАНИЯ РАБОТЫ////////////////////////////////////////////////
keyboard.add_hotkey('F5', start)  # при нажатии на F5 Бот ловит
keyboard.add_hotkey('F7', stop)  # при нажатии на F7 Бот доловит рыбу и остановится

# //////////////////////////////////////////ДЛЯ БЕСКОНЕЧНОЙ РАБОТЫ БОТА//////////////////////////////////////////////////
while True:
    cod()
