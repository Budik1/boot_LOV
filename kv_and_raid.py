import pyautogui

import fun
from fun import push_close, move_to_click, click_update, wait_and_stop_img, selection_hero, date_start_prog
from fun import o_in_oo, locCenterImg, date_utc_now
import my_text as m_t
import time
import pickle

gavr___duel_q = 0
gavr_duel_q_v = 0
gavr_duel_kv = 0
gavr_duel_kv_vikt = 0
gavr_hour_kvStart = 0
gavr_hour_kvVerifi = int(time.strftime('%H'))
gavr_date_start_kv = date_start_prog

gady___duel_q = 0
gady_duel_q_v = 0
gady_duel_kv = 0
gady_duel_kv_vikt = 0
gady_hour_kvStart = 0
gady_hour_kvVerifi = int(time.strftime('%H'))
gady_date_start_kv = date_start_prog

date_kv = date_start_prog
hero_name = 0
state_raid = "ещё не было"
time_raid = False
minutes_verifi = 0.1


def change_raid_kv():
    minets = time.strftime('M')


def verifi_time_raid():
    global minutes_verifi
    hour_now = int(time.strftime('%H'))
    minutes_now = int(time.strftime('%M'))
    if minutes_verifi != minutes_now:
        hour_oo = o_in_oo(hour_now)
        minutes_oo = o_in_oo(minutes_now)
        # print(hour_oo, ':', minutes_oo)
        minutes_verifi = int(time.strftime('%M'))
    if hour_now == 21 and minutes_now >= 45:
        return True
    elif hour_now == 22 and minutes_now <= 45:
        return True
    else:
        return False


def save_data_kv():
    # print('запись файла kv')
    global gady_hour_kvStart, gavr_hour_kvStart, gavr_date_start_kv, gady_date_start_kv
    global gavr___duel_q, gavr_duel_q_v, gavr_duel_kv, gavr_duel_kv_vikt
    global gady___duel_q, gady_duel_q_v, gady_duel_kv, gady_duel_kv_vikt

    data_kv_to_save = {
        'к-во_боёв-gady': gady___duel_q,
        'к-во_побед-gady': gady_duel_q_v,
        'час-старта-кв-gady': gady_hour_kvStart,
        'к-во_боёв-в-кв_gady': gady_duel_kv,
        'к-во_побед-в-кв_gady': gady_duel_kv_vikt,
        'дата-кв_gady': gady_date_start_kv,

        'к-во_боёв-gavr': gavr___duel_q,
        'к-во_побед-gavr': gavr_duel_q_v,
        'час-старта-кв-gavr': gavr_hour_kvStart,
        'к-во_боёв-в-кв_gavr': gavr_duel_kv,
        'к-во_побед-в-кв_gavr': gavr_duel_kv_vikt,
        'дата-кв_gavr': gavr_date_start_kv,

        'дата-кв': date_kv,
    }

    # print('запись переменных kv')  # , data_kv_to_save
    file1 = open('config_kv.txt', 'wb')
    pickle.dump(data_kv_to_save, file1)
    file1.close()


