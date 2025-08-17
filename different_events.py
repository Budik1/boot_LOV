import os
from time import sleep

import fun
import find_img
import my_color_text
# import sounds


def exit_to_fountain():
    # print('fun.exit_to_fountain')
    img_to_fountain = fun.locCenterImg('img/city/houses/to_fountain_from_houses.png')
    while not img_to_fountain:
        sleep(1)
        print(img_to_fountain, 'to_fountain')
        img_to_fountain = fun.locCenterImg('img/city/houses/to_fountain_from_houses.png', 0.85)

    fun.Mouse.move_to_click(pos_click=img_to_fountain, speed=0.5)


def attack_guru():
    name = fun.selection_hero()
    if name == 'Gavr' or name == 'Gadya' or name == 'Veles':
        # переход на экран 'ученики и наставники'
        guru = find_img.find_guru()
        # print('guru', guru)
        fun.mouse_move_to_click(guru, 0.2)
        # подтверждение открытия окна "наставник - ученик"
        fun.wait_and_stop_img(name_img='img/city/guru/guru_and_students.png')
        # переход на экран атаки
        attack_guru_img1 = fun.wait_and_stop_img(name_img="img/city/guru/attak_guru.png")
        fun.mouse_move_to_click(attack_guru_img1, 0.2)
        # нажать кнопку "атаковать"
        in_battle_img = fun.wait_and_stop_img(name_img='img/arena/in_battle.png')
        fun.mouse_move_to_click(in_battle_img, 0.2)
        # нажать кнопку "закрыть"
        close_img = fun.wait_and_stop_img(name_img='img/everything/close.png', param_confidence=0.85)
        fun.mouse_move_to_click(close_img, 0.1)
        return name
    elif name == 'Mara':
        con = 0.87
        guru = fun.locCenterImg('img/city/friend_line/i_am_guru.png', confidence=con)
        while not guru:
            arr = fun.locCenterImg('img/city/friend_line/arrow_right.png')
            fun.mouse_move_to_click(arr, 0)
            x, y = arr
            y -= 30
            pos = x, y
            fun.mouse_move(pos=pos)
            guru = fun.locCenterImg('img/city/test_guru.png', confidence=con)
        fun.mouse_move(pos=guru)
        fun.mouse_move_to_click(pos_click=guru, z_p_k=0)
        # x, y = guru
        # x -= 26
        # y -= 46
        # fun.mouse_move(pos=(x, y), speed=0.5)
        # x_demo, y_demo = x, y
        # change_x = 20
        # change_y = 20
        # x_demo += change_x
        # y_demo += change_y
        # fun.mouse_move(pos=(x_demo, y_demo), speed=0.5)
        # fun.foto('img/city/friend_line/button_attack_friend.png', (x, y, change_x, change_y))
        attack = fun.wait_and_stop_img(name_img='img/city/friend_line/button_attack_friend.png', message='wait attack')
        fun.mouse_move_to_click(pos_click=attack, z_p_k=0.5)
        in_battle_img = fun.wait_and_stop_img(name_img='img/arena/in_battle.png')
        fun.mouse_move_to_click(in_battle_img, 0.2)
        # нажать кнопку "закрыть"
        close_img = fun.wait_and_stop_img(name_img='img/everything/close.png', param_confidence=0.85)
        fun.mouse_move_to_click(close_img, 0.1)
        return name


def craps():
    #
    dock = find_img.find_dock()
    if not dock:
        print('no dock')
    else:
        fun.mouse_move_to_click(pos_click=dock, move_time=1, z_p_k=0.2)
    # ожидание прорисовки экрана пристани
    fun.wait_and_stop_img(name_img='img/city/dock/forge.png')
    # зайти к лодочнику
    boatman = find_img.find_boatman()
    fun.mouse_move_to_click(pos_click=boatman)
    # ожидание прорисовки входа
    fun.wait_and_stop_img(name_img='img/city/dock/link_boatman.png')
    link_boatman = find_img.find_link_boatman()
    fun.mouse_move(pos=link_boatman)
    # нажать сыграть в кости
    game_craps = find_img.find_game_craps()
    fun.mouse_move_to_click(game_craps)
    # ожидание прорисовки игры
    shot_craps = find_img.find_shot_craps()
    while not shot_craps:
        many_shot = find_img.find_many_shot()
        shot_craps = find_img.find_shot_craps()
        if many_shot:
            break
    shot_craps = find_img.find_shot_craps()
    if shot_craps:
        fun.mouse_move_to_click(shot_craps)

    finish_game = None
    close = None
    many_shot = None
    while (not finish_game) and (not close) and (not many_shot):
        finish_game = find_img.find_finish_game_craps()
        close = find_img.find_close()
        many_shot = find_img.find_many_shot()

    # sounds.melody_vic()
    print('ok')
    return


def numbers_lvl_list():
    directory = "C:/py_bot/boot_LOV_2/img/energy/lvl"
    files = os.listdir(directory)
    lvl_dig_list = []
    for name in files:
        dig = fun.extraction_digit(item=name)
        lvl_dig_list.append(dig)
    return lvl_dig_list



def creating_photo_lvl(*, lvl_num):
    if not lvl_num:
        # sounds.melody_fail()
        print(my_color_text.tc_red('не введен параметр уровня'))
        return
    # Указываем путь к директории
    directory = "C:/py_bot/boot_LOV_2/img/energy/lvl"
    # Получаем список файлов
    files = os.listdir(directory)
    # Выводим список файлов

    lvl_dig_list = numbers_lvl_list()
    # Выводим список номеров уровней
    print(lvl_dig_list)
    # проверяю наличие файла в списке
    if int(lvl_num) in lvl_dig_list:
        print(f'Имя "{lvl_num}lvl" существует в списке файлов')
        # и соответствие действительности
        for file in files:
            name_file = f'img/energy/lvl/{file}'
            control = fun.locCenterImg(name_file)
            if control:
                print(my_color_text.tc_cyan(f'Найден файл с именем {file} соответствующий фактическому уровню))'))
                break
    else:
        print(f'Имя {lvl_num} не существует в списке файлов')
        name_file = f'img/energy/lvl/{lvl_num}lvl.png'
        pos = fun.find_link_i()
        # fun.Mouse.move(pos=pos, speed=1)
        x, y = pos
        y -= 94 - 1
        x += 26 + 1
        # fun.Mouse.move(pos=(x, y), speed=1)
        x_k, y_k = x, y
        change = 36
        x_k += change
        y_k += change
        # fun.Mouse.move(pos=(x_k, y_k), speed=1)
        fun.foto(name_file, (x, y, change, change))
        print(name_file)
    return


