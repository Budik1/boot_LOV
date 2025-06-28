import pyautogui
from playsound3 import playsound
from time import sleep

from pyexpat.errors import messages

import fun
import baza_dannyx as b_d
import creating_photo
import heroes
import solid_memory
import my_color_text as m_t
from heroes import Hero, Active

region_events = 504, 389, 300, 200
par_conf = 0.88


def define_lvl():
    lvl_list = b_d.lvl_list

    for value in lvl_list:
        fail_name = f'img/energy/lvl/{value}lvl.png'
        lvl = fun.locCenterImg(fail_name, confidence=0.92)
        if lvl:
            print(f'уровень героя {value}')
            return value
    else:
        print("уровень не определен")
        return None


def foto_pos():
    fun.foto('img/tests/test_foto.png', region_events)


def verify_energy(q_it):
    """
    :param q_it: количество циклов ожидания
    :return: Point / False
    """
    it = 0
    not_energy = fun.locCenterImg('img/energy/not_energy.png', confidence=0.9)  # ??
    while not not_energy and it < q_it:
        it += 1
        sleep(1)
        not_energy = fun.locCenterImg('img/energy/not_energy.png', confidence=0.9)
    return not_energy


def task_selection_dict(tasks):
    variant_ = None
    conf = 0.99
    while not variant_:
        for img in tasks:
            task_pos = fun.locCenterImg(tasks[img], confidence=conf)
            if task_pos:
                vers_in_print = '' if conf == 0.99 else m_t.tc_red(f', conf={conf}')
                # print(f"{tasks[img]}, conf={conf}")
                en = fun.extraction_digit(item=tasks[img])
                # print(f"{tasks[img]}{vers_in_print} {en} потрачено")
                # task_message = f"{vers_in_print} {en} потрачено"
                # print('проверь наличие и место')
                x, y = task_pos
                y -= 40
                click_task = x, y
                # fun.move_to_click(task_pos, 2)
                pyautogui.moveTo(click_task)
                return click_task, en
        conf -= 0.001
        print(f"поиск вариантов, conf ={conf}")
        if conf <= 0.98:
            click_task = None
            creating_photo.creating_photo_tasks()
            print(m_t.tc_magenta('задание не найдено, обнови данные'))
            print(m_t.tc_magenta('заготовки тут "img/full_t/"'))
            playsound("muz/fresh.mp3")
            return click_task, None


