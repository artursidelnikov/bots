import tkinter as tk
import subprocess
import win32gui
import win32process
import psutil
import cv2
import win32con
import win32api
import win32ui
import win32gui
import win32process
import psutil
import pytesseract
import time
import sqlite3
from audioplayer import AudioPlayer
import threading

#   ЧТО НУЖНО ДЕЛАТЬ ПРИ КАЖДОМ ЗАПУСКЕ+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++
#   Ищем номер окна по его процессу
notepads = [item for item in psutil.process_iter() if item.name() == 'GTA5.exe']
pid = next(item for item in psutil.process_iter() if item.name() == 'GTA5.exe').pid


def enum_window_callback(hwnd, pid):
    tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid == current_pid and win32gui.IsWindowVisible(hwnd):
        windows.append(hwnd)


windows = []
win32gui.EnumWindows(enum_window_callback, pid)
a = [win32gui.GetWindowText(item) for item in windows]
#   НАХОДИМ ОКНО
hwnd = win32gui.FindWindow(None, a[0])  # "RAGE Multiplayer") ОКНО К КОТОРОМУ ВСЕГДА ИДЕТ ОБРАЩЕНИЕ
#   КОНЕЦ+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#   ФЛАГИ ДЛЯ ЗАПУСКА ДРУГИХ ФАЙЛОВ
global ribalka_flag, kachalka_flag, stroika_flag, port_flag, kamenolomnya_flag, smuzy_flag, sterlyad_flag
ribalka_flag = False
kachalka_flag = False
stroika_flag = False
port_flag = False
kamenolomnya_flag = False
smuzy_flag = False
sterlyad_flag = False

# <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><
#   //////////ПЕРЕМЕННЫЕ/////////////////////////////////////////////////////////////////
#   Картинка для скринов
filename = 'Image.png'
#   Цвет капчи
kapcha = [29, 38, 52]
#   Цвет серый правой кнопки
krasn_net = [204, 204, 204]
#   Цвет красной левой кнопки
krasn = [255, 0, 0]

#   //////////КООРДИНАТЫ ВСЕ/////////////////////////////////////////////////////////////////
# Расположение инвентаря
# Начало
X0_inventar = 1612  #
Y0_inventar = 200  #
# Конец
X1_inventar = 1719  #
Y1_inventar = 230  #

# Расположение капчи
kapcha_x = 795  # 1118#?????????????????????????????????????????????????????
kapcha_y = 448  #

# Расположение левой красной кнопки
krasn_x = 1053  #
krasn_y = 902

# Расположение правой серой кнопки
krasn_net_x = 1070  #
krasn_net_y = 902
# ПИШЕМ КООРДИНАТЫ КУДА НАЖИМАТЬ
l_param = win32api.MAKELONG(1777, 309)

# Расположение рыбы
# Начало
X0_rib = 818  #
Y0_rib = 1011  #
# Конец
X1_rib = 1174  #
Y1_rib = 1046


