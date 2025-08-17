import pyautogui
from time import sleep
import datetime

import find_img
import find_img as find
# import fun
import fun_down
import my_color_text as m_t
import heroes as her

log = 1


def one_in_two(symbol):
    if 0 <= symbol <= 9:
        return str(f'0{symbol}')
    else:
        return str(symbol)


def locCenterImg(name_img, confidence=0.9, region: tuple[int, int, int, int] | None = None):
    pos_img = fun_down.locCenterImg(name_img=name_img,
                                    confidence=confidence,
                                    region=region)
    return pos_img


def wait_and_stop_img(*, name_img, region: tuple[int, int, int, int] | None = None, param_confidence=0.85, message=''):
    """    Ждет появление и фиксацию картинки    """

    img_1 = locCenterImg(name_img, region=region, confidence=param_confidence)
    sleep(0.3)
    img_2 = locCenterImg(name_img, region=region, confidence=param_confidence)
    while not img_1 or img_1 != img_2:
        if message != '':
            print(f'{message}')
        if img_1 or img_2:
            img_1 = locCenterImg(name_img, region=region, confidence=param_confidence)
            sleep(0.3)
            img_2 = locCenterImg(name_img, region=region, confidence=param_confidence)
        else:
            img_1 = locCenterImg(name_img, region=region, confidence=param_confidence)
            sleep(0.3)
            img_2 = locCenterImg(name_img, region=region, confidence=param_confidence)
    if img_1 == img_2 and img_1:
        return img_2


def click_update(info=None):
    update = locCenterImg('img/kv/update.png', 0.9)
    sleep(0.2)
    update_1 = locCenterImg('img/kv/update.png', 0.9)
    while not update or update != update_1:
        update = locCenterImg('img/kv/update.png', 0.9)
        sleep(0.2)
        update_1 = locCenterImg('img/kv/update.png', 0.9)
    # print("обновить", update)
    if info:
        return update
    else:
        Mouse.move_to_click(update, 0.1)
        x, y = update
        x -= 25
        y += 25
        Mouse.move(pos=(x, y))


def my_print_to_file(text):
    if log == 1:
        time_now_value = time_now()
        date = date_now()
        file_name = date + ".txt"
        file = open('log/' + file_name, 'a+', encoding='utf-8')
        print(time_now_value, text, file=file)
        file.close()  # закрыть файл после работы с ним.


def time_now(date_class=False):
    """Если True:
            возвращает объект datetime.datetime
        Иначе:
            возвращает объект str"""
    now = datetime.datetime.now()
    # '%Y-%m-%d_%H:%M:%S' '%Y-%m-%d %H°%M\'\'%S\''
    time_now_ = (now.strftime('%Y-%m-%d %H:%M:%S'))
    # date = (now.strftime('%Y-%m-%d'))
    if date_class:
        return now
    else:
        return time_now_


def time_utc_now():
    now = datetime.datetime.now(datetime.UTC)
    time_now_ = (now.strftime('%Y-%m-%d %H:%M:%S'))
    return time_now_


def date_now():
    now = datetime.datetime.now()
    date = (now.strftime('%Y-%m-%d'))
    return date


def date_utc_now():
    utc_now = datetime.datetime.now(datetime.UTC)
    utc_date = (utc_now.strftime('%Y-%m-%d'))
    return utc_date


date_start_prog = date_utc_now()


class Mouse:

    @staticmethod
    def left_click(*, pos):
        # playsound('sound/mouse-click.wav')
        pyautogui.click(pos)
        pyautogui.hotkey('Ctrl')
        return

    @staticmethod
    def right_click():
        pyautogui.click(button='RIGHT')
        pyautogui.hotkey('Ctrl')
        return

    @staticmethod
    def move(*, pos: tuple, speed=0.2, show=True):
        if show:
            pyautogui.moveTo(pos, duration=speed)
        return

    @staticmethod
    def move_to_click(pos_click: tuple, speed=0.5, z_p_k=0.2):
        """
        Поместить указатель мыши по координатам и кликнуть, учитывая задержку.
        :param pos_click: Point
        :param speed: время перемещения указателя мыши в секундах
        :param z_p_k: задержка перед кликом(float)
        :return: None
        """
        my_print_to_file('move_to_click')
        sleep(0.3)
        mouse_move(pos=pos_click, speed=speed)  # , tween=pyautogui.easeInOutQuad
        # print('должен быть клик')
        sleep(z_p_k)
        if pos_click:
            mouse_left_click(pos=pos_click)
        else:
            print("некуда кликать")
        sleep(0.18)
        return

    @staticmethod
    def mouse_move_to_click(pos_click: tuple, move_time=0.5, z_p_k=0.2):
        """
        Поместить указатель мыши по координатам и кликнуть, учитывая задержку.
        :param pos_click: Point
        :param move_time: время перемещения указателя мыши в секундах
        :param z_p_k: задержка перед кликом(float)
        :return: None
        """
        my_print_to_file('move_to_click')
        sleep(0.3)
        mouse_move(pos=pos_click, speed=move_time)  # , tween=pyautogui.easeInOutQuad
        # print('должен быть клик')
        sleep(z_p_k)
        if pos_click:
            mouse_left_click(pos=pos_click)
        else:
            print("некуда кликать")
        sleep(0.18)
        return


