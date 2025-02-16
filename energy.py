import pyautogui
from playsound3 import playsound
from time import sleep
import fun
import creating_photo
import baza_dannyx as b_d
import my_text as m_t
import heroes as her

region_events = 504, 389, 300, 200
par_conf = 0.88


def foto_pos():
    fun.foto('img/tests/test_foto.png', region_events)


def verify_energy(q_it):
    it = 0
    not_energy = fun.locCenterImg('img/energy/not_energy.png', confidence=0.9)  # ??
    while not not_energy and it < q_it:
        it += 1
        sleep(1)
        not_energy = fun.locCenterImg('img/energy/not_energy.png', confidence=0.9)
    return not_energy


def task_selection(tasks):
    variant_ = None
    conf = 0.99
    while not variant_:
        for img in tasks:
            task_pos = fun.locCenterImg(tasks[img], confidence=conf)
            if task_pos:
                vers_in_print = '' if conf == 0.99 else m_t.text_red(f', conf={conf}')
                # print(f"{tasks[img]}, conf={conf}")
                print(f"{tasks[img]}{vers_in_print}")
                # print('проверь наличие и место')
                x, y = task_pos
                y -= 40
                click_task = x, y
                # fun.move_to_click(task_pos, 2)
                pyautogui.moveTo(click_task)
                return click_task
        conf -= 0.001
        print(f"поиск вариантов, conf ={conf}")
        if conf <= 0.98:
            click_task = None
            creating_photo.creating_photo_tasks()
            print(m_t.text_magenta('задание не найдено, обнови данные'))
            print(m_t.text_magenta('заготовки тут "img/full_t/"'))
            playsound("muz/fresh.mp3")
            return click_task