#   ФУНКЦИЯ ВЫВОДА ДАННЫХ ИЗ БД
def vivod_dannih():
    conn = sqlite3.connect('statistika.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM riby")
    rows = cursor.fetchall()
    # Вывод данных с форматированием
    point = 0
    for row in rows:
        riba = row[1]
        kolvo = row[2]
        stoimost = row[3]
        vsego = kolvo * (stoimost - 35)
        text_fields[point].delete("1.0", tk.END)
        text_fields[point].insert(tk.END, vsego)
        point = point + 1
        text_box.insert(tk.END, f"{riba}: kolvo - {kolvo}; stoimost - {stoimost} \n")
        text_box.see(tk.END)
    conn.close()


#   ФУНКЦИЯ ГДЕ ДОБОВЛЯЕТСЯ КОЛ-ВО РЫБЫ ПРИ ПОИМКЕ
def increase_fish_count(fish_name):
    # Подключение к базе данных
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Поиск рыбы в таблице riby
    cursor.execute("SELECT kolvo FROM riby WHERE riba = ?", (fish_name,))
    result = cursor.fetchone()
    updated_count = 0
    if result is None:
        print("Рыба не найдена в базе данных")
    else:
        # Увеличение количества рыбы на 1
        updated_count = result[0] + 1
        cursor.execute("UPDATE riby SET kolvo = ? WHERE riba = ?", (updated_count, fish_name))
        conn.commit()
        print(f"Количество рыбы {fish_name} увеличено на 1")

    # Закрытие соединения
    conn.close()
    return updated_count


#   ОБНАВЛЕНИЕ ПОЛЯ В ИНТЕРФЕЙСЕ
def update_text_field(riba, kolvo):
    # Поиск соответствующего поля text_field
    if riba == "Стерлядь":
        text_fields[0].delete("1.0", tk.END)
        text_fields[0].insert(tk.END, kolvo)
    elif riba == "Лосось":
        text_fields[1].delete("1.0", tk.END)
        text_fields[1].insert(tk.END, kolvo)
    elif riba == "Осетр":
        text_fields[2].delete("1.0", tk.END)
        text_fields[2].insert(tk.END, kolvo)
    elif riba == "Чёрный Амур":
        text_fields[3].delete("1.0", tk.END)
        text_fields[3].insert(tk.END, kolvo)
    elif riba == "Скат":
        text_fields[4].delete("1.0", tk.END)
        text_fields[4].insert(tk.END, kolvo)
    elif riba == "Тунец":
        text_fields[5].delete("1.0", tk.END)
        text_fields[5].insert(tk.END, kolvo)
    elif riba == "Мальма":
        text_fields[6].delete("1.0", tk.END)
        text_fields[6].insert(tk.END, kolvo)
    elif riba == "Фугу":
        text_fields[7].delete("1.0", tk.END)
        text_fields[7].insert(tk.END, kolvo)
    else:
        text_box.insert(tk.END, "Я не понял, сори)" + "\n")
        text_box.see(tk.END)
        # print("Я не понял, сори)")
    for text_field in text_fields:
        if text_field.get("1.0", tk.END).startswith(f"Рыба: {riba}"):
            # Очистка поля text_field и обновление значения
            text_field.delete("1.0", tk.END)
            text_field.insert(tk.END, kolvo)
            break


# СКРИН
def background_screenshot(hwnd, X0, Y0, width,
                          height):  # ПОДАЕТСЯ: hwnd-окно игры; X0,Y0-начальные координаты; width,height-высота и шрина
    win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)  # возможно не нужны
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (width, height), dcObj, (X0, Y0), win32con.SRCCOPY)  # ДЕЛАЕТ СКРИН ОБЛАСТИ
    # win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0) # возможно не нужны
    dataBitMap.SaveBitmapFile(cDC, filename)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


# Находим цвет пикселя
def set_hex(color):
    r = color & 0xFF
    g = color >> 8 & 0xFF
    b = color >> 16
    col = [r, g, b]
    return col


# Чекаем капчу есть она лили нет и если есть вкл музыку??????????????????????????????????
def kapcha_opoveshenie():
    # global status
    # Получаем пиксель с экрана
    win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
    time.sleep(0.2)
    dc = win32gui.GetWindowDC(hwnd)
    color = win32gui.GetPixel(dc, kapcha_x, kapcha_y)
    win32gui.ReleaseDC(hwnd, dc)
    # win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0)
    zvet = set_hex(color)
    if (kapcha[0] == zvet[0] and kapcha[1] == zvet[1] and kapcha[2] == zvet[2]):
        AudioPlayer("kapcha.mp3").play(block=True)
        kapcha_naydena(hwnd)
        # status = False


# Если капча все еще там то цикл работает???????????????????????????????????????????????????
def kapcha_naydena():
    # global status
    # Получаем пиксель с экрана
    while True:
        win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
        dc = win32gui.GetWindowDC(hwnd)
        color = win32gui.GetPixel(dc, kapcha_x, kapcha_y)
        win32gui.ReleaseDC(hwnd, dc)
        time.sleep(1)
        # win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0)
        zvet = set_hex(color)
        if (kapcha[0] != zvet[0] and kapcha[1] != zvet[1] and kapcha[2] != zvet[2]):
            break