def read_data_kv():
    # print('чтение файла kv')
    global hero_name, gavr_hour_kvStart, gady_hour_kvStart, gavr_hour_kvVerifi, gady_hour_kvVerifi
    global gavr___duel_q, gavr_duel_q_v, gavr_duel_kv, gavr_duel_kv_vikt, gavr_date_start_kv
    global gady___duel_q, gady_duel_q_v, gady_duel_kv, gady_duel_kv_vikt, gady_date_start_kv

    try:
        file1 = open('config_kv.txt', 'rb')
        data_kv_to_load = pickle.load(file1)
        file1.close()
        # print('чтение переменных kv')  # , data_kv_to_load

        gady___duel_q = data_kv_to_load['к-во_боёв-gady']
        gady_duel_q_v = data_kv_to_load['к-во_побед-gady']
        gady_hour_kvStart = data_kv_to_load['час-старта-кв-gady']
        date_kv_load_gady = data_kv_to_load['дата-кв_gady']

        gavr___duel_q = data_kv_to_load['к-во_боёв-gavr']
        duel_q_vikt_gavr = data_kv_to_load['к-во_побед-gavr']
        gavr_hour_kvStart = data_kv_to_load['час-старта-кв-gavr']
        date_kv_load_gavr = data_kv_to_load['дата-кв_gavr']

        if hero_name == 'Gadya':
            print(f'всего боёв {gady___duel_q}, из них {gady_duel_q_v} побед')
            print(gady_date_start_kv, date_kv_load_gady)
            # gady_hour_kvVerifi = 9
            if date_kv_load_gady == gady_date_start_kv and (gady_hour_kvVerifi - gady_hour_kvStart) <= 3:
                print('gady_hour_kvVerifi = ', gady_hour_kvVerifi)
                print('gady_hour_kvStart = ', gady_hour_kvStart)
                print(gady_hour_kvVerifi - gady_hour_kvStart)
                gady_duel_kv = data_kv_to_load['к-во_боёв-в-кв_gady']
                gady_duel_kv_vikt = data_kv_to_load['к-во_побед-в-кв_gady']
                print(m_t.text_green("Дата-время кв совпадают"),
                      m_t.text_magenta(F"боёв в кв {gady_duel_kv}, из них {gady_duel_kv_vikt} побед"))
            else:
                print(m_t.text_red("Дата-время кв не совпадают, суточные счетчики обнулены!"))
                gady_duel_kv = 0
                gady_duel_kv_vikt = 0
                gady_hour_kvStart = gady_hour_kvVerifi
                save_data_kv()
        if hero_name == 'Gavr':
            print(f'всего боёв {gavr___duel_q}, из них {duel_q_vikt_gavr} побед')
            if date_kv_load_gavr == gavr_date_start_kv and (gavr_hour_kvVerifi - gavr_hour_kvStart) <= 3:
                gavr_duel_kv = data_kv_to_load['к-во_боёв-в-кв_gavr']
                gavr_duel_kv_vikt = data_kv_to_load['к-во_побед-в-кв_gavr']
                print(m_t.text_green("Дата-время кв совпадают"),
                      m_t.text_magenta(F"боёв в кв {gavr_duel_kv}, из них {gavr_duel_kv_vikt} побед"))
            else:
                print(m_t.text_red("Дата-время кв не совпадают, суточные счетчики обнулены!"))
                gavr_duel_kv = 0
                gavr_duel_kv_vikt = 0
                gavr_hour_kvStart = gavr_hour_kvVerifi
                save_data_kv()
    except:
        print(m_t.text_red('Файл config_kv.txt имеет неверную структуру или не создан.'))
        save_data_kv()