def energy_gold():
    close = fun.locCenterImg('img/everything/close.png', confidence=0.89)
    if close:
        fun.mouse_move_to_click(close, 0)
    # опознать героя
    hero = fun.selection_hero()
    while not hero:
        close = fun.locCenterImg('img/everything/close.png', confidence=0.89)
        if close:
            fun.mouse_move_to_click(close, 0)
        hero = fun.selection_hero()
    tasks_ = Hero.get_task_gold(Active.hero_activ)
    # print(Hero.get_task_gold(Active.hero_activ))
    energy_ = True
    while energy_:
        q_call_pet = 0
        review = 0
        fun.open_taverna()
        variant, value_en = task_selection_dict(tasks_)

        if not variant:
            print('нет подходящих вариантов ))')
            return
        else:
            fun.mouse_move_to_click(variant, 0.5)
            x, y = variant
            x -= 200
            y -= 100
            pos_g = x, y
            pyautogui.moveTo(pos_g, duration=0.25)
            no_energy = verify_energy(4)
            if no_energy:
                print(m_t.tc_red('         NO ENERGY !!!'))
                energy_ = False
                fun.mouse_move_to_click(fun.wait_close('NO ENERGY !!!'), 0.3)
                return hero
            else:
                Hero.set_en_now(Active.hero_activ, value=value_en)
                Hero.set_energy_count_all(Active.hero_activ, value=value_en)
                print(f'потрачено сейчас {value_en},'
                      f' сегодня {Hero.get_en_now(Active.hero_activ)} из {Hero.get_en_sum(Active.hero_activ)},'
                      f'всего {Hero.get_energy_count_all(Active.hero_activ)}')
                solid_memory.save_to_file(info=False)
                pos_i = fun.find_link_i()
                taverna = fun.locCenterImg('img/energy/link_taverna.png', confidence=0.9)
                while taverna:
                    sleep(1)
                    taverna = fun.locCenterImg('img/energy/link_taverna.png', confidence=0.9)
                link_battle_end = fun.locCenterImg('img/link_battle_end.png', confidence=0.9)
                while not link_battle_end:
                    awake_friend = pyautogui.locateCenterOnScreen('img/energy/_awake_friend.png', confidence=par_conf,
                                                                  region=region_events)
                    popup_xp = pyautogui.locateCenterOnScreen('img/energy/_popup_xp.png', confidence=par_conf,
                                                              region=region_events)
                    invite_friends = pyautogui.locateCenterOnScreen('img/energy/_invite_friends.png',
                                                                    confidence=par_conf,
                                                                    region=region_events)
                    treasure = pyautogui.locateCenterOnScreen('img/energy/_treasure.png', confidence=par_conf,
                                                              region=region_events)
                    yes_go = pyautogui.locateCenterOnScreen('img/energy/_yes_go.png', confidence=par_conf,
                                                            region=region_events)
                    if review == 0:
                        if popup_xp:  # я учту это
                            review = 1
                            print(m_t.tc_cyan('         я учту это'))
                            sleep(0.2)
                            popup_xp = pyautogui.locateCenterOnScreen('img/energy/_popup_xp.png', confidence=par_conf,
                                                                      region=region_events)
                            fun.mouse_move_to_click(popup_xp, 0.1)
                            close_img_ = fun.wait_close('я учту это')
                            while not close_img_:
                                close_img_ = fun.wait_close('я учту это')
                            fun.mouse_move_to_click(close_img_, 0)
                        if invite_friends:  # Пригласить друга
                            review = 1
                            print(m_t.tc_cyan('         Пригласить друга'))
                            fun.mouse_move_to_click(invite_friends, 0.1)
                            fun.mouse_move_to_click(fun.cancel_or_knob(), 0)
                            close = fun.wait_close('Пригласить друга')
                            if close:
                                fun.mouse_move_to_click(close, 0)
                        if treasure:
                            review = 1
                            print(m_t.tc_cyan('         Искать клад'))
                            sleep(0.2)
                            treasure = pyautogui.locateCenterOnScreen('img/energy/_treasure.png', confidence=par_conf,
                                                                      region=region_events)
                            fun.mouse_move_to_click(treasure, 0.1)
                            fun.mouse_move_to_click(fun.cancel_or_knob(), 0)
                        if yes_go:
                            review = 1
                            print(m_t.tc_cyan('         Да, поехали'))
                            sleep(0.2)
                            yes_go = pyautogui.locateCenterOnScreen('img/energy/_yes_go.png', confidence=par_conf,
                                                                    region=region_events)
                            fun.mouse_move_to_click(yes_go, 0.1)
                        if awake_friend:
                            review = 1
                            print(m_t.tc_cyan('         Разбудить друга'))
                            awake_friend = pyautogui.locateCenterOnScreen('img/energy/_awake_friend.png',
                                                                          confidence=par_conf, region=region_events)
                            fun.mouse_move_to_click(awake_friend, 0.1)
                            fun.mouse_move_to_click(fun.cancel_or_knob(), 0)
                            close = fun.wait_close('Разбудить друга')
                            if close:
                                fun.mouse_move_to_click(close, 0)
                    skip_battle = fun.locCenterImg('img/everything/skip_battle.png', confidence=par_conf)
                    if skip_battle and q_call_pet == 0:
                        q_call_pet = 1
                        fun.call_pet(pos_i)
                    link_battle_end = fun.locCenterImg('img/link_battle_end.png', confidence=0.9)
                link_battle_end = fun.wait_and_stop_img(name_img='img/link_battle_end.png')
                pyautogui.moveTo(link_battle_end, duration=0.25)
                if link_battle_end:
                    link_victory = fun.locCenterImg('img/energy/rezult_vick.png', confidence=0.9)
                    # print(f'Сегодня потрачено {Hero.get_en_now(Active.hero_activ)} из '
                    #       f'{Hero.get_en_sum(Active.hero_activ)} доступных')
                    if link_victory:
                        # print("Победа")
                        fun.melody_vic()
                    else:
                        print("Неудача")
                        fun.melody_fail()

                close_img = fun.wait_and_stop_img(name_img='img/everything/close.png', param_confidence=0.85)
                # закрыть сражение
                fun.mouse_move_to_click(close_img, 0)
                sleep(1)
                # сражение закрыто.
                close = fun.wait_close('ожидание всплывающего события')
                # если всплывает "закрыть"
                if close:
                    c_or_k = fun.cancel_or_knob()  # ищем "кнопку" или "отменить" и если есть нажимаем
                    if c_or_k:  # нажимаем 'close'
                        fun.mouse_move_to_click(c_or_k, 0)
                    else:  # если нет -> жмем 'close'
                        fun.mouse_move_to_click(close, 0)

                    close = fun.wait_close('ожидание всплывающего события')
                    # если всплывает "закрыть"
                    if close:
                        c_or_k = fun.cancel_or_knob()  # ищем "кнопку" или "отменить" и если есть нажимаем
                        if c_or_k:  # нажимаем 'close'
                            fun.mouse_move_to_click(c_or_k, 0)
                        else:  # если нет -> жмем 'close'
                            fun.mouse_move_to_click(close, 0)
                sleep(1)

            # energy_ = 0 # для выполнения одного цикла
            if energy_ == 0:
                print('задание завершено')
            else:
                print()
                print('следующее задание')