def cod():
    global ribalka_flag
    while ribalka_flag:
        #   ОТКРЫТИЕ ИНВЕНТАРЯ
        time.sleep(2)
        win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0X49, 0)  # Нажали I
        time.sleep(0.1)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0X49, 0)  # Отпустили I
        # win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0)
        time.sleep(1)
        #   СКРИН ЭКРАНА
        background_screenshot(hwnd, X0_inventar, Y0_inventar, X1_inventar - X0_inventar, Y1_inventar - Y0_inventar)
        img = cv2.imread('Image.png')
        pytesseract.pytesseract.tesseract_cmd = r"A:\cod\gtaРЫБАЛКА\teseract\tesseract.exe"  # подключение
        Ves_inventar = pytesseract.image_to_string(img,
                                                   config='--psm 11 tessedit_char_whitelist=0123456789')  # распознание цыфр и
        Ves_inventar = Ves_inventar[:4]
        pos = Ves_inventar.find('/')
        if 3 == pos:
            Ves_inventar = Ves_inventar[:-1]
            Ves_inventar = float(Ves_inventar)
            Ves_inventar = round(Ves_inventar / 100, 2)
        elif pos < 3:
            Ves_inventar = Ves_inventar[:pos]
            Ves_inventar = round(float(Ves_inventar), 2)
            Ves_inventar = Ves_inventar + 1
        else:
            Ves_inventar = round(float(Ves_inventar), 2)
        # if Ves_inventar[3] == '/':
        #     Ves_inventar = Ves_inventar[:-1]
        #     Ves_inventar = float(Ves_inventar)
        #     Ves_inventar = round(Ves_inventar/100, 2)
        # else:
        #     Ves_inventar = round(float(Ves_inventar), 2)
        text_box.insert(tk.END, "Вес инвентаря: " + str(Ves_inventar) + "\n")
        # print("Вес инвентаря: ", Ves_inventar)# вывод веса инвентаря
        time.sleep(1)
        win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0X49, 0)  # Нажали I
        time.sleep(0.1)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0X49, 0)  # Отпустили I
        # win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0)
        time.sleep(1)
        while Ves_inventar < 9.50 and ribalka_flag:
            win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
            time.sleep(0.5)
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0X35, 0)  # Нажали 5
            time.sleep(0.1)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0X35, 0)  # Отпустили 5
            time.sleep(4)
            # win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0)
            kapcha_opoveshenie()  # Проверяем есть ли капча
            Ves_inventar = round(Ves_inventar - 0.01, 2)
            text_box.insert(tk.END, "Вес инвентаря: " + str(Ves_inventar) + "\n")
            # print("Вес инвентаря: ", Ves_inventar)# вывод веса инвентаря
            time.sleep(5)
            nekras = True
            # Ждем пока появится мышка на клик
            while nekras and ribalka_flag:
                win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
                time.sleep(0.2)
                dc = win32gui.GetWindowDC(hwnd)
                color = win32gui.GetPixel(dc, krasn_x, krasn_y)
                win32gui.ReleaseDC(hwnd, dc)
                # win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0)
                zvet = set_hex(color)
                if (krasn[0] == zvet[0] and krasn[1] == zvet[1] and krasn[2] == zvet[2]):
                    nekras = False  # Мышка появилась
            nekras = True
            time.sleep(0.1)
            # Ждем пока выловит1111111111111111111111111111111111111111111111111111111
            while nekras and ribalka_flag:
                win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
                dc = win32gui.GetWindowDC(hwnd)
                color = win32gui.GetPixel(dc, krasn_x, krasn_y)
                win32gui.ReleaseDC(hwnd, dc)
                zvet = set_hex(color)  # Пиксель левой кнопки мышы(касной)
                dc = win32gui.GetWindowDC(hwnd)
                color = win32gui.GetPixel(dc, krasn_net_x, krasn_net_y)
                win32gui.ReleaseDC(hwnd, dc)
                zvet_k = set_hex(color)  # Пиксель правой кнопки мышы(серой)
                # win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0)
                if (krasn[0] == zvet[0] and krasn[1] == zvet[1] and krasn[2] == zvet[2]):  # Если левая красная, пикаем
                    win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0)
                    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON,
                                         l_param)  # нажать левую кнопку мыши
                    time.sleep(0.05)
                    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, l_param)  # отпустить левую кнопку мыши
                    # win32api.SendMessage(hwnd, win32con.WM_KILLFOCUS, 0)
                    time.sleep(0.1)
                if (krasn_net[0] != zvet_k[0] and krasn_net[1] != zvet_k[1] and krasn_net[2] != zvet_k[
                    2]):  # Если правая серая, продолжаем чекать красную
                    nekras = False
            time.sleep(1.2)
            riba = ""
            while True:
                background_screenshot(hwnd, X0_rib, Y0_rib, X1_rib - X0_rib, Y1_rib - Y0_rib)
                img = cv2.imread('Image.png')
                pytesseract.pytesseract.tesseract_cmd = r"A:\cod\gtaРЫБАЛКА\teseract\tesseract.exe"
                riba = pytesseract.image_to_string(img, lang="rus", config='--psm 11')
                if riba != "":
                    if riba[0] == "В" and riba[1] == "ы":
                        break
            # print("Рыба: ", riba)
            riba = riba.split(' ')[2]
            # print("Рыба - : ", riba)
            if riba.endswith('.'):
                riba = riba[:-1]
            if riba == "Стерлядь":
                text_box.insert(tk.END, "Вы поймали Стерлядь" + "\n")
                text_box.see(tk.END)
                # print("Вы поймали Стерлядь")
                kolvo = increase_fish_count(riba)
                update_text_field(riba, kolvo)
                increase_fish_count(riba)
            elif riba == "Лосось":
                text_box.insert(tk.END, "Вы поймали Лосось" + "\n")
                text_box.see(tk.END)
                # print("Вы поймали Лосось")
                kolvo = increase_fish_count(riba)
                update_text_field(riba, kolvo)
                increase_fish_count(riba)
            elif riba == "Осетр":
                text_box.insert(tk.END, "Вы поймали Осетра" + "\n")
                text_box.see(tk.END)
                # print("Вы поймали Осетра")
                kolvo = increase_fish_count(riba)
                update_text_field(riba, kolvo)
                increase_fish_count(riba)
            elif riba == "Чёрный Амур":
                text_box.insert(tk.END, "Вы поймали Чёрный Амур" + "\n")
                text_box.see(tk.END)
                # print("Вы поймали Чёрный Амур")
                kolvo = increase_fish_count(riba)
                update_text_field(riba, kolvo)
                increase_fish_count(riba)
            elif riba == "Скат":
                text_box.insert(tk.END, "Вы поймали Скат" + "\n")
                text_box.see(tk.END)
                # print("Вы поймали Скат")
                kolvo = increase_fish_count(riba)
                update_text_field(riba, kolvo)
                increase_fish_count(riba)
            elif riba == "Тунец":
                text_box.insert(tk.END, "Вы поймали Тунец" + "\n")
                text_box.see(tk.END)
                # print("Вы поймали Тунец")
                kolvo = increase_fish_count(riba)
                update_text_field(riba, kolvo)
                increase_fish_count(riba)
            elif riba == "Мальма":
                text_box.insert(tk.END, "Вы поймали Мальма" + "\n")
                text_box.see(tk.END)
                # print("Вы поймали Мальма")
                kolvo = increase_fish_count(riba)
                update_text_field(riba, kolvo)
                increase_fish_count(riba)
            elif riba == "Фугу":
                text_box.insert(tk.END, "Вы поймали Фугу" + "\n")
                text_box.see(tk.END)
                # print("Вы поймали Фугу")
                kolvo = increase_fish_count(riba)
                update_text_field(riba, kolvo)
                increase_fish_count(riba)
            else:
                text_box.insert(tk.END, "Я не понял, сори)" + "\n")
                text_box.insert(tk.END, "Вот что я понял" + riba + "\n")
                text_box.see(tk.END)
                # print("Я не понял, сори)")


