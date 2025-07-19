import pyautogui
from time import sleep, time
from fun import log
import fun
import baza_dannyx as b_d

par_conf = 0.9


# def wait_and_stop_img(name_img, region: tuple[int, int, int, int] | None = None, confidence=0.85):
#     """    Ждет появление и фиксацию картинки    """
#     img_1 = pyautogui.locateCenterOnScreen(name_img, region=region, confidence=confidence)
#     sleep(0.3)
#     img_2 = pyautogui.locateCenterOnScreen(name_img, region=region, confidence=confidence)
#     while not img_1 or img_1 != img_2:
#         if img_1 or img_2:
#             img_1 = pyautogui.locateCenterOnScreen(name_img, region=region, confidence=confidence)
#             sleep(0.3)
#             img_2 = pyautogui.locateCenterOnScreen(name_img, region=region, confidence=confidence)
#         else:
#             img_1 = pyautogui.locateCenterOnScreen(name_img, region=region, confidence=confidence)
#             sleep(0.3)
#             img_2 = pyautogui.locateCenterOnScreen(name_img, region=region, confidence=confidence)
#     if img_1 == img_2 and img_1:
#         return img_2


def battle_in_arena():
    # print('battle_in_arena')

    fun.my_print_to_file('arena.battle_in_arena')
    fun.my_print_to_file(f'quantity_battles = {b_d.quantity_battles}')

    link_in_hall_glory = fun.locCenterImg('img/arena/link_in_hall_glory.png', confidence=0.98)
    close = fun.locCenterImg('img/everything/close.png', confidence=0.89)

    if link_in_hall_glory:
        # print("в зале славы")
        x, y = link_in_hall_glory
        x -= 255
        y += 110
        region_search = x, y, 545, 65

    elif close:
        # print("видно закрыть")
        fun.push_close()
        fun.go_in_hall_glory()
        link_in_hall_glory = fun.locCenterImg('img/arena/link_in_hall_glory.png', confidence=0.98)
        while not link_in_hall_glory:
            print(link_in_hall_glory)
            link_in_hall_glory = fun.locCenterImg('img/arena/link_in_hall_glory.png', confidence=0.98)
    else:
        print("с главного экрана в зал славы")
        fun.go_in_hall_glory()
        link_in_hall_glory = fun.locCenterImg('img/arena/link_in_hall_glory.png', confidence=0.98)
        while not link_in_hall_glory:
            print(link_in_hall_glory)
            link_in_hall_glory = fun.locCenterImg('img/arena/link_in_hall_glory.png', confidence=0.98)

    link_in_hall_glory = fun.locCenterImg('img/arena/link_in_hall_glory.png', confidence=0.98)
    fun.my_print_to_file(f'link_in_hall_glory = , {link_in_hall_glory}')
    x, y = link_in_hall_glory
    x -= 255
    y += 110
    region_search = x, y, 545, 65
    # foto('img/tests/test_region_search.png', region_search)
    # return
    hero_arena = fun.locCenterImg('img/arena/hero_arena.png', confidence=0.95, region=region_search)
    fun.my_print_to_file(f'hero_arena = , {hero_arena}')
    it = 0
    it_att = 0
    while not hero_arena:
        attack = None
        if it == 0:
            fun.my_print_to_file("поиск противника")
        it += 1
        # print(it, attack)
        scroll_down = fun.locCenterImg('img/arena/scroll_down.png', region=(550, 550, 750, 750), confidence=0.98)
        while not scroll_down:
            sleep(0.5)
            scroll_down = fun.locCenterImg('img/arena/scroll_down.png', region=(550, 550, 750, 750), confidence=0.98)
            print(scroll_down, 'scroll_down в цикле поиска')
        scroll_down = fun.locCenterImg('img/arena/scroll_down.png', region=(550, 550, 750, 750), confidence=0.98)
        # print(scroll_down, 'scroll_down нажимаем')
        fun.Mouse.move_to_click(pos_click=scroll_down, speed=0.1)
        attack = fun.wait_and_stop_img(name_img='img/arena/attack.png', region=region_search, param_confidence=0.95)
        hero_arena = fun.locCenterImg(name_img='img/arena/hero_arena.png', confidence=0.95, region=region_search)
        if not hero_arena:
            # name_foto_h = f'img/tests/test{it}_hero_arena.png'
            # print(name_foto_h)
            # foto(name_foto_h, region_search)
            hero_arena = fun.locCenterImg(name_img='img/arena/hero_arena.png', confidence=0.95, region=region_search)
        else:
            pass
            # print('найден')

    fun.my_print_to_file(f' it = {it}')
    # attack = pyautogui.locateCenterOnScreen('img/arena/attack.png', confidence=0.95, region=region_search)
    attack = fun.wait_and_stop_img(name_img='img/arena/attack.png', region=region_search, param_confidence=0.95)
    fun.my_print_to_file(f'attack = {attack}')
    fun.Mouse.move_to_click(pos_click=attack, speed=0.2)
    link_arena = fun.locCenterImg('img/arena/link_arena.png')
    fun.my_print_to_file(f'link_arena = {link_arena}')
    while not link_arena:
        sleep(1)
        link_arena = fun.locCenterImg('img/arena/link_arena.png')
    fun.my_print_to_file(f'link_arena = {link_arena}')
    hero_arena_ver = fun.locCenterImg('img/arena/hero_arena_ver.png')
    if hero_arena_ver:
        fun.my_print_to_file("безоружен")
        print("безоружен")
        b_d.quantity_battles += 1
        pos_i = fun.find_link_i()
        in_battl = fun.locCenterImg('img/arena/in_battle.png')
        it_in_battl = 0
        while not in_battl:
            if it_in_battl == 0:
                fun.my_print_to_file("ожидание боя")
            it_in_battl += 1
            sleep(1)
            in_battl = fun.locCenterImg('img/arena/in_battle.png')
        fun.my_print_to_file(f'in_battl = {in_battl}')
        fun.Mouse.move_to_click(pos_click=in_battl, speed=0.2)
        skip_battle = fun.locCenterImg('img/everything/skip_battle.png', confidence=par_conf)
        it_skip_battle = 0
        while not skip_battle:
            if it_skip_battle == 0:
                fun.my_print_to_file("ожидание пропустить бой")
            it_skip_battle += 1
            sleep(1)
            skip_battle = fun.locCenterImg('img/everything/skip_battle.png', confidence=par_conf)
        # print("есть пропустить бой")
        fun.in_battle(par_conf, pos_i)
        close = fun.locCenterImg('img/everything/close.png', confidence=0.89)
        it_close = 0
        while not close:
            fun.my_print_to_file("ожидание close")
            it_close += 1
            sleep(0.2)
            close = fun.locCenterImg('img/everything/close.png', confidence=0.89)
        sleep(0.2)
        close = fun.locCenterImg('img/everything/close.png', confidence=0.89)
        fun.my_print_to_file("закрыть результат боя")
        fun.Mouse.move_to_click(pos_click=close, speed=0.1)
        sleep(1)
    else:
        print('вооружён')
        fun.my_print_to_file('вооружён')


def inspection_hero():
    fun.my_print_to_file('inspection_hero')
    in_hall_glory = fun.locCenterImg('img/arena/link_in_hall_glory.png', confidence=0.98)
    x, y = in_hall_glory
    y += 170
    link = x, y
    return link


def search_unarmed():
    """
    поиск невооруженного
    """

    start_time = time()
    fun.go_in_hall_glory()

    no_arms = fun.locCenterImg('img/no_arm.png', confidence=0.98)
    while not no_arms:
        fun.Mouse.move_to_click(pos_click=inspection_hero(), speed=0.05)

        ver_her_arms = fun.locCenterImg('img/ver_her_arms.png', confidence=0.98)
        while not ver_her_arms:
            # sleep(0.2)
            ver_her_arms = fun.locCenterImg('img/ver_her_arms.png', confidence=0.98)

        no_arms = fun.locCenterImg('img/no_arm.png', confidence=0.98)
        if no_arms:
            print('no_arms')
        else:
            fun.push_close()
            fun.Mouse.move_to_click(pos_click=fun.scroll_down(), speed=0.05)

    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')

# search_unarmed()
