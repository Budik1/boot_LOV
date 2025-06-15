import pyautogui

import fun
import find_img as find


def button_expand():
    show = False
    # нахождение привязки
    pos = fun.locCenterImg('img/everything/my games.png')
    fun.mouse_move(pos=pos, show=show)
    # активация окна (если не активно)
    x_change1, y_change1 = pos
    y_change1 -= 35
    pos_change1 = x_change1, y_change1
    fun.mouse_move(pos=pos_change1, show=show)
    fun.mouse_left_click(pos=pos_change1)
    # смещение к верхнему углу
    x_change2, y_change2 = pos_change1
    x_change2 += 362
    y_change2 -= 16
    pos_change2 = x_change2, y_change2
    fun.mouse_move(pos=pos_change2, show=show)
    # смещение к нижнему углу
    x_demo, y_demo = pos_change2
    change_x = 20
    change_y = 20
    x_demo += change_x
    y_demo += change_y
    pos_demo = x_demo, y_demo
    fun.mouse_move(pos=pos_demo, speed=1, show=show)
    name_foto = 'img/everything/event_entry/expand.png'
    fun.foto(name_foto, (x_change2, y_change2, change_x, change_y))
    print(f'foto ok {name_foto}')


def button_collapse():
    show = False
    # нахождение привязки
    pos = fun.locCenterImg('img/everything/my games.png')
    fun.mouse_move(pos=pos, show=show)
    # активация окна (если не активно)
    x_change1, y_change1 = pos
    y_change1 -= 35
    pos_change1 = x_change1, y_change1
    fun.mouse_move(pos=pos_change1, show=show)
    fun.mouse_left_click(pos=pos_change1)
    # разворачивание окна
    pos_expand = find.find_expand()
    while not pos_expand:
        pos_expand = find.find_expand()
    fun.mouse_move_to_click(pos_click=pos_expand)
    # смещение к верхнему углу
    x_change2, y_change2 = pos_change1
    x_change2 += 822
    y_change2 -= 16
    pos_change2 = x_change2, y_change2
    fun.mouse_move(pos=pos_change2, show=show)
    # смещение к нижнему углу
    x_demo, y_demo = pos_change2
    change_x = 20
    change_y = 20
    x_demo += change_x
    y_demo += change_y
    pos_demo = x_demo, y_demo
    fun.mouse_move(pos=pos_demo, speed=1, show=show)
    name_foto = 'img/everything/event_entry/collapse.png'
    fun.foto(name_foto, (x_change2, y_change2, change_x, change_y))
    print(f'foto ok {name_foto}')


def button_change_hero():
    show = False
    # нахождение привязки
    pos = fun.locCenterImg('img/everything/my games.png')
    fun.mouse_move(pos=pos, show=show)
    # активация окна (если не активно)
    x_change1, y_change1 = pos
    y_change1 -= 35
    pos_change1 = x_change1, y_change1
    fun.mouse_move(pos=pos_change1, show=show)
    fun.mouse_left_click(pos=pos_change1)
    # разворачивание окна
    pos_expand = find.find_expand()
    while not pos_expand:
        pos_expand = find.find_expand()
    fun.mouse_move_to_click(pos_click=pos_expand)
    # смещение к верхнему углу
    x_change2, y_change2 = pos_change1
    # x_change2 += 580
    x_change2 += 600 + 7
    y_change2 += 110 + 148
    pos_change2 = x_change2, y_change2
    fun.mouse_move(pos=pos_change2, show=show)
    # смещение к нижнему углу
    x_demo, y_demo = pos_change2
    change_x = 165
    change_y = 40
    x_demo += change_x
    y_demo += change_y
    pos_demo = x_demo, y_demo
    fun.mouse_move(pos=pos_demo, speed=1, show=show)
    name_foto = 'img/hero/change_hero/add acc.png'
    fun.foto(name_foto, (x_change2, y_change2, change_x, change_y))
    print(f'foto ok {name_foto}')
    fun.melody_vic()
    return


def load_game():
    show = True
    # нахождение привязки
    pos = find.find_my_games()
    fun.mouse_move(pos=pos, show=show)
    # смещение к верхнему углу
    x_change1, y_change1 = pos
    x_change1 -= 230
    y_change1 += 220
    pos_change1 = x_change1, y_change1
    fun.mouse_move(pos=pos_change1, show=show)
    # смещение к нижнему углу
    x_demo, y_demo = pos_change1
    change_x = 300
    change_y = 180
    x_demo += change_x
    y_demo += change_y
    pos_demo = x_demo, y_demo
    fun.mouse_move(pos=pos_demo, speed=1, show=show)
    name_foto = 'img/everything/event_entry/load_game.png'
    fun.foto(name_foto, (x_change1, y_change1, change_x, change_y))
    print(f'foto ok {name_foto}')
    fun.melody_vic()
    return