# <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><   <º)))><

# Функции для кнопок
def start_button_click():
    selected_value = dropdown.get()
    if selected_value == "Ловить рыбу":
        text_box.insert(tk.END, "Вы выбрали Ловить рыбу\n")
        text_box.see(tk.END)
        global ribalka_flag
        ribalka_flag = True
        vivod_dannih()
        thread1 = threading.Thread(target=cod)
        thread1.start()
    elif selected_value == "Качалка":
        text_box.insert(tk.END, "Вы выбрали Качалку\n")
        text_box.insert(tk.END, "ЕЩЕ НЕ РАБОТАЕТ\n")
        text_box.see(tk.END)
    elif selected_value == "Стройка":
        text_box.insert(tk.END, "Вы выбрали Стройку\n")
        text_box.insert(tk.END, "ЕЩЕ НЕ РАБОТАЕТ\n")
        text_box.see(tk.END)
    elif selected_value == "Порт":
        text_box.insert(tk.END, "Вы выбрали Порт\n")
        text_box.insert(tk.END, "ЕЩЕ НЕ РАБОТАЕТ\n")
        text_box.see(tk.END)
    elif selected_value == "Каменоломня":
        text_box.insert(tk.END, "Вы выбрали Каменоломня\n")
        text_box.insert(tk.END, "ЕЩЕ НЕ РАБОТАЕТ\n")
        text_box.see(tk.END)
    elif selected_value == "Готовить Смузи":
        text_box.insert(tk.END, "Вы выбрали Готовить Смузи\n")
        text_box.insert(tk.END, "ЕЩЕ НЕ РАБОТАЕТ\n")
        text_box.see(tk.END)
    elif selected_value == "Жарить стерлядь":
        text_box.insert(tk.END, "Жарить стерлядь\n")
        text_box.insert(tk.END, "ЕЩЕ НЕ РАБОТАЕТ\n")
        text_box.see(tk.END)


