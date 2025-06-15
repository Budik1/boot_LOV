import pyautogui
import fun
import find_img as find


def creating_photo_tasks():
    """ Создание фото заданий """
    pos = fun.open_taverna()
    width = 145
    height = 24
    step = 80
    x, y = pos
    x += 130
    y += 296
    r_x_1, r_y_1 = x, y
    fun.foto("img/full_t/line_1.png", _region=(r_x_1, r_y_1, width, height))
    y += step
    r_x_2, r_y_2 = x, y
    fun.foto("img/full_t/line_2.png", _region=(r_x_2, r_y_2, width, height))
    y += step
    r_x_3, r_y_3 = x, y
    fun.foto("img/full_t/line_3.png", _region=(r_x_3, r_y_3, width, height))


def creating_photo_hero_in_hall_glory():
    in_hall_glory = fun.locCenterImg('img/arena/link_in_hall_glory.png', confidence=0.98)
    pyautogui.moveTo(in_hall_glory, duration=1)
    x, y = in_hall_glory
    y += 116
    x -= 250
    pos = x, y
    # pyautogui.moveTo(pos, duration=1)
    fun.foto('img/tests/hero_arena-5.png', (x, y, 140, 55))


def creating_photo_hero_ver_in_hall_glory():
    link_arena = fun.locCenterImg('img/arena/link_arena.png', confidence=0.98)
    pyautogui.moveTo(link_arena, duration=1)
    x, y = link_arena
    rep = 53
    y += 22 + rep  # 22
    x += 15
    pos = x, y
    pyautogui.moveTo(pos, duration=1)
    fun.foto('img/tests/test_ver-5.png', (x, y, 214, 421 - rep))


def creating_photo_hero():
    pos = fun.find_link_i()
    pyautogui.moveTo(pos, duration=1)
    x, y = pos
    y -= 90
    x -= 30
    pos = x, y
    # pyautogui.moveTo(pos, duration=1)
    fun.foto('img/tests/test_her.png', (x, y, 58, 80))


def creating_photo_guru():
    pos = fun.find_link_i()
    pyautogui.moveTo(pos, duration=1)
    x, y = pos
    y -= 81
    x += 581
    pyautogui.moveTo(x, y, duration=1)
    # x_k, y_k = x, y
    # x_k += 40
    # y_k += 40
    # pyautogui.moveTo(x_k, y_k, duration=1)
    fun.foto('img/tests/guru.png', (x, y, 38, 37))


def attak_guru():
    pos = find.find_guru()
    pyautogui.moveTo(pos, duration=1)
    x, y = pos
    y += 150
    x += 25
    # pyautogui.moveTo(x, y, duration=1)
    # x_k, y_k = x, y
    # x_k += 40
    # y_k += 40
    # pyautogui.moveTo(x_k, y_k, duration=1)
    fun.foto('img/city/attak_guru.png', (x, y, 40, 40))


def first_cell_foto():
    exit_img = fun.locCenterImg('img/everything/exit.png', confidence=0.9)
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
        fun.foto('img/tests/cell.png', (x_v, y_v, corr, corr))
    else:
        print('не вижу')


def mask_pos_foto():
    exit_img = fun.locCenterImg('img/everything/exit.png', confidence=0.9)
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
        fun.foto('img/tests/cell.png', (x_v, y_v, corr, corr))
    else:
        print('не вижу')


def link_backpack():
    exit_img = fun.locCenterImg('img/everything/exit.png', confidence=0.9)
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
        fun.foto('img/tests/cell.png', (x_v, y_v, 87, 30))
    else:
        print('не вижу')


def creating_photo_lvl():
    pos = fun.find_link_i()
    pyautogui.moveTo(pos, duration=1)
    x, y = pos
    y -= 94 - 1
    x += 26 + 1
    pyautogui.moveTo(x, y, duration=1)
    x_k, y_k = x, y
    change = 36
    x_k += change
    y_k += change
    pyautogui.moveTo(x_k, y_k, duration=1)
    fun.foto('img/energy/lvl/29lvl.png', (x, y, change, change))
    print('29lvl.png create')