def energy_xp():

    close = fun.locCenterImg('img/everything/close.png', confidence=0.89)
    if close:
        fun.mouse_move_to_click(close, 0)
    # опознать героя
    hero = fun.selection_hero()
    while not hero:
        close = fun.locCenterImg('img/everything/close.png', confidence=0.89)
        if close:
            fun.mouse_move_to_click(close, 0)
        hero = fun.selection_hero()
    # получить список его заданий
    if hero:
        print(f"имя {Hero.get_name(Active.hero_activ)}")
        tasks_ = Hero.get_task_xp(Active.hero_activ)
        wilt = fun.verifi_isolation(Hero.get_isolation_end_date(Active.hero_activ))
    else:
        tasks_ = None
        wilt = None
        print('сделай что нибудь, герой не опознан!!')
        return
    if wilt:
        print(f'Ты слишком слаб, что-бы набирать опыт. Попробуй через {fun.return_days_transformation(wilt)}')
        print(' Перевод energy_gold')
        energy_gold()
    energy_ = True
    while energy_:
        review = 0
        q_call_pet = 0
        fun.open_taverna()
        variant, value_en = task_selection_dict(tasks_)
        fun.mouse_move_to_click(variant, 0.5)  # автомат
        x, y = variant
        x -= 200
        y -= 100
        pos_g = x, y
        pyautogui.moveTo(pos_g, duration=0.25)
        no_energy = verify_energy(4)
        if no_energy:
            print(m_t.tc_red('         NO ENERGY !!!'))
            energy_ = None
            fun.mouse_move_to_click(fun.wait_close('NO ENERGY !!!'), 0.3)
            return hero

        else:
            Hero.set_en_now(Active.hero_activ, value=value_en)
            Hero.set_energy_count_all(Active.hero_activ, value=value_en)
            print(f'потрачено сейчас {value_en},'
                  f' сегодня {Hero.get_en_now(Active.hero_activ)} из {Hero.get_en_sum(Active.hero_activ)},'
                  f'всего {Hero.get_energy_count_all(Active.hero_activ)}')
            solid_memory.save_to_file(info=False)
            pos_i = fun.find_link_i()
            taverna = fun.locCenterImg('img/energy/link_taverna.png', confidence=0.9)
            while taverna:
                sleep(1)
                taverna = fun.locCenterImg('img/energy/link_taverna.png', confidence=0.9)
            link_battle_end = fun.locCenterImg('img/link_battle_end.png', confidence=0.9)
            while not link_battle_end:
                awake_friend = pyautogui.locateCenterOnScreen('img/energy/_awake_friend.png', confidence=par_conf,
                                                              region=region_events)
                popup_xp = pyautogui.locateCenterOnScreen('img/energy/_popup_xp.png', confidence=par_conf,
                                                          region=region_events)
                invite_friends = pyautogui.locateCenterOnScreen('img/energy/_invite_friends.png', confidence=par_conf,
                                                                region=region_events)
                treasure = pyautogui.locateCenterOnScreen('img/energy/_treasure.png', confidence=par_conf,
                                                          region=region_events)
                yes_go = pyautogui.locateCenterOnScreen('img/energy/_yes_go.png', confidence=par_conf,
                                                        region=region_events)
                if review == 0:
                    if popup_xp:
                        review = 1
                        print(m_t.tc_cyan('         я учту это'))
                        sleep(0.2)
                        popup_xp = pyautogui.locateCenterOnScreen('img/energy/_popup_xp.png', confidence=par_conf,
                                                                  region=region_events)
                        fun.mouse_move_to_click(popup_xp, 0.1)
                        fun.mouse_move_to_click(fun.wait_close('я учту это'), 0)
                    if invite_friends:
                        review = 1
                        print(m_t.tc_cyan('         Пригласить друга'))
                        fun.mouse_move_to_click(invite_friends, 0.1)
                        fun.mouse_move_to_click(fun.cancel_or_knob(), 0)
                        close = fun.wait_close('Пригласить друга')
                        if close:
                            fun.mouse_move_to_click(close, 0)
                    if treasure:
                        review = 1
                        print(m_t.tc_cyan('         Искать клад'))
                        sleep(0.2)
                        treasure = pyautogui.locateCenterOnScreen('img/energy/_treasure.png', confidence=par_conf,
                                                                  region=region_events)
                        fun.mouse_move_to_click(treasure, 0.1)
                        fun.mouse_move_to_click(fun.cancel_or_knob(), 0)
                    if yes_go:
                        review = 1
                        print(m_t.tc_cyan('         Да, поехали'))
                        sleep(0.2)
                        yes_go = pyautogui.locateCenterOnScreen('img/energy/_yes_go.png', confidence=par_conf,
                                                                region=region_events)
                        fun.mouse_move_to_click(yes_go, 0.1)
                    if awake_friend:
                        review = 1
                        print(m_t.tc_cyan('Разбудить друга'))
                        awake_friend = pyautogui.locateCenterOnScreen('img/energy/_awake_friend.png',
                                                                      confidence=par_conf, region=region_events)
                        fun.mouse_move_to_click(awake_friend, 0.1)
                        fun.mouse_move_to_click(fun.cancel_or_knob(), 0)
                        close = fun.wait_close('Разбудить друга')
                        if close:
                            fun.mouse_move_to_click(close, 0)
                skip_battle = fun.locCenterImg('img/everything/skip_battle.png', confidence=par_conf)
                if skip_battle and q_call_pet == 0:
                    q_call_pet = 1
                    fun.call_pet(pos_i)
                link_battle_end = fun.locCenterImg('img/link_battle_end.png', confidence=0.9)

            link_battle_end = fun.wait_and_stop_img(name_img='img/link_battle_end.png')
            pyautogui.moveTo(link_battle_end, duration=0.25)

            if link_battle_end:
                link_victory = fun.locCenterImg('img/energy/rezult_vick.png', confidence=0.9)
                # print(f'Сегодня потрачено {Hero.get_en_now(Active.hero_activ)} из '
                #       f'{Hero.get_en_sum(Active.hero_activ)} доступных')
                if link_victory:
                    # print("Победа")
                    fun.melody_vic()
                else:
                    print("Неудача")
                    fun.melody_fail()
                    Hero.set_isolation_end_date(Active.hero_activ)
                    energy_gold()

            close_img = fun.wait_and_stop_img(name_img='img/everything/close.png', param_confidence=0.85)
            # закрыть сражение
            fun.mouse_move_to_click(close_img, 0)
            sleep(1)
            # сражение закрыто.
            close = fun.wait_close('ожидание всплывающего события')
            # если всплывает "закрыть"
            if close:
                c_o_k = fun.cancel_or_knob()  # ищем "кнопку" или "отменить" и если есть нажимаем
                if c_o_k:  # нажимаем 'close'
                    fun.mouse_move_to_click(c_o_k, 0)
                else:  # если нет -> жмем 'close'
                    fun.mouse_move_to_click(close, 0)

                close = fun.wait_close('ожидание всплывающего события')
                # если всплывает "закрыть"
                if close:
                    c_o_k = fun.cancel_or_knob()  # ищем "кнопку" или "отменить" и если есть нажимаем
                    if c_o_k:  # нажимаем 'close'
                        fun.mouse_move_to_click(c_o_k, 0)
                    else:  # если нет -> жмем 'close'
                        fun.mouse_move_to_click(close, 0)
            sleep(1)

        if energy_ == 0:
            print()
        else:
            print()
            print('следующее задание')
        # energy_ = 0 # для выполнения одного цикла