def reset_button_click():
    text_box.delete("1.0", tk.END)


def zanogo_button_click():
    text_box.delete("1.0", tk.END)


def stop_button_click():
    global ribalka_flag, kachalka_flag, stroika_flag, port_flag, kamenolomnya_flag, smuzy_flag, sterlyad_flag
    ribalka_flag = False
    kachalka_flag = False
    stroika_flag = False
    port_flag = False
    kamenolomnya_flag = False
    smuzy_flag = False
    sterlyad_flag = False
    text_box.insert(tk.END, "Сообщение", "Операция остановлена.")


#   ОПИСАНИЕ ИНТЕРФЕЙСА
# Создание окна приложения
window = tk.Tk()
window.title("Мое приложение")

# Установка размеров окна и фиксация
window.geometry("400x200")
window.resizable(False, False)

# Создание вертикального разделителя
separator = tk.Frame(window, width=5, bg='black')
separator.pack(side='top', fill='x')

# Создание верхней части окна
top_frame = tk.Frame(window)
top_frame.pack(side='top', expand=True, fill='both')

# Создание нижней части окна
bottom_frame = tk.Frame(window, height=20)
bottom_frame.pack(side='top', expand=True, fill='both')

# Создание Части1 (верхняя левая часть)
part1_frame = tk.Frame(top_frame)
part1_frame.pack(side='left', expand=True, fill='both')
# Создание текстового поля в левой части
text_box = tk.Text(part1_frame, width=35, height=10)
text_box.pack(anchor='nw')

# Создание Части2 (верхняя правая часть)
part2_frame = tk.Frame(top_frame)
part2_frame.pack(side='left', expand=True, fill='both')
# # Создание 8 строк в правой части
labels = ['Стерлядь', 'Лосось', 'Осетр', 'Чер.Амур', 'Скат', 'Тунец', 'Мальма', 'Фугу']
#   ПЕРЕМЕННАЯ ДЛЯ СОХРАНЕНИЕ ВСЕХ
text_fields = []

for i, label_text in enumerate(labels):
    frame = tk.Frame(part2_frame)
    frame.pack(anchor='w')
    label = tk.Label(frame, text=label_text, width=10)
    label.pack(side='left')
    text = tk.Text(frame, width=5, height=1)
    text.pack(side='left')
    text_fields.append(text)  # Добавление поля Text в список

# Создание Части3 (нижняя часть)
part3_frame = tk.Frame(bottom_frame)
part3_frame.pack(side='top', expand=True, fill='both')

# Создание выпадающего списка
dropdown_values = ["Ловить рыбу", "Качалка", "Стройка", "Порт", "Каменоломня", "Готовить Смузи", "Жарить стерлядь"]
dropdown = tk.StringVar(part3_frame)
dropdown.set(dropdown_values[0])  # Значение по умолчанию
dropdown_menu = tk.OptionMenu(part3_frame, dropdown, *dropdown_values)
dropdown_menu.pack(side='left', padx=5, pady=5)

# Добавление кнопок
start_button = tk.Button(part3_frame, text="Начать", command=start_button_click)
start_button.pack(side='left', padx=5, pady=5)

reset_button = tk.Button(part3_frame, text="Сбросить", command=reset_button_click)
reset_button.pack(side='left', padx=5, pady=5)

stop_button = tk.Button(part3_frame, text="Стоп", command=stop_button_click)
stop_button.pack(side='left', padx=5, pady=5)

zanogo_button = tk.Button(part3_frame, text="Перезапуск", command=zanogo_button_click)
zanogo_button.pack(side='left', padx=5, pady=5)

# Запуск главного цикла приложения
window.mainloop()
