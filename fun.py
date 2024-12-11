from playsound3 import playsound
import pyautogui
from time import sleep
import datetime
import my_text as m_t

# init()
log = 1


def melodi_vic():
    playsound("muz/success.mp3")


def melodi_feil():
    playsound('muz/feil.mp3')


def o_in_oo(symbol):
    if 0 <= symbol <= 9:
        return str(f'0{symbol}')
    else:
        return str(symbol)


def locCenterImg(name_img, confidence=0.9):
    pos_img = pyautogui.locateCenterOnScreen(name_img, confidence=confidence)
    return pos_img


def wait_and_stop_img(name_img, param_confidence=0.85):
    """    Ждет появление и фиксацию картинки    """
    # lookin_image = pyautogui.locateCenterOnScreen(path_and_name_img, confidence=param_confidence)

    img_1 = locCenterImg(name_img, param_confidence)
    sleep(0.3)
    img_2 = locCenterImg(name_img, param_confidence)
    while not img_1 or img_1 != img_2:
        if img_1 or img_2:
            img_1 = locCenterImg(name_img, param_confidence)
            sleep(0.3)
            img_2 = locCenterImg(name_img, param_confidence)
        else:
            img_1 = locCenterImg(name_img, param_confidence)
            sleep(0.3)
            img_2 = locCenterImg(name_img, param_confidence)
    if img_1 == img_2 and img_1:
        return img_2


def attack_guru():
    name = selection_hero()
    if name == 'Gavr' or name == 'Gadya' or name == 'Veles' or name == 'Mara':
        # переход на экран 'ученики и наставники'
        # guru = pyautogui.locateCenterOnScreen('img/city/guru.png', confidence=0.9)
        guru = locCenterImg('img/city/guru.png', 0.9)
        # print('guru', guru)
        move_to_click(guru, 0.2)
        # подтверждение открытия окна "наставник - ученик"
        wait_and_stop_img('img/city/guru_and_students.png')
        # переход на экран атаки
        attack_guru_img1 = wait_and_stop_img("img/city/attak_guru.png")
        move_to_click(attack_guru_img1, 0.2)
        # нажать кнопку "атаковать"
        in_battle_img = wait_and_stop_img('img/arena/in_battle.png')
        move_to_click(in_battle_img, 0.2)
        # нажать кнопку "закрыть"
        close_img = wait_and_stop_img('img/everything/close.png', 0.85)
        move_to_click(close_img, 0.1)
        return name
    else:
        pass


def click_update():
    update = locCenterImg('img/kv/update.png', 0.9)
    sleep(0.2)
    update_1 = locCenterImg('img/kv/update.png', 0.9)
    while not update or update != update_1:
        update = locCenterImg('img/kv/update.png', 0.9)
        sleep(0.2)
        update_1 = locCenterImg('img/kv/update.png', 0.9)
    # print("обновить", update)
    move_to_click(update, 0.1)
    x, y = update
    x -= 25
    y += 25
    pyautogui.moveTo(x, y)


def my_print_to_file(text):
    if log == 1:
        time_now_value = time_now()
        date = date_now()
        file_name = date + ".txt"
        file = open('log/' + file_name, 'a+', encoding='utf-8')
        print(time_now_value, text, file=file)
        file.close()  # закрыть файл после работы с ним.


def time_now():
    now = datetime.datetime.now()
    # '%Y-%m-%d_%H:%M:%S' '%Y-%m-%d %H°%M\'\'%S\''
    time_now_ = (now.strftime('%Y-%m-%d %H:%M:%S'))
    # date = (now.strftime('%Y-%m-%d'))
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


def move_to_click(pos_click: tuple, z_p_k: float):
    """
    Поместить указатель мыши по координатам и кликнуть, учитывая задержку.
    :param pos_click: Point
    :param z_p_k: задержка перед кликом(float)
    :return: None
    """

    my_print_to_file('move_to_click')
    sleep(0.3)
    pyautogui.moveTo(pos_click, duration=0.5)  # , tween=pyautogui.easeInOutQuad
    # print('должен быть клик')
    sleep(z_p_k)
    pyautogui.hotkey('Ctrl')
    if pos_click:
        pyautogui.click(pos_click)
    else:
        print("некуда кликать")
    sleep(0.18)


