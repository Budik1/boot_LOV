import time

import fun
import heroes
import heroes as her
import find_img as find
import my_color_text as mct


def change_acc(*, hero_name_in_file):
    def reload_page():
        pos_my_game = find.find_my_games()
        x_pos, y_pos = pos_my_game
        y_pos += 300
        pos_right_click = x_pos, y_pos
        fun.mouse_move(pos=pos_right_click, speed=0.3)
        fun.mouse_right_click()

        x_vid, y_vid = pos_right_click
        x_vid += 100
        y_vid += 150
        pos_vid = x_vid, y_vid
        fun.mouse_move(pos=pos_vid, speed=0.6)
        pos_reload_page = find.find_reload_page()
        faze = True
        while not pos_reload_page:
            x_faze, y_faze = pos_vid
            if faze:
                y_faze -= 150
                faze = False
            else:
                y_faze += 150
                faze = True
            fun.mouse_move(pos=(x_faze, y_faze), speed=0.5)
            time.sleep(0.5)
            pos_reload_page = find.find_reload_page()
        fun.mouse_move_to_click(pos_click=pos_reload_page)
        start_time_after_reloat = time.time()
        return start_time_after_reloat

    move_time = 1
    # опознать героя
    vid = fun.selection_hero()
    while not vid:
        fun.push_close_all_()
        vid = fun.selection_hero()
    activ_hero = her.Hero.get_hero_name_in_file(her.Active.hero_activ)
    # print(f'{hero_name_in_file=}, {activ_hero=}')
    # проверить совпадение
    if hero_name_in_file == activ_hero:
        print('этот герой уже активен))')
        return
    img_button_expand = find.find_expand()
    # если не видно кнопки "развернуть" активировать окно
    if not img_button_expand:
        print('невидно кнопки развернуть)) активирую окно')
        # активация окна (если не активно)
        pos = find.find_my_games()
        x_change1, y_change1 = pos
        y_change1 -= 35
        pos_activate_win = x_change1, y_change1
        fun.mouse_left_click(pos=pos_activate_win)

    # развернуть окно
    img_button_expand = find.find_expand()
    fun.mouse_move_to_click(pos_click=img_button_expand)
    fun.wait_and_stop_img(name_img='img/everything/event_entry/collapse.png', message='жду collapse')
    print('окно окончательно развернуто, можно открывать меню')
    # вычисление позиции меню смены аккаунта
    pos = find.find_my_games()
    x_menu, y_menu = pos
    x_menu += 435
    # y_menu += 30
    pos_menu = x_menu, y_menu
    # открыть меню смены аккаунта если закрыто
    pos_menu_is_open = find.find_add_acc()
    if not pos_menu_is_open:
        fun.mouse_move_to_click(pos_click=pos_menu, move_time=0.3)
    # нажать нужного героя
    change_hero = fun.locCenterImg(f'img/hero/change_hero/change hero {hero_name_in_file}.png')
    print(f'выбор {hero_name_in_file}')
    fun.mouse_move_to_click(pos_click=change_hero)
    # collapse win
    pos_collapse = find.find_collapse()
    fun.mouse_move_to_click(pos_click=pos_collapse)
    print('свернул окно')
    # процесс загрузки игры
    pos_fountain = find.find_fountain()
    load_game_img = find.find_load_game()
    # ожидание обновления окна
    while pos_fountain:
        pos_fountain = find.find_fountain()

    start_time = time.time()
    mark_load_game_img = False
    mark_progress_load = False
    home_page = mark_progress_load and mark_load_game_img
    interval_load_time = -1
    interval_id_time = -1
    extra_time = 4
    while not home_page:
        if load_game_img:
            print('окно загрузки игры есть')
            mark_load_game_img = True
            # print(f'{mark_load_game_img=} 1')
            pos_slider = find.find_slider()
            # fun.mouse_move(pos=pos_slider)
            # pyautogui.dragTo(pos_slider[0], pos_slider[1] + 80, duration=5)
            fun.mouse_take_drag_drop_y(pos_take=pos_slider, dist=79, speed=0.2)
            pos_not_progress_load = find.find_progress_load()
            print('жду загрузки')
            start_time = time.time()

            while pos_not_progress_load:
                pos_not_progress_load = find.find_progress_load()
                present_time = time.time()
                pause = round(present_time - start_time)
                mark_progress_load = True
                # print(f'{mark_progress_load=} 1')
                if pause != interval_load_time:
                    interval_load_time = pause
                    print(f'{pause=} в ожидании загрузки игры')
                if pause >= (heroes.Active.max_time_wait_load + extra_time):
                    print('Надо обновить страницу')
                    start_time = reload_page()
                    mark_load_game_img = False
                    break

            # mark_progress_load = True
        # если нет окна загрузки игры
        else:
            # print('нет окна загрузки игры')
            mark_load_game_img = False
            mark_progress_load = False
            present_time = time.time()
            pause = round(present_time - start_time)
            if pause != interval_id_time:
                interval_id_time = pause
                print(f'{pause=} в ожидании ID')
            vk_id = find.find_enter_vk_id()
            if vk_id:
                continue_hero = fun.locCenterImg(f'img/everything/event_entry/continue {hero_name_in_file}.png')
                fun.mouse_move_to_click(pos_click=continue_hero)
            if pause > (heroes.Active.max_time_wait_id + extra_time):
                print('Надо обновить страницу')
                start_time = reload_page()
        # pos_fountain = find.find_fountain()
        load_game_img = find.find_load_game()
        home_page = mark_progress_load and mark_load_game_img
    # fun.wait_and_stop_img(name_img='img/city/fountain_on_the_square.png', message='жду появления фонтана')

    stop_close_img = False
    stop_fountain_img = False
    while not stop_close_img  and not stop_fountain_img:
        print('жду окончания загрузки')
        close_img1 = find.find_close()
        fountain_img1 = find.find_fountain()
        close_img2 = find.find_close()
        fountain_img2 = find.find_fountain()
        if (close_img1 == close_img2) and close_img1:
            stop_close_img = True
        else:
            stop_close_img = False
        if (fountain_img1 == fountain_img2) and fountain_img1:
            stop_fountain_img = True
        else:
            stop_fountain_img = False

    pos_progress = find.find_progress()
    if pos_progress:
        pos_slider = find.find_slider()
        fun.mouse_take_drag_drop_y(pos_take=pos_slider, dist=8, speed=0.1)
    print('смена героя окончена')

    print()
    param_change = mct.tc_red('параметр увеличен')
    param_not_change = mct.tc_green('параметр неизменен')
    if heroes.Active.max_time_wait_load < interval_load_time:
        heroes.Active.max_time_wait_load = interval_load_time
        print(f'{interval_load_time=}, {param_change}  {heroes.Active.max_time_wait_load=}')
    else:
        print(f'{interval_load_time=}, {param_not_change}  {heroes.Active.max_time_wait_load=}')

    if heroes.Active.max_time_wait_id < interval_id_time:
        heroes.Active.max_time_wait_id = interval_id_time
        print(f'{interval_id_time=}, {param_change}  {heroes.Active.max_time_wait_id=}')
    else:
        print(f'{interval_id_time=}, {param_not_change}  {heroes.Active.max_time_wait_id=}')