def kv():
    global gavr___duel_q, gavr_duel_q_v, gavr_duel_kv, gavr_duel_kv_vikt, gavr_date_start_kv
    global gady___duel_q, gady_duel_q_v, gady_duel_kv, gady_duel_kv_vikt, gady_date_start_kv
    global hero_name, gavr_hour_kvStart, gady_hour_kvStart, gady_hour_kvVerifi, gavr_hour_kvVerifi
    global time_raid

    q_it_print = True
    hero_name = selection_hero()
    if not hero_name:
        print(m_t.text_red("Герой не опознан"))
        exit_kv_img = locCenterImg('img/everything/exit.png')
        move_to_click(exit_kv_img, 0)
        wait_and_stop_img('img/everything/info1.png', 0.9)
        hero_name = selection_hero()
    if hero_name == 'Gadya':
        fun.to_clan()
        btn_battles = wait_and_stop_img('img/kv/battles.png', 0.9)
        move_to_click(btn_battles, 0)
        read_data_kv()  # устновка значений в соответствии с файлом 'config_kv.txt'
        gady_hour_kvStart = int(time.strftime('%H'))
        gady_date_start_kv = date_utc_now()
        print("установка переменных kv Gadya")
    if hero_name == 'Gavr':
        fun.to_clan()
        btn_battles = wait_and_stop_img('img/kv/battles.png', 0.9)
        move_to_click(btn_battles, 0)
        read_data_kv()  # устновка значений в соответствии с файлом 'config_kv.txt'
        gavr_hour_kvStart = int(time.strftime('%H'))
        gavr_date_start_kv = date_start_prog
        print("установка переменных kv Gavr")

    # read_data_kv()  # устновка значений в соответствии с файлом 'config_kv.txt'
    # state_raid -> "не было", "идет", "прошёл"
    time_raid = verifi_time_raid()
    if time_raid:
        print(m_t.text_cyan('рейд!!!'))
        img_raids = locCenterImg('img/kv/raids.png')
        move_to_click(img_raids, 0)
        wait_and_stop_img('img/kv/update.png')
    click_update()

    q_duel_start = True  # Флаг входа в дуэль, имеет состояния True/False. Если True - вход возможен
    clan_var_img = locCenterImg('img/kv/clan_var.png', 0.9)
    duel_start = locCenterImg('img/kv/duel_start.png', 0.9)
    duel_over = locCenterImg('img/kv/duel_over.png', 0.8)
    clan_raid_img = locCenterImg('img/kv/clan_raid.png')

    # check_kv
    # check_raid
    # while check_kv and check_raid:
    while clan_var_img or clan_raid_img:
        if not time_raid:
            time_raid = verifi_time_raid()
            if time_raid:
                print(m_t.text_cyan('рейд!!!'))
                img_raids = locCenterImg('img/kv/raids.png')
                move_to_click(img_raids, 0)
                wait_and_stop_img('img/kv/update.png')
                click_update()
        # if not check_vs: # нужен счетчик
        #     img_raids = locCenterImg('img/kv/raids.png')
        #     move_to_click(img_raids, 0)
        #     wait_and_stop_img('img/kv/update.png')
        if duel_start and q_duel_start:  # загорелась кнопка атаковать в войне
            q_it_print = True
            clan_var_img = locCenterImg('img/kv/clan_var.png', 0.9)
            clan_raid_img = locCenterImg('img/kv/clan_raid.png')
            if clan_var_img:
                print("Война, можно атаковать")
            elif clan_raid_img:
                print("Рейд, можно атаковать")
            q_duel_start = False
            # print(clan_var_img, 'clan_var_img v duel_start')
            # print(clan_raid_img, 'clan_raid_img v duel_start')
            move_to_click(duel_start, 0)
            # задержка для выполнения действий в бою
            if hero_name == 'Gadya':
                gady_name_hero = wait_and_stop_img('img/kv/gady.png')
            #     move_to_click(gady_name_hero, 0)
            if time_raid:
                bomba_img = locCenterImg('img/kv/bomba.png')
                print('бомба', bomba_img)
                if bomba_img:
                    move_to_click(bomba_img, 0)
                    x, y = bomba_img
                    x -= 325
                    y -= 30
                    pos_pet = x, y
                    move_to_click(pos_pet, 0)
        if duel_over and clan_var_img:
            # print(clan_raid_img, 'clan_raid_img in duel_over')
            q_duel_start = True
            if hero_name == 'Gavr':  # изменение счетчиков КВ для героя
                gavr___duel_q += 1
                gavr_duel_kv += 1
            elif hero_name == 'Gadya':  # изменение счетчиков КВ для героя
                gady___duel_q += 1
                gady_duel_kv += 1
            print(m_t.text_yellow("дуэль в кв окончена"))
            # задержка для определени победа/поражение
            duel_over = wait_and_stop_img('img/kv/duel_over.png', 0.8)
            pyautogui.moveTo(duel_over, duration=0.5)
            img_duel_victory = locCenterImg('img/kv/kv_duel_victory.png', 0.9)
            img_duel_defeat = locCenterImg('img/kv/kv_duel_defeat.png', 0.9)
            if img_duel_victory:
                print("Победа")
                if hero_name == 'Gavr':
                    gavr_duel_kv_vikt += 1
                    gavr_duel_q_v += 1
                    vik_gavr = round((gavr_duel_q_v / (gavr___duel_q / 100)), 4)
                    print(m_t.text_green(f"{gavr_duel_q_v} побед в {gavr___duel_q} боях,"),
                          m_t.text_magenta(f'всего побед {vik_gavr}%)'))
                    percent_vik_in_kv = round((gavr_duel_kv_vikt / (gavr_duel_kv / 100)), 3)
                    print(m_t.text_cyan(f'в кв боёв {gavr_duel_kv}, побед {gavr_duel_kv_vikt} ({percent_vik_in_kv}%)'))

                    gavr_hour_kvVerifi = int(time.strftime('%H'))
                elif hero_name == 'Gadya':
                    gady_duel_kv_vikt += 1
                    gady_duel_q_v += 1
                    vik_gady = round((gady_duel_q_v / (gady___duel_q / 100)), 4)
                    print(m_t.text_green(f"{gady_duel_q_v} побед в {gady___duel_q} боях,"),
                          m_t.text_magenta(f'( {vik_gady}% )'))
                    percent_vik_in_kv = round((gady_duel_kv_vikt / (gady_duel_kv / 100)), 3)
                    print(m_t.text_cyan(f'в кв боёв {gady_duel_kv}, побед {gady_duel_kv_vikt} ({percent_vik_in_kv}%)'))
                    gady_hour_kvVerifi = int(time.strftime('%H'))
            elif img_duel_defeat:
                print("поражение((")
                if hero_name == 'Gavr':
                    vik_gavr = round((gavr_duel_q_v / (gavr___duel_q / 100)), 3)
                    print(m_t.text_green(f"{gavr_duel_q_v} побед в {gavr___duel_q} боях,"),
                          m_t.text_magenta(f'всего побед {vik_gavr}%)'))
                    percent_vik_in_kv = round((gavr_duel_kv_vikt / (gavr_duel_kv / 100)), 3)
                    print(m_t.text_cyan(f'в кв боёв {gavr_duel_kv}, побед {gavr_duel_kv_vikt} ({percent_vik_in_kv}%)'))

                elif hero_name == 'Gadya':
                    vik_gady = round((gady_duel_q_v / (gady___duel_q / 100)), 3)
                    print(m_t.text_green(f"{gady_duel_q_v} побед в {gady___duel_q} боях,"),
                          m_t.text_magenta(f'( {vik_gady}% )'))
                    percent_vik_in_kv = round((gady_duel_kv_vikt / (gady_duel_kv / 100)), 3)
                    print(m_t.text_cyan(f'в кв боёв {gady_duel_kv}, побед {gady_duel_kv_vikt} ({percent_vik_in_kv}%)'))
            push_close()
            clan_var_img = wait_and_stop_img('img/kv/clan_var.png', 0.9)
            # clan_raid_img = loc_center_img('img/kv/clan_raid.png')
            # click_update()
            save_data_kv()
            #
            if time_raid:
                # print(text_cyan('в цикле рейд!!!'))
                img_raids = locCenterImg('img/kv/raids.png')
                move_to_click(img_raids, 0)
                wait_and_stop_img('img/kv/update.png')

            click_update()
        if duel_over and clan_raid_img:
            q_duel_start = True
            print(m_t.text_yellow("дуэль в рейде окончена"))
            duel_over = wait_and_stop_img('img/kv/duel_over.png', 0.8)
            pyautogui.moveTo(duel_over, duration=0.5)

            push_close()
            # вылетает на площадь с фонтаном((
            fountain_pl_img = locCenterImg('img/everything/fountain_pl.jpg', 0.9)
            clan_raid_img = locCenterImg('img/kv/clan_raid.png', 0.9)
            while not fountain_pl_img and not clan_raid_img:
                print('вылет с рейда?')
                fountain_pl_img = locCenterImg('img/everything/fountain_pl.jpg', 0.9)
                clan_raid_img = locCenterImg('img/kv/clan_raid.png', 0.9)
            if fountain_pl_img:
                print('точно)) надо обратно')
                if hero_name == 'Gadya':
                    in_clan = wait_and_stop_img('img/kv/clan_gadya.png', 0.9)
                    move_to_click(in_clan, 0)
                    # поиск рейдов и нажать
                    clan_raid_img = wait_and_stop_img('img/kv/raids.png', 0.9)
                    move_to_click(clan_raid_img, 0)
                if hero_name == 'Gavr':
                    in_clan = wait_and_stop_img('img/kv/clan_gavr.png', 0.9)
                    move_to_click(in_clan, 0)

            raids_img = wait_and_stop_img('img/kv/raids.png', 0.9)
            move_to_click(raids_img, 0)

            img_battle = locCenterImg('img/kv/battles.png')
            move_to_click(img_battle, 0)
            wait_and_stop_img('img/kv/update.png')

            check_vs = locCenterImg('img/kv/_VS.png')
            print("VS = ", bool(check_vs))
            if check_vs:
                click_update()
            if not check_vs:
                img_raids = locCenterImg('img/kv/raids.png')
                move_to_click(img_raids, 0)
                wait_and_stop_img('img/kv/update.png')
                click_update()

        if q_it_print:
            q_it_print = False
            # print(clan_var_img, 'clan_var_img v', clan_raid_img, 'clan_raid_img v')
            # print(clan_raid_img, 'clan_raid_img v')

        check_vs = locCenterImg('img/kv/_VS.png')

        duel_start = locCenterImg('img/kv/duel_start.png', 0.9)
        duel_over = locCenterImg('img/kv/duel_over.png', 0.8)
        # bomba_img = loc_center_img('img/kv/bomba.png')

    print('выход из кв')
    print(clan_var_img, 'clan_var_img')
    print(clan_raid_img, 'clan_raid_img')