def creating_photo_clan():
    pos = fun.find_link_i()
    pyautogui.moveTo(pos, duration=1)
    x, y = pos
    y -= 40
    x += 26 + 1
    pos_foto = x, y
    pyautogui.moveTo(pos_foto, duration=1)
    x_k, y_k = x, y
    change = 48
    x_k += change
    y_k += change
    pyautogui.moveTo(x, y, duration=1)
    fun.foto('img/kv/clan_gadya2.png', (x, y, change, change))


def creating_result():
    """Результат задания"""
    pos = fun.find_link_i()
    pyautogui.moveTo(pos, duration=2)
    x, y = pos
    y += 54 - 1
    x += 370 + 1 + 2
    pyautogui.moveTo(x, y, duration=2)
    x_demo, y_demo = x, y
    change_x = 100 - 6
    change_y = 36 - 5
    x_demo += change_x
    y_demo += change_y
    pyautogui.moveTo(x_demo, y_demo, duration=1)
    fun.foto('img/tests/test_result_.png', (x, y, change_x, change_y))


def state_kv():
    pos = fun.click_update(1)
    x, y = pos
    x -= 390 - 5
    y -= 20
    pyautogui.moveTo(x, y, duration=1)
    x_demo, y_demo = x, y
    change_x = 180
    change_y = 100
    x_demo += change_x
    y_demo += change_y
    pyautogui.moveTo(x_demo, y_demo, duration=1)
    fun.foto('img/tests/state_kv_defeat.png', (x, y, change_x, change_y))
    print('foto ok')


def drop_in_raid2():
    pos = fun.click_update(1)
    x, y = pos
    x -= 419
    y += 241
    pyautogui.moveTo(x, y, duration=1)
    x_demo, y_demo = x, y
    change_x = 244
    change_y = 44
    x_demo += change_x
    y_demo += change_y
    pyautogui.moveTo(x_demo, y_demo, duration=1)
    fun.foto('img/tests/drop_in_raid.png', (x, y, change_x, change_y))
    print('foto ok')


def drop_in_raid():
    pos = fun.click_update(1)
    x, y = pos
    x -= 450 - 25
    y += 141 + 2
    pyautogui.moveTo(x, y, duration=1)
    x_demo, y_demo = x, y
    change_x = 200 - 25 - 9
    change_y = 270 - 8
    x_demo += change_x
    y_demo += change_y
    pyautogui.moveTo(x_demo, y_demo, duration=1)
    fun.foto('img/tests/drop_in_raid.png', (x, y, change_x, change_y))
    cnob = fun.cancel_or_knob()
    if cnob:
        fun.mouse_move_to_click(pos_click=cnob, z_p_k=0.5)
    print('foto ok')


def i_am_guru():
    pos = fun.find_link_i()
    pyautogui.moveTo(pos, duration=2)
    x, y = pos
    # x += 2
    y += 450
    pyautogui.moveTo(x, y, duration=2)
    x_demo, y_demo = x, y
    change_x = 70
    change_y = 60
    x_demo += change_x
    y_demo += change_y
    pyautogui.moveTo(x_demo, y_demo, duration=1)
    fun.foto('img/city/test_guru.png', (x, y, change_x, change_y))
    print('foto ok')


def img_atack_guru():
    pos = fun.locCenterImg('img/kv/update.png')
    if pos:
        fun.mouse_move(pos=pos)
        guru = fun.locCenterImg('img/city/test_guru.png')
        fun.mouse_move_to_click(guru, 0)
        x, y = guru
        x -= 30
        y -= 50
        fun.mouse_move(pos=(x, y))
        x_demo, y_demo = x, y
        change_x = 70
        change_y = 60
        x_demo += change_x
        y_demo += change_y

        # fun.foto('img/city/test_guru.png', (x, y, change_x, change_y))
        print('foto ok')

    else:
        print('невидно обновить')


def arrow_right():
    pos = fun.find_link_i()
    pyautogui.moveTo(pos, duration=2)
    x, y = pos
    x += 577 + 6
    y += 450
    pyautogui.moveTo(x, y, duration=2)
    x_demo, y_demo = x, y
    change_x = 30
    change_y = 40
    x_demo += change_x
    y_demo += change_y
    pyautogui.moveTo(x_demo, y_demo, duration=1)
    fun.foto('img/city/arrow_right.png', (x, y, change_x, change_y))
    print('foto ok')