def foto(path_name, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(path_name)


def find_link_i():
    pos_i = wait_and_stop_img('img/everything/info1.png')
    return pos_i


def open_taverna():
    """Открыть таверну"""
    taverna = locCenterImg('img/energy/link_taverna.png')
    if taverna:
        sleep(1)
        taverna = locCenterImg('img/energy/link_taverna.png')
        pyautogui.moveTo(taverna, duration=1)
        return taverna
    else:
        pos = find_link_i()
        x, y = pos
        x += 70
        y += 140
        pos = x, y
        move_to_click(pos, 0.2)
        taverna = locCenterImg('img/energy/link_taverna.png')
        while not taverna:
            sleep(0.1)
            taverna = locCenterImg('img/energy/link_taverna.png')
        sleep(1)
        taverna = locCenterImg('img/energy/link_taverna.png')
        pyautogui.moveTo(taverna, duration=1)
        return taverna


def push_close():
    it = 0
    my_print_to_file('fun.push_close')
    close = locCenterImg('img/everything/close.png', 0.89)
    while not close:
        it += 0.2
        sleep(0.1)
        close = locCenterImg('img/everything/close.png', 0.89)
        if it == int:
            my_print_to_file("поиск close")
    if close:
        my_print_to_file(f'close = {close}')
        move_to_click(close, 0.1)


def push_close_all_():
    # print('def "fun.push_close_all_"')
    close = locCenterImg('img/everything/close.png', 0.89)
    # print(close, 'close')
    while close:
        close_popup_window()
        push_close()
        sleep(1)
        close = locCenterImg('img/everything/close.png', 0.89)
        # print("цикл close")


def close_popup_window():
    print('def "fun.close_popup_window"')
    knob = locCenterImg('img/everything/knob.png', 0.89)
    cancel = locCenterImg('img/everything/cancel.png', 0.89)
    if knob:
        sleep(1)
        knob = locCenterImg('img/everything/knob.png', 0.89)
        print("снять галочку")
        move_to_click(knob, 1)
    if cancel:
        sleep(1)
        cancel = locCenterImg('img/cancel.png', 0.89)
        print('нажал отменить')
        move_to_click(cancel, 1)


def exit_to_fountain():
    # print('fun.exit_to_fountain')
    img_to_fountain = locCenterImg('img/to_fountain_from_houses.png')
    while not img_to_fountain:
        sleep(1)
        print(img_to_fountain, 'to_fountain')
        img_to_fountain = locCenterImg('img/to_fountain_from_houses.png', 0.85)

    move_to_click(img_to_fountain, 0.5)


def wait_close(txt):
    """Ждет появления"""
    if txt:
        pass
        # print('fun.wait_close', txt)
    it = 0
    close = locCenterImg('img/everything/close.png', 0.89)
    while not close and it < 3:
        sleep(1)
        it += 1
        close = locCenterImg('img/everything/close.png', 0.89)
    sleep(0.2)
    close = locCenterImg('img/everything/close.png', 0.89)
    return close


def cancel_or_knob():
    print('fun.cancel_or_knob')
    it = 0
    cancel = locCenterImg('img/everything/cancel.png', 0.89)
    knob = locCenterImg('img/everything/knob.png', 0.89)
    while not cancel and not knob and it < 2:
        it += 0.2
        # print(cancel, '= cancel', knob, '= knob')
        sleep(0.1)
        cancel = locCenterImg('img/everything/cancel.png', 0.89)
        knob = locCenterImg('img/everything/knob.png', 0.89)
    if cancel:
        sleep(0.1)
        cancel = locCenterImg('img/everything/cancel.png', 0.89)
        move_to_click(cancel, 0)
    if knob:
        sleep(0.1)
        knob = locCenterImg('img/everything/knob.png', 0.89)
        move_to_click(knob, 0)
    close = wait_close('cancel_or_knob')
    return close


def selection_hero():
    gavril = locCenterImg('img/hero/h_gavril.png')
    gadya = locCenterImg('img/hero/h_gadya.png')
    veles = locCenterImg('img/hero/h_veles.png')
    mara = locCenterImg('img/hero/h_mara.png')
    if gavril:
        print(m_t.text_yellow('         Гаврил'))
        hero = 'Gavr'
    elif gadya:
        print(m_t.text_yellow('         Гадя'))
        hero = 'Gadya'
    elif veles:
        print(m_t.text_yellow('         Велес'))
        hero = 'Veles'
    elif mara:
        print(m_t.text_yellow('         Марьяна'))
        hero = 'Mara'
    else:
        print(m_t.text_red('Невозможно опознать героя(('))
        hero = None

    return hero


def to_fountain():
    fountain1 = locCenterImg('img/to_fountain_from_houses.png')
    fountain2 = locCenterImg('img/to_fountain_from_pier.png')
    if fountain1:
        print('от домов к фонтану')
        move_to_click(fountain1, 0)
    if fountain2:
        print('от пристани к фонтану')
        move_to_click(fountain2, 0)
    else:
        print('у фонтана')


def in_battle(par_conf, pos_i):
    my_print_to_file('in_battle')

    skip_battle = locCenterImg('img/everything/skip_battle.png', par_conf)
    my_print_to_file(f'skip_battle = {skip_battle}')
    if skip_battle:
        x, y = pos_i
        y += 410
        pos_pet = x, y  # позиция пета
        pyautogui.click(pos_pet)  # нажать на пета
        my_print_to_file('пропускаем бой')
        move_to_click(skip_battle, 0.2)

        return 1


def scroll_down():
    scroll_down_ = pyautogui.locateCenterOnScreen('img/arena/scroll_down.png', region=(550, 550, 750, 750),
                                                  confidence=0.98)
    while not scroll_down_:
        sleep(0.5)
        scroll_down_ = pyautogui.locateCenterOnScreen('img/arena/scroll_down.png', region=(550, 550, 750, 750),
                                                      confidence=0.98)
    sleep(0.1)
    return scroll_down_


def go_in_hall_glory():
    my_print_to_file('go_in_hall_glory')

    link_in_hall_glory = locCenterImg('img/arena/link_in_hall_glory.png', 0.98)
    hall_glory = locCenterImg('img/arena/hall_glory.png', 0.999)
    close = locCenterImg('img/everything/close.png', 0.89)

    my_print_to_file(f'link_in_hall_glory = {link_in_hall_glory}')
    my_print_to_file(f'hall_glory = {hall_glory}')
    my_print_to_file(f'close = {close}')

    while not link_in_hall_glory:
        if close:
            push_close()
            sleep(3)
        elif hall_glory:
            my_print_to_file(f'hall_glory = {hall_glory}')
            move_to_click(hall_glory, 0.2)
            link_in_hall_glory = locCenterImg('img/arena/link_in_hall_glory.png', 0.98)
            while not link_in_hall_glory:
                link_in_hall_glory = locCenterImg('img/arena/link_in_hall_glory.png', 0.98)
        link_in_hall_glory = locCenterImg('img/arena/link_in_hall_glory.png', 0.98)
        hall_glory = locCenterImg('img/arena/hall_glory.png', 0.999)
        close = locCenterImg('img/everything/close.png', 0.89)
