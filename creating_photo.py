import pyautogui
from fun import foto, open_taverna, find_link_i, loc_center_img


def creating_photo_tasks():
    pos = open_taverna()
    width = 145
    height = 24
    step = 80
    x, y = pos
    x += 130
    y += 296
    r_x_1, r_y_1 = x, y
    foto("img/full_t/line_1.png", _region=(r_x_1, r_y_1, width, height))
    y += step
    r_x_2, r_y_2 = x, y
    foto("img/full_t/line_2.png", _region=(r_x_2, r_y_2, width, height))
    y += step
    r_x_3, r_y_3 = x, y
    foto("img/full_t/line_3.png", _region=(r_x_3, r_y_3, width, height))


def creating_photo_hero_in_hall_glory():
    in_hall_glory = pyautogui.locateCenterOnScreen('img/arena/link_in_hall_glory.png', confidence=0.98)
    pyautogui.moveTo(in_hall_glory, duration=1)
    x, y = in_hall_glory
    y += 116
    x -= 250
    pos = x, y
    # pyautogui.moveTo(pos, duration=1)
    foto('img/tests/hero_arena.png', (x, y, 140, 55))


def creating_photo_hero_ver_in_hall_glory():
    link_arena = pyautogui.locateCenterOnScreen('img/arena/link_arena.png', confidence=0.98)
    pyautogui.moveTo(link_arena, duration=1)
    x, y = link_arena
    y += 22
    x += 15
    pos = x, y
    pyautogui.moveTo(pos, duration=1)
    foto('img/tests/test_ver.png', (x, y, 214, 421))


def creating_photo_hero():
    pos = find_link_i()
    pyautogui.moveTo(pos, duration=1)
    x, y = pos
    y -= 90
    x -= 30
    pos = x, y
    # pyautogui.moveTo(pos, duration=1)
    foto('img/tests/test_her.png', (x, y, 58, 80))


def creating_photo_guru():
    pos = find_link_i()
    pyautogui.moveTo(pos, duration=1)
    x, y = pos
    y -= 81
    x += 581
    pyautogui.moveTo(x, y, duration=1)
    # x_k, y_k = x, y
    # x_k += 40
    # y_k += 40
    # pyautogui.moveTo(x_k, y_k, duration=1)
    foto('img/tests/guru.png', (x, y, 38, 37))


def attak_guru():
    pos = pyautogui.locateCenterOnScreen('img/city/guru.png', confidence=0.9)
    pyautogui.moveTo(pos, duration=1)
    x, y = pos
    y += 150
    x += 25
    # pyautogui.moveTo(x, y, duration=1)
    # x_k, y_k = x, y
    # x_k += 40
    # y_k += 40
    # pyautogui.moveTo(x_k, y_k, duration=1)
    foto('img/city/attak_guru.png', (x, y, 40, 40))


def first_cell_foto():
    exit_img = loc_center_img('img/everything/exit.png')
    if exit_img:
        pyautogui.moveTo(exit_img, duration=1)
        x, y = exit_img
        x += 55
        y -= 455
        cell = x, y
        x_v, y_v = cell
        pyautogui.moveTo(cell, duration=1)
        corr = 78
        x += corr
        y += corr
        pos = x, y
        pyautogui.moveTo(pos, duration=1)
        foto('img/tests/cell.png', (x_v, y_v, corr, corr))
    else:
        print('не вижу')
        

def mask_pos_foto():
    exit_img = loc_center_img('img/everything/exit.png')
    if exit_img:
        pyautogui.moveTo(exit_img, duration=1)
        x, y = exit_img
        x += 625
        y -= 485
        cell = x, y
        x_v, y_v = cell
        pyautogui.moveTo(cell, duration=1)
        corr = 78
        x += corr
        y += corr
        pos = x, y
        pyautogui.moveTo(pos, duration=1)
        foto('img/tests/cell.png', (x_v, y_v, corr, corr))
    else:
        print('не вижу')


def link_backpack():
    exit_img = loc_center_img('img/everything/exit.png')
    if exit_img:
        pyautogui.moveTo(exit_img, duration=1)
        x, y = exit_img
        x += 136
        y -= 485
        cell = x, y
        x_v, y_v = cell
        pyautogui.moveTo(cell, duration=1)
        # corr = 78
        # x += 80
        # y += 30
        # pos = x, y
        # pyautogui.moveTo(pos, duration=1)
        foto('img/tests/cell.png', (x_v, y_v, 87, 30))
    else:
        print('не вижу')


def creating_photo_lvl():
    pos = find_link_i()
    pyautogui.moveTo(pos, duration=1)
    x, y = pos
    y -= 94 -1
    x += 26 +1
    pyautogui.moveTo(x, y, duration=1)
    x_k, y_k = x, y
    change = 36
    x_k += change
    y_k += change
    pyautogui.moveTo(x_k, y_k, duration=1)
    foto('img/energy/lvl/22lvl.png', (x, y, change, change))


def creat_rezult():
    pos = find_link_i()
    pyautogui.moveTo(pos, duration=2)
    x, y = pos
    y += 54 - 1
    x += 370 + 1 + 2
    pyautogui.moveTo(x, y, duration=2)
    x_k, y_k = x, y
    change_x = 100 - 6
    change_y = 36 - 5
    x_k += change_x
    y_k += change_y
    pyautogui.moveTo(x_k, y_k, duration=1)
    foto('img/tests/test_rezult_.png', (x, y, change_x, change_y))


# creat_rezult()
# creating_photo_lvl()
# link_backpack()
# mask_pos_foto()
# first_cell_foto()
# attak_guru()
# creating_photo_guru()
# creating_photo_hero()
# creating_photo_tasks()
# creating_photo_hero_ver_in_hall_glory()
# creating_photo_hero_in_hall_glory()