def pos_work_completed():
    pos_item = fun.locCenterImg('img/everything/close.png')
    if pos_item:
        fun.mouse_move(pos=pos_item, speed=1)
        x, y = pos_item
        x -= 78
        y -= 178
        fun.mouse_move(pos=(x, y), speed=1)
        x_demo, y_demo = x, y
        change_x = 153
        change_y = 27
        x_demo += change_x
        y_demo += change_y
        fun.mouse_move(pos=(x_demo, y_demo), speed=1)
        fun.foto('img/everything/work_completed.png', (x, y, change_x, change_y))
        print('foto ok')
    else:
        print('no vision')


def her_war_thg(nam):
    pos = fun.locCenterImg('img/everything/skip_battle.png')
    if pos:
        print('бой идет')
        x, y = pos
        x += 0
        y -= 41
        # pyautogui.moveTo(x, y, duration=1)
        x_demo, y_demo = x, y
        change_x = 400
        change_y = 500
        x_demo += change_x
        y_demo += change_y
        # pyautogui.moveTo(x_demo, y_demo, duration=1)
        fun.foto(f'img/tests/{nam}.png', (x, y, change_x, change_y))
        print(f'foto {nam}. png ok')


def raid_opponent_img():
    pos = fun.locCenterImg('img/kv/update.png')
    # fun.move_mause(pos=pos)
    if pos:
        x, y = pos
        x -= 192
        y += 33
        # fun.move_mause(pos=(x, y), speed=1)
        x_demo, y_demo = x, y
        change_x = 195 + 5
        change_y = 156
        x_demo += change_x
        y_demo += change_y
        # fun.move_mause(pos=(x_demo, y_demo))
        name_foto = 'img/tests/raid_opponent/lich.png'
        fun.foto(name_foto, (x, y, change_x, change_y))
        print(f'foto ok {name_foto}')

    else:
        print('no vision')


def my_games_png():
    show = True
    pos = fun.locCenterImg('img/everything/my games.jpg')
    fun.mouse_move(pos=pos, show=show)
    if pos:
        x, y = pos
        x -= 42 - 3
        y -= 18
        fun.mouse_move(pos=(x, y), speed=1, show=show)
        x_demo, y_demo = x, y
        change_x = 84 - 4
        change_y = 36
        x_demo += change_x
        y_demo += change_y
        fun.mouse_move(pos=(x_demo, y_demo), show=show)
        name_foto = 'img/everything/my games.png'
        fun.foto(name_foto, (x, y, change_x, change_y))
        print(f'foto ok {name_foto}')


def repeat():
    show = False
    pos = fun.locCenterImg('img/everything/my games.png')
    fun.mouse_move(pos=pos, show=show)
    if pos:
        x, y = pos
        x -= 150
        y += 466
        fun.mouse_move(pos=(x, y), speed=1, show=show)
        x_demo, y_demo = x, y
        change_x = 140 + 4
        change_y = 29
        x_demo += change_x
        y_demo += change_y
        fun.mouse_move(pos=(x_demo, y_demo), show=show)
        name_foto = 'img/everything/repeat.png'
        fun.foto(name_foto, (x, y, change_x, change_y))
        print(f'foto ok {name_foto}')


def connection_problem():
    show = True
    pos = fun.locCenterImg('img/everything/my games.png')
    fun.mouse_move(pos=pos, show=show)
    if pos:
        x, y = pos
        x -= 180
        y += 210 + 1
        fun.mouse_move(pos=(x, y), speed=1, show=show)
        x_demo, y_demo = x, y
        change_x = 220 + 4 - 20
        change_y = 29
        x_demo += change_x
        y_demo += change_y
        fun.mouse_move(pos=(x_demo, y_demo), show=show)
        name_foto = 'img/everything/connection_problem.png'
        fun.foto(name_foto, (x, y, change_x, change_y))
        print(f'foto ok {name_foto}')

# connection_problem()
# my_games_png()
# raid_opponent_img()
# her_war_thg()
# pos_work_completed()
# img_atack_guru()
# arrow_right()
# i_am_guru()
# drop_in_raid()
# state_kv()
# creating_result()
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
