# from playsound3 import playsound
from time import sleep

import find_img
import fun
import sounds
import creating_photo
import solid_memory
import complex_phrases
import baza_dannyx as b_d
import my_color_text as m_t
from heroes import Hero, Active

# import heroes

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
                fun.mouse_move(pos=click_task)
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


def event_passage(*, review):
    awake_friend = fun.locCenterImg(name_img='img/energy/_awake_friend.png', confidence=par_conf, region=region_events)
    popup_xp = fun.locCenterImg(name_img='img/energy/_popup_xp.png', confidence=par_conf, region=region_events)
    invite_friends = fun.locCenterImg(name_img='img/energy/_invite_friends.png', confidence=par_conf,
                                      region=region_events)
    treasure = fun.locCenterImg(name_img='img/energy/_treasure.png', confidence=par_conf, region=region_events)
    yes_go = fun.locCenterImg(name_img='img/energy/_yes_go.png', confidence=par_conf, region=region_events)
    if review == 0:
        if popup_xp:  # я учту это
            review = 1
            print(m_t.tc_cyan('         я учту это'))
            sleep(0.2)
            popup_xp = fun.locCenterImg(name_img='img/energy/_popup_xp.png', confidence=par_conf,
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
            treasure = fun.locCenterImg(name_img='img/energy/_treasure.png', confidence=par_conf, region=region_events)
            fun.mouse_move_to_click(treasure, 0.1)
            fun.mouse_move_to_click(fun.cancel_or_knob(), 0)
        if yes_go:
            review = 1
            print(m_t.tc_cyan('         Да, поехали'))
            sleep(0.2)
            yes_go = fun.locCenterImg(name_img='img/energy/_yes_go.png', confidence=par_conf, region=region_events)
            fun.mouse_move_to_click(yes_go, 0.1)
        if awake_friend:
            review = 1
            print(m_t.tc_cyan('         Разбудить друга'))
            awake_friend = fun.locCenterImg(name_img='img/energy/_awake_friend.png', confidence=par_conf,
                                            region=region_events)
            fun.mouse_move_to_click(awake_friend, 0.1)
            fun.mouse_move_to_click(fun.cancel_or_knob(), 0)
            close = fun.wait_close('Разбудить друга')
            if close:
                fun.mouse_move_to_click(close, 0)
    return review


def get_task(*, target):
    tasks_ = None
    if target == 'gold_task':
        tasks_ = Hero.get_task_gold(Active.hero_activ)
    elif target == 'xp_task':
        tasks_ = Hero.get_task_xp(Active.hero_activ)
    else:
        print('не понятно что делать, лучше полежу)))')
    return tasks_

def info_energy(*, value_energy: int):
    """
    :param value_energy: количество потраченной энергии сейчас
    :return: строка
    """
    return complex_phrases.about_energy_costs_for_the_task(value_energy=value_energy)


def energy(*, target_task):
    # 'gold_task' 'xp_task'
    # если что-то открыто - закрыть и выйти на главный экран
    close = find_img.find_close()
    if close:
        fun.mouse_move_to_click(close, 0)
    # опознать героя
    hero = fun.selection_hero()
    while not hero:
        close = find_img.find_close()
        if close:
            fun.mouse_move_to_click(close, 0)
        hero = fun.selection_hero()
    # получить список его заданий
    tasks_ = get_task(target=target_task)
    if not tasks_:
        return
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
            fun.mouse_move(pos=pos_g, speed=0.25)
            no_energy = verify_energy(q_it=4)
            if no_energy:
                print(m_t.tc_red('         NO ENERGY !!!'))
                fun.mouse_move_to_click(fun.wait_close('NO ENERGY !!!'), 0.3)
                return hero
            else:
                Hero.ap_en_now(Active.hero_activ, value=value_en)
                Hero.ap_energy_count_all(Active.hero_activ, value=value_en)
                print(info_energy(value_energy=value_en))
                solid_memory.save_to_file(info=False)
                pos_i = fun.find_link_i()
                taverna = find_img.find_link_taverna()
                while taverna:
                    sleep(1)
                    taverna = find_img.find_link_taverna()
                link_battle_end = find_img.find_link_battle_end()
                while not link_battle_end:
                    event_passage(review=review)
                    skip_battle = fun.locCenterImg('img/everything/skip_battle.png', confidence=par_conf)
                    if skip_battle and q_call_pet == 0:
                        q_call_pet = 1
                        fun.call_pet(pos_i)
                    link_battle_end = find_img.find_link_battle_end()
                link_battle_end = fun.wait_and_stop_img(name_img='img/link_battle_end.png')
                fun.mouse_move(pos=link_battle_end, speed=0.25)
                if link_battle_end:
                    link_victory = fun.locCenterImg('img/energy/rezult_vick.png', confidence=0.9)
                    # print(f'Сегодня потрачено {Hero.get_en_now(Active.hero_activ)} из '
                    #       f'{Hero.get_en_sum(Active.hero_activ)} доступных')
                    if link_victory:
                        # print("Победа")
                        sounds.melody_vic()
                    else:
                        print("Неудача")
                        sounds.melody_fail()

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