def mouse_left_click(*, pos):
    # playsound('sound/mouse-click.wav')
    pyautogui.click(pos)
    pyautogui.hotkey('Ctrl')
    return


def mouse_right_click():
    pyautogui.click(button='RIGHT')
    pyautogui.hotkey('Ctrl')
    return


def mouse_move(*, pos: tuple, speed=0.2, show=True):
    if show:
        pyautogui.moveTo(pos, duration=speed)
    return


def mouse_move_to_click(pos_click: tuple, move_time=0.5, z_p_k=0.2):
    """
    Поместить указатель мыши по координатам и кликнуть, учитывая задержку.
    :param pos_click: Point
    :param move_time: время перемещения указателя мыши в секундах
    :param z_p_k: задержка перед кликом(float)
    :return: None
    """
    my_print_to_file('move_to_click')
    sleep(0.3)
    mouse_move(pos=pos_click, speed=move_time)  # , tween=pyautogui.easeInOutQuad
    # print('должен быть клик')
    sleep(z_p_k)
    if pos_click:
        mouse_left_click(pos=pos_click)
    else:
        print("некуда кликать")
    sleep(0.18)
    return


def mouse_take_drag_drop_y(pos_take, dist, speed=0.2):
    pyautogui.mouseDown(pos_take)
    x, y = pos_take
    y += dist
    new_pos = x, y
    mouse_move(pos=new_pos, speed=speed)
    pyautogui.mouseUp()
    return