def energy_gold():
    close = fun.locCenterImg('img/everything/close.png', confidence=0.89)
    if close:
        fun.move_to_click(close, 0)
    # опознать героя
    hero = fun.selection_hero()
    while not hero:
        close = fun.locCenterImg('img/everything/close.png', confidence=0.89)
        if close:
            fun.move_to_click(close, 0)
        hero = fun.selection_hero()
    # получение списка заданий
    print(hero, 'hero')
    if hero == 'Gavr':
        tasks_ = b_d.tasks_gold_gavr
    elif hero == 'Gadya':
        tasks_ = b_d.tasks_gold_v
    elif hero == 'Veles':
        tasks_ = b_d.tasks_gold_vel
    elif hero == 'Mara':
        tasks_ = b_d.tasks_gold_mar
    else:
        tasks_ = None
    print(f'список заданий для {her.Hero.introduce(her.Active.hero_activ)}')
    energy_ = True
    while energy_:
        q_call_pet = 0
        review = 0
        fun.open_taverna()
        variant = task_selection(tasks_)
        if not variant:
            return
        else:
            fun.move_to_click(variant, 0.5)
            x, y = variant
            x -= 200
            y -= 100
            pos_g = x, y
            pyautogui.moveTo(pos_g, duration=0.25)
            no_energy = verify_energy(4)
            if no_energy:
                print(m_t.text_red('         NO ENERGY !!!'))
                energy_ = False
                fun.move_to_click(fun.wait_close('NO ENERGY !!!'), 0.3)
                return hero

            else:
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
                        if popup_xp:  # я учту это
                            review = 1
                            print(m_t.text_cyan('         я учту это'))
                            sleep(0.2)
                            popup_xp = pyautogui.locateCenterOnScreen('img/energy/_popup_xp.png', confidence=par_conf,
                                                                      region=region_events)
                            fun.move_to_click(popup_xp, 0.1)
                            close_img_ = fun.wait_close('я учту это')
                            while not close_img_:
                                close_img_ = fun.wait_close('я учту это')
                            fun.move_to_click(close_img_, 0)
                        if invite_friends:  # Пригласить друга
                            review = 1
                            print(m_t.text_cyan('         Пригласить друга'))
                            fun.move_to_click(invite_friends, 0.1)
                            fun.move_to_click(fun.cancel_or_knob(), 0)
                            close = fun.wait_close('Пригласить друга')
                            if close:
                                fun.move_to_click(close, 0)
                        if treasure:
                            review = 1
                            print(m_t.text_cyan('         Искать клад'))
                            sleep(0.2)
                            treasure = pyautogui.locateCenterOnScreen('img/energy/_treasure.png', confidence=par_conf,
                                                                      region=region_events)
                            fun.move_to_click(treasure, 0.1)
                            fun.move_to_click(fun.cancel_or_knob(), 0)
                        if yes_go:
                            review = 1
                            print(m_t.text_cyan('         Да, поехали'))
                            sleep(0.2)
                            yes_go = pyautogui.locateCenterOnScreen('img/energy/_yes_go.png', confidence=par_conf,
                                                                    region=region_events)
                            fun.move_to_click(yes_go, 0.1)
                        if awake_friend:
                            review = 1
                            print(m_t.text_cyan('         Разбудить друга'))
                            awake_friend = pyautogui.locateCenterOnScreen('img/energy/_awake_friend.png',
                                                                          confidence=par_conf, region=region_events)
                            fun.move_to_click(awake_friend, 0.1)
                            fun.move_to_click(fun.cancel_or_knob(), 0)
                            close = fun.wait_close('Разбудить друга')
                            if close:
                                fun.move_to_click(close, 0)
                    skip_battle = fun.locCenterImg('img/everything/skip_battle.png', confidence=par_conf)
                    if skip_battle and q_call_pet == 0:
                        q_call_pet = 1
                        fun.call_pet(pos_i)
                    link_battle_end = fun.locCenterImg('img/link_battle_end.png', confidence=0.9)
                link_battle_end = fun.wait_and_stop_img('img/link_battle_end.png')
                pyautogui.moveTo(link_battle_end, duration=0.25)
                if link_battle_end:
                    link_victory = fun.locCenterImg('img/energy/rezult_vick.png', confidence=0.9)
                    if link_victory:
                        # print("Победа")
                        fun.melodi_vic()
                    else:
                        print("Неудача")
                        fun.melodi_feil()

                close_img = fun.wait_and_stop_img('img/everything/close.png', 0.85)
                # закрыть сражение
                fun.move_to_click(close_img, 0)
                sleep(1)
                # сражение закрыто.
                close = fun.wait_close('ожидание всплывающего события')
                # если всплывает "закрыть"
                if close:
                    c_or_k = fun.cancel_or_knob()  # ищем "кнопку" или "отменить" и если есть нажимаем
                    if c_or_k:  # нажимаем 'close'
                        fun.move_to_click(c_or_k, 0)
                    else:  # если нет -> жмем 'close'
                        fun.move_to_click(close, 0)

                    close = fun.wait_close('ожидание всплывающего события')
                    # если всплывает "закрыть"
                    if close:
                        c_or_k = fun.cancel_or_knob()  # ищем "кнопку" или "отменить" и если есть нажимаем
                        if c_or_k:  # нажимаем 'close'
                            fun.move_to_click(c_or_k, 0)
                        else:  # если нет -> жмем 'close'
                            fun.move_to_click(close, 0)
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
        fun.move_to_click(close, 0)
    # опознать героя
    hero = fun.selection_hero()
    while not hero:
        close = fun.locCenterImg('img/everything/close.png', confidence=0.89)
        if close:
            fun.move_to_click(close, 0)
        hero = fun.selection_hero()
    # получить список его заданий
    if hero == 'Gavr':
        tasks_ = b_d.tasks_xp_gavr
        wilt = fun.verifi_isolation(her.Gavr.isolation_end_date)
    elif hero == 'Gadya':
        tasks_ = b_d.tasks_xp_v
        wilt = fun.verifi_isolation(her.Gady.isolation_end_date)
    elif hero == 'Veles':
        tasks_ = b_d.tasks_xp_vel
        wilt = fun.verifi_isolation(her.Veles.isolation_end_date)
    elif hero == 'Mara':
        tasks_ = b_d.tasks_xp_mar
        wilt = fun.verifi_isolation(her.Mara.isolation_end_date)
    # else:
    #     tasks_ = None
    #     wilt = None
    if wilt > 0:
        print(f'Ты слишком слаб, что-бы набирать опыт. Попробуй через {fun.return_days_transformation(wilt)}')
        print(' Перевод energy_gold')
        energy_gold()
    energy_ = True
    while energy_:
        review = 0
        q_call_pet = 0
        fun.open_taverna()
        variant = task_selection(tasks_)
        fun.move_to_click(variant, 0.5)  # автомат
        x, y = variant
        x -= 200
        y -= 100
        pos_g = x, y
        pyautogui.moveTo(pos_g, duration=0.25)
        no_energy = verify_energy(4)
        if no_energy:
            print(m_t.text_red('         NO ENERGY !!!'))
            energy_ = None
            fun.move_to_click(fun.wait_close('NO ENERGY !!!'), 0.3)
            return hero

        else:
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
                        print(m_t.text_cyan('         я учту это'))
                        sleep(0.2)
                        popup_xp = pyautogui.locateCenterOnScreen('img/energy/_popup_xp.png', confidence=par_conf,
                                                                  region=region_events)
                        fun.move_to_click(popup_xp, 0.1)
                        fun.move_to_click(fun.wait_close('я учту это'), 0)
                    if invite_friends:
                        review = 1
                        print(m_t.text_cyan('         Пригласить друга'))
                        fun.move_to_click(invite_friends, 0.1)
                        fun.move_to_click(fun.cancel_or_knob(), 0)
                        close = fun.wait_close('Пригласить друга')
                        if close:
                            fun.move_to_click(close, 0)
                    if treasure:
                        review = 1
                        print(m_t.text_cyan('         Искать клад'))
                        sleep(0.2)
                        treasure = pyautogui.locateCenterOnScreen('img/energy/_treasure.png', confidence=par_conf,
                                                                  region=region_events)
                        fun.move_to_click(treasure, 0.1)
                        fun.move_to_click(fun.cancel_or_knob(), 0)
                    if yes_go:
                        review = 1
                        print(m_t.text_cyan('         Да, поехали'))
                        sleep(0.2)
                        yes_go = pyautogui.locateCenterOnScreen('img/energy/_yes_go.png', confidence=par_conf,
                                                                region=region_events)
                        fun.move_to_click(yes_go, 0.1)
                    if awake_friend:
                        review = 1
                        print(m_t.text_cyan('Разбудить друга'))
                        awake_friend = pyautogui.locateCenterOnScreen('img/energy/_awake_friend.png',
                                                                      confidence=par_conf, region=region_events)
                        fun.move_to_click(awake_friend, 0.1)
                        fun.move_to_click(fun.cancel_or_knob(), 0)
                        close = fun.wait_close('Разбудить друга')
                        if close:
                            fun.move_to_click(close, 0)
                skip_battle = fun.locCenterImg('img/everything/skip_battle.png', confidence=par_conf)
                if skip_battle and q_call_pet == 0:
                    q_call_pet = 1
                    fun.call_pet(pos_i)
                link_battle_end = fun.locCenterImg('img/link_battle_end.png', confidence=0.9)

            link_battle_end = fun.wait_and_stop_img('img/link_battle_end.png')
            pyautogui.moveTo(link_battle_end, duration=0.25)
            if link_battle_end:
                link_victory = fun.locCenterImg('img/energy/rezult_vick.png', confidence=0.9)
                if link_victory:
                    # print("Победа")
                    fun.melodi_vic()
                else:
                    print("Неудача")
                    fun.melodi_feil()
                    if her.Active == 'Gadya':
                        her.Gady.isolation_end_date = fun.get_isolation_end_date()
                    if her.Active == 'Gavr':
                        her.Gavr.isolation_end_date = fun.get_isolation_end_date()
                    if her.Active == 'Veles':
                        her.Veles.isolation_end_date = fun.get_isolation_end_date()
                    if her.Active == 'Mara':
                        her.Mara.isolation_end_date = fun.get_isolation_end_date()
                    energy_gold()

            close_img = fun.wait_and_stop_img('img/everything/close.png', 0.85)
            # закрыть сражение
            fun.move_to_click(close_img, 0)
            sleep(1)
            # сражение закрыто.
            close = fun.wait_close('ожидание всплывающего события')
            # если всплывает "закрыть"
            if close:
                c_o_k = fun.cancel_or_knob()  # ищем "кнопку" или "отменить" и если есть нажимаем
                if c_o_k:  # нажимаем 'close'
                    fun.move_to_click(c_o_k, 0)
                else:  # если нет -> жмем 'close'
                    fun.move_to_click(close, 0)

                close = fun.wait_close('ожидание всплывающего события')
                # если всплывает "закрыть"
                if close:
                    c_o_k = fun.cancel_or_knob()  # ищем "кнопку" или "отменить" и если есть нажимаем
                    if c_o_k:  # нажимаем 'close'
                        fun.move_to_click(c_o_k, 0)
                    else:  # если нет -> жмем 'close'
                        fun.move_to_click(close, 0)
            sleep(1)

        if energy_ == 0:
            print()
        else:
            print()
            print('следующее задание')
        # energy_ = 0 # для выполнения одного цикла