def slider():
    show = True
    # нахождение привязки
    pos = find.find_my_games()
    fun.mouse_move(pos=pos, show=show)
    # смещение к верхнему углу
    x_change1, y_change1 = pos
    x_change1 += 415 + 3
    y_change1 += 200
    pos_change1 = x_change1, y_change1
    fun.mouse_move(pos=pos_change1, show=show)
    # смещение к нижнему углу
    x_demo, y_demo = pos_change1
    change_x = 20
    change_y = 80
    x_demo += change_x
    y_demo += change_y
    pos_demo = x_demo, y_demo
    fun.mouse_move(pos=pos_demo, speed=1, show=show)
    name_foto = 'img/everything/event_entry/slider.png'
    fun.foto(name_foto, (x_change1, y_change1, change_x, change_y))
    print(f'foto ok {name_foto}')
    fun.melody_vic()
    return

def progress():
    show = False
    # нахождение привязки
    pos = find.find_my_games()
    fun.mouse_move(pos=pos, show=show)
    # смещение к верхнему углу
    x_change1, y_change1 = pos
    x_change1 -= 462 - 8
    y_change1 += 27
    pos_change1 = x_change1, y_change1
    fun.mouse_move(pos=pos_change1, show=show)
    # смещение к нижнему углу
    x_demo, y_demo = pos_change1
    change_x = 115
    change_y = 13
    x_demo += change_x
    y_demo += change_y
    pos_demo = x_demo, y_demo
    fun.mouse_move(pos=pos_demo, speed=1, show=show)
    name_foto = 'img/everything/event_entry/progress.png'
    fun.foto(name_foto, (x_change1, y_change1, change_x, change_y))
    print(f'foto ok {name_foto}')
    fun.melody_vic()
    return

def progress_load():
    show = True
    # нахождение привязки
    pos = find.find_my_games()
    fun.mouse_move(pos=pos, show=show)
    # смещение к верхнему углу
    x_change1, y_change1 = pos
    x_change1 -= 285
    y_change1 += 612
    pos_change1 = x_change1, y_change1
    fun.mouse_move(pos=pos_change1, show=show)
    # смещение к нижнему углу
    x_demo, y_demo = pos_change1
    change_x = 115
    change_y = 40
    x_demo += change_x
    y_demo += change_y
    pos_demo = x_demo, y_demo
    fun.mouse_move(pos=pos_demo, speed=1, show=show)
    name_foto = 'img/everything/event_entry/progress_load.png'
    fun.foto(name_foto, (x_change1, y_change1, change_x, change_y))
    print(f'foto ok {name_foto}')
    fun.melody_vic()
    return

def fountain():
    show = False
    # нахождение привязки
    pos = find.find_my_games()
    fun.mouse_move(pos=pos, show=show)
    # смещение к верхнему углу
    x_change1, y_change1 = pos
    x_change1 -= 185
    y_change1 += 480
    pos_change1 = x_change1, y_change1
    fun.mouse_move(pos=pos_change1, show=show)
    # смещение к нижнему углу
    x_demo, y_demo = pos_change1
    change_x = 240
    change_y = 80
    x_demo += change_x
    y_demo += change_y
    pos_demo = x_demo, y_demo
    fun.mouse_move(pos=pos_demo, speed=1, show=show)
    name_foto = 'img/city/fountain_on_the_square.png'
    fun.foto(name_foto, (x_change1, y_change1, change_x, change_y))
    print(f'foto ok {name_foto}')
    fun.melody_vic()
    pos_f = fun.locCenterImg('img/city/fountain_on_the_square.png')
    fun.mouse_move(pos=pos_f)
    return


def continue_her():
    show = True
    # нахождение привязки
    pos = find.find_enter_vk_id()
    fun.mouse_move(pos=pos, show=show)
    # смещение к верхнему углу
    x_change1, y_change1 = pos
    x_change1 -= 150
    y_change1 += 156
    pos_change1 = x_change1, y_change1
    fun.mouse_move(pos=pos_change1, show=show)
    # смещение к нижнему углу
    x_demo, y_demo = pos_change1
    change_x = 306
    change_y = 38
    x_demo += change_x
    y_demo += change_y
    pos_demo = x_demo, y_demo
    fun.mouse_move(pos=pos_demo, speed=1, show=show)
    name_foto = 'img/everything/event_entry/continue gady.png'
    fun.foto(name_foto, (x_change1, y_change1, change_x, change_y))
    print(f'foto ok {name_foto}')
    pos_f = fun.locCenterImg(name_img=name_foto)
    fun.mouse_move(pos=pos_f)
    fun.melody_vic()
    return

# continue_her()
# fountain()
# progress_load()
# progress()
# button_change_hero()
# button_collapse()
# slider()
# load_game()