def foto(path_name, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(path_name)


def find_link_i():
    pos_i = wait_and_stop_img(name_img='img/everything/info1.png')
    return pos_i


def open_taverna():
    """Открыть таверну"""
    taverna = locCenterImg('img/energy/link_taverna.png')
    if taverna:
        sleep(1)
        taverna = locCenterImg('img/energy/link_taverna.png')
        Mouse.move(pos=taverna, speed=1)
        return taverna
    else:
        pos = find_link_i()
        x, y = pos
        x += 70
        y += 140
        pos = x, y
        Mouse.move_to_click(pos_click=pos, speed=0.2)
        taverna = locCenterImg('img/energy/link_taverna.png')
        while not taverna:
            sleep(0.1)
            taverna = locCenterImg('img/energy/link_taverna.png')
        sleep(1)
        taverna = locCenterImg('img/energy/link_taverna.png')
        Mouse.move(pos=taverna, speed=1)
        return taverna


def push_close():
    it = 0
    my_print_to_file('fun.push_close')
    close = find.find_close()
    while not close:
        it += 0.2
        sleep(0.1)
        close = find.find_close()
        if it == int:
            my_print_to_file("поиск close")
    if close:
        my_print_to_file(f'close = {close}')
        Mouse.move_to_click(pos_click=close, speed=0.1)


def push_close_all_():
    # print('def "fun.push_close_all_"')
    close = find.find_close()
    # print(close, 'close')
    while close:
        close_popup_window()
        push_close()
        sleep(1)
        close = find.find_close()
        # print("цикл close")


def close_popup_window():
    print('def "fun.close_popup_window"')
    knob = find_img.find_knob()
    cancel = find_img.find_cancel()
    if knob:
        sleep(1)
        knob = find_img.find_knob()
        print("снять галочку")
        Mouse.move_to_click(pos_click=knob, speed=1)
    if cancel:
        sleep(1)
        cancel = find_img.find_cancel()
        print('нажал отменить')
        Mouse.move_to_click(pos_click=cancel, speed=1)


def wait_close(txt):
    """Ждет появления"""
    if txt:
        pass
        # print('fun.wait_close', txt)
    it = 0
    close = find.find_close()
    while not close and it < 3:
        sleep(1)
        it += 1
        close = find.find_close()
    sleep(0.2)
    close = find.find_close()
    return close


def cancel_or_knob():
    print('fun.cancel_or_knob')
    it = 0
    cancel = find_img.find_cancel()
    knob = find_img.find_knob()
    while not cancel and not knob and it < 2:
        it += 0.2
        # print(cancel, '= cancel', knob, '= knob')
        sleep(0.1)
        cancel = find_img.find_cancel()
        knob = find_img.find_knob()
    if cancel:
        sleep(0.1)
        cancel = find_img.find_cancel()
        Mouse.move_to_click(pos_click=cancel, speed=0)
    if knob:
        sleep(0.1)
        knob = find_img.find_knob()
        Mouse.move_to_click(pos_click=knob, speed=0)
    close = wait_close('cancel_or_knob')
    return close


def selection_hero(*, show_name=True):
    gavril = locCenterImg('img/hero/h_gavril.png')
    gadya = locCenterImg('img/hero/h_gadya.png')
    veles = locCenterImg('img/hero/h_veles.png')
    mara = locCenterImg('img/hero/h_mara.png')
    if gavril:
        if show_name:
            print(m_t.tc_yellow('         Гаврил'))
        hero = 'Gavr'
        her.Active.hero_activ = her.Gavr
    elif gadya:
        if show_name:
            print(m_t.tc_yellow('         Гадя'))
        hero = 'Gadya'
        her.Active.hero_activ = her.Gady
    elif veles:
        if show_name:
            print(m_t.tc_yellow('         Велес'))
        hero = 'Veles'
        her.Active.hero_activ = her.Veles
    elif mara:
        if show_name:
            print(m_t.tc_yellow('         Марьяна'))
        hero = 'Mara'
        her.Active.hero_activ = her.Mara
    else:
        print(m_t.tc_red('Невозможно опознать героя(('))
        hero = None
        her.Active.hero_activ = None

    return hero


def to_fountain():
    fountain1 = locCenterImg('img/to_fountain_from_houses.png')
    fountain2 = locCenterImg('img/to_fountain_from_pier.png')
    if fountain1:
        print('от домов к фонтану')
        Mouse.move_to_click(pos_click=fountain1, speed=0)
    if fountain2:
        print('от пристани к фонтану')
        Mouse.move_to_click(pos_click=fountain2, speed=0)
    else:
        print('у фонтана')


def in_battle(par_conf, pos_i):
    my_print_to_file('in_battle')
    # print('fun.in_battle')
    skip_battle = locCenterImg('img/everything/skip_battle.png', par_conf)
    my_print_to_file(f'skip_battle = {skip_battle}')
    if skip_battle:
        call_pet(pos_i)
        my_print_to_file('пропускаем бой')
        mouse_move_to_click(skip_battle, 0.2)

        return 1


def call_pet(pos_i):
    # print('call_pet')
    if pos_i:
        x, y = pos_i
        y += 410
        pos_pet = x, y  # позиция пета
        Mouse.left_click(pos=pos_pet)  # нажать на пета
        # melodi_pet()


def scroll_down():
    pos = locCenterImg(name_img='img/arena/scroll_down.png', confidence=0.98, region=(550, 550, 750, 750))
    while not pos:
        sleep(0.5)
        pos = locCenterImg(name_img='img/arena/scroll_down.png', confidence=0.98, region=(550, 550, 750, 750))
    sleep(0.1)
    return pos


def go_in_hall_glory():
    my_print_to_file('go_in_hall_glory')

    link_in_hall_glory = locCenterImg('img/arena/link_in_hall_glory.png', 0.98)
    hall_glory = locCenterImg('img/arena/hall_glory.png', 0.999)
    close = find_img.find_close()

    my_print_to_file(f'link_in_hall_glory = {link_in_hall_glory}')
    my_print_to_file(f'hall_glory = {hall_glory}')
    my_print_to_file(f'close = {close}')

    while not link_in_hall_glory:
        if close:
            push_close()
            sleep(3)
        elif hall_glory:
            my_print_to_file(f'hall_glory = {hall_glory}')
            Mouse.move_to_click(pos_click=hall_glory, speed=0.2)
            link_in_hall_glory = locCenterImg('img/arena/link_in_hall_glory.png', 0.98)
            while not link_in_hall_glory:
                link_in_hall_glory = locCenterImg('img/arena/link_in_hall_glory.png', 0.98)
        link_in_hall_glory = locCenterImg('img/arena/link_in_hall_glory.png', 0.98)
        hall_glory = locCenterImg('img/arena/hall_glory.png', 0.999)
        close = find_img.find_close()


def pos_clan(show_i=True):
    pos = find_link_i()
    if show_i:
        Mouse.move(pos=pos, speed=1)
    x, y = pos
    y -= 25
    x += 45
    pos_click = x, y
    # move_to_click(pos_click, 0)
    return x, y


def get_isolation_end_date():
    day_now = datetime.datetime.now()
    quarantine = day_now + datetime.timedelta(days=10)
    print(quarantine)
    return quarantine


def verifi_isolation(date_end_isolation):
    """
    return: int
    """
    day_now = datetime.datetime.now()
    if type(date_end_isolation) == type(day_now):
        time_diff = date_end_isolation - day_now
        days_left = time_diff.days
        if days_left < 0:
            days_left = 0
    else:
        days_left = 0
    return days_left


def return_days_transformation(days):
    days_des = days // 10  # остается десятков
    days_ed = days % 10  # остается единиц

    if days_ed == 1 and days_des != 1:  #
        return f'{days} день'
    elif days_ed in [2, 3, 4] and days_des != 1:  #
        return f'{days} дня'
    elif days_des == 1:  #
        return f'{days} дней'
    elif days_ed in [0, 5, 6, 7, 8, 9] and days_des != 1:  #
        return f'{days} дней'


def check_work_completed():
    work_completed = locCenterImg('img/everything/work_completed.png')
    close = locCenterImg('img/everything/close.png')
    if work_completed:
        Mouse.move_to_click(pos_click=close, z_p_k=1)


def extraction_digit(*, item):
    digit = int(''.join(c if c.isdigit() else ' ' for c in item))
    return digit
