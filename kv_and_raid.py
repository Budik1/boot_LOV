#  заменить на переменную класса
# не отслеживает окончание КВ
import pyautogui
import fun
from fun import move_to_click, click_update, wait_and_stop_img
from fun import o_in_oo, locCenterImg, date_utc_now
import my_text as m_t
import time
import pickle
import heroes as her
from heroes import Hero, Active

her.Gavr.hour_start_kv_ver = int(time.strftime('%H'))
her.Gavr.date_start_kv = fun.date_utc_now()

her.Gady.hour_start_kv_ver = int(time.strftime('%H'))
her.Gady.date_start_kv = fun.date_utc_now()

date_kv = fun.date_utc_now()
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
    data_kv_to_save = {
        'к-во_боёв-gady': her.Gady.qty_all,
        'к-во_побед-gady': her.Gady.qty_all_victory,
        'к-во_боёв-в-кв_gady': her.Gady.qty_kv_all,
        'к-во_побед-в-кв_gady': her.Gady.qty_kv_victory,
        'дата-кв_gady': her.Gady.date_start_kv,
        'час-старта-кв-gady': her.Gady.hour_start_kv,

        'к-во_боёв-gavr': her.Gavr.qty_all,
        'к-во_побед-gavr': her.Gavr.qty_all_victory,
        'к-во_боёв-в-кв_gavr': her.Gavr.qty_kv_all,
        'к-во_побед-в-кв_gavr': her.Gavr.qty_kv_victory,
        'дата-кв_gavr': her.Gavr.date_start_kv,
        'час-старта-кв-gavr': her.Gavr.hour_start_kv,

        'дата-кв': date_kv,
    }

    file1 = open('config_kv.txt', 'wb')
    pickle.dump(data_kv_to_save, file1)
    file1.close()


def read_data_kv():
    # print('чтение файла kv')
    global hero_name
    hour_verifi = int(time.strftime('%H'))

    try:
        file1 = open('config_kv.txt', 'rb')
        data_kv_to_load = pickle.load(file1)
        file1.close()

        her.Gady.qty_all = data_kv_to_load['к-во_боёв-gady']
        her.Gady.qty_all_victory = data_kv_to_load['к-во_побед-gady']
        her.Gady.hour_start_kv = data_kv_to_load['час-старта-кв-gady']
        date_kv_load_gady = data_kv_to_load['дата-кв_gady']

        her.Gavr.qty_all = data_kv_to_load['к-во_боёв-gavr']
        her.Gavr.qty_all_victory = data_kv_to_load['к-во_побед-gavr']
        her.Gavr.hour_start_kv = data_kv_to_load['час-старта-кв-gavr']
        date_kv_load_gavr = data_kv_to_load['дата-кв_gavr']

        if hero_name == 'Gadya':
            print(f'всего боёв {her.Gady.qty_all}, из них {her.Gady.qty_all_victory} побед')
            print(her.Gady.date_start_kv, date_kv_load_gady)
            # her.Gady.hour_start_kv_ver = 9

            if date_kv_load_gady == her.Gady.date_start_kv and (her.Gady.hour_start_kv_ver - her.Gady.hour_start_kv) <= 3:
                print('her.Gady.hour_start_kv_ver = ', her.Gady.hour_start_kv_ver)
                print('her.Gady.hour_start_kv = ', her.Gady.hour_start_kv)
                print(her.Gady.hour_start_kv_ver - her.Gady.hour_start_kv)
                her.Gady.qty_kv_all = data_kv_to_load['к-во_боёв-в-кв_gady']
                her.Gady.qty_kv_victory = data_kv_to_load['к-во_побед-в-кв_gady']
                print(m_t.text_green("Дата-время кв совпадают"),
                      m_t.text_magenta(F"боёв в кв {her.Gady.qty_kv_all}, из них {her.Gady.qty_kv_victory} побед"))
            else:
                print(m_t.text_red("Дата-время кв не совпадают, суточные счетчики обнулены!"))
                her.Gady.qty_kv_all = 0
                her.Gady.qty_kv_victory = 0
                her.Gady.hour_start_kv = her.Gady.hour_start_kv_ver
                save_data_kv()
        if hero_name == 'Gavr':
            print(f'всего боёв {her.Gavr.qty_all}, из них {her.Gavr.qty_all_victory} побед')
            if date_kv_load_gavr == her.Gavr.date_start_kv and (her.Gavr.hour_start_kv_ver - her.Gavr.hour_start_kv) <= 3:
                her.Gavr.qty_kv_all = data_kv_to_load['к-во_боёв-в-кв_gavr']
                her.Gavr.qty_kv_victory = data_kv_to_load['к-во_побед-в-кв_gavr']
                print(m_t.text_green("Дата-время кв совпадают"),
                      m_t.text_magenta(F"боёв в кв {her.Gavr.qty_kv_all}, из них {her.Gavr.qty_kv_victory} побед"))
            else:
                print(m_t.text_red("Дата-время кв не совпадают, суточные счетчики обнулены!"))
                her.Gavr.qty_kv_all = 0
                her.Gavr.qty_kv_victory = 0
                her.Gavr.hour_start_kv = her.Gavr.hour_start_kv_ver
                save_data_kv()
    except:
        print(m_t.text_red('Файл config_kv.txt имеет неверную структуру или не создан.'))
        save_data_kv()


def kv():
    global hero_name
    global time_raid

    q_it_print = True
    hero_name = fun.selection_hero()
    if not hero_name:
        print(m_t.text_red("Герой не опознан"))
        exit_kv_img = fun.locCenterImg('img/everything/exit.png')
        move_to_click(exit_kv_img, 0)
        wait_and_stop_img('img/everything/info1.png', 0.9)
        hero_name = fun.selection_hero()
    if hero_name == 'Gadya':
        in_clan = fun.pos_clan()
        fun.move_to_click(in_clan, 0)
        btn_battles = wait_and_stop_img('img/kv/battles.png', 0.9)
        move_to_click(btn_battles, 0)

        read_data_kv()  # устновка значений в соответствии с файлом 'config_kv.txt'
        her.Gady.hour_start_kv = int(time.strftime('%H'))
        her.Gady.date_start_kv = date_utc_now()
        print("установка переменных kv Gadya")
    if hero_name == 'Gavr':
        in_clan = fun.pos_clan()
        fun.move_to_click(in_clan, 0)
        btn_battles = wait_and_stop_img('img/kv/battles.png', 0.9)
        move_to_click(btn_battles, 0)
        read_data_kv()  # устновка значений в соответствии с файлом 'config_kv.txt'
        her.Gavr.hour_start_kv = int(time.strftime('%H'))
        her.Gavr.date_start_kv = fun.date_start_prog
        print("установка переменных kv Gavr")

    # read_data_kv()  # устновка значений в соответствии с файлом 'config_kv.txt'
    # state_raid -> "не было", "идет", "прошёл"
    time_raid = verifi_time_raid()
    if time_raid:
        print(m_t.text_cyan('рейд!!!'))
        img_raids = fun.locCenterImg('img/kv/raids.png')
        move_to_click(img_raids, 0)
        wait_and_stop_img('img/kv/update.png')
    click_update()

    q_duel_start = True  # Флаг входа в дуэль, имеет состояния True/False. Если True - вход возможен
    clan_var_img = fun.locCenterImg('img/kv/clan_var.png', 0.9)
    duel_start = fun.locCenterImg('img/kv/duel_start.png', 0.9)
    duel_over = fun.locCenterImg('img/kv/duel_over.png', 0.8)
    clan_raid_img = fun.locCenterImg('img/kv/clan_raid.png')
    state_kv_vs_img = fun.locCenterImg('img/tests/state_kv_vs.png')

    # check_kv
    # check_raid
    # while check_kv and check_raid:
    while clan_var_img or clan_raid_img:
        if not time_raid:
            time_raid = verifi_time_raid()
            if time_raid:
                print(m_t.text_cyan('рейд!!!'))
                img_raids = fun.locCenterImg('img/kv/raids.png')
                move_to_click(img_raids, 0)
                wait_and_stop_img('img/kv/update.png')
                click_update()
                print("при первом пуске ? до цикла в рейде")
        # if not check_vs: # нужен счетчик
        #     img_raids = fun.locCenterImg('img/kv/raids.png')
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
                her.Gavr.qty_all += 1
                her.Gavr.qty_kv_all += 1
            elif hero_name == 'Gadya':  # изменение счетчиков КВ для героя
                her.Gady.qty_all += 1
                her.Gady.qty_kv_all += 1
            print(m_t.text_yellow("дуэль в кв окончена"))
            # задержка для определени победа/поражение
            duel_over = wait_and_stop_img('img/kv/duel_over.png', 0.8)
            pyautogui.moveTo(duel_over, duration=0.5)
            img_duel_victory = locCenterImg('img/kv/kv_duel_victory.png', 0.9)
            img_duel_defeat = locCenterImg('img/kv/kv_duel_defeat.png', 0.9)
            if img_duel_victory:
                print("Победа")
                if hero_name == 'Gavr':
                    # увеличение счетчиков победы
                    her.Gavr.qty_kv_victory += 1
                    her.Gavr.qty_all_victory += 1
                    #
                    vik_gavr = round((her.Gavr.qty_all_victory / (her.Gavr.qty_all / 100)), 4)
                    print(m_t.text_green(f"{her.Gavr.qty_all_victory} побед в {her.Gavr.qty_all} боях,"),
                          m_t.text_magenta(f'всего побед {vik_gavr}%)'))
                    percent_vik_in_kv = round((her.Gavr.qty_kv_victory / (her.Gavr.qty_kv_all / 100)), 3)
                    print(m_t.text_cyan(
                        f'в кв боёв {her.Gavr.qty_kv_all}, побед {her.Gavr.qty_kv_victory} ({percent_vik_in_kv}%)'))

                    her.Gavr.hour_start_kv_ver = int(time.strftime('%H'))
                elif hero_name == 'Gadya':
                    her.Gady.qty_kv_victory += 1
                    her.Gady.qty_all_victory += 1
                    vik_gady = round((her.Gady.qty_all_victory / (her.Gady.qty_all / 100)), 4)
                    print(m_t.text_green(f"{her.Gady.qty_all_victory} побед в {her.Gady.qty_all} боях,"),
                          m_t.text_magenta(f'( {vik_gady}% )'))
                    percent_vik_in_kv = round((her.Gady.qty_kv_victory / (her.Gady.qty_kv_all / 100)), 3)
                    print(m_t.text_cyan(
                        f'в кв боёв {her.Gady.qty_kv_all}, побед {her.Gady.qty_kv_victory} ({percent_vik_in_kv}%)'))
                    her.Gady.hour_start_kv_ver = int(time.strftime('%H'))
            elif img_duel_defeat:
                print("поражение((")
                if hero_name == 'Gavr':
                    vik_gavr = round((her.Gavr.qty_all_victory / (her.Gavr.qty_all / 100)), 3)
                    print(m_t.text_green(f"{her.Gavr.qty_all_victory} побед в {her.Gavr.qty_all} боях,"),
                          m_t.text_magenta(f'всего побед {vik_gavr}%)'))
                    percent_vik_in_kv = round((her.Gavr.qty_kv_victory / (her.Gavr.qty_kv_all / 100)), 3)
                    print(m_t.text_cyan(
                        f'в кв боёв {her.Gavr.qty_kv_all}, побед {her.Gavr.qty_kv_victory} ({percent_vik_in_kv}%)'))

                elif hero_name == 'Gadya':
                    vik_gady = round((her.Gady.qty_all_victory / (her.Gady.qty_all / 100)), 3)
                    print(m_t.text_green(f"{her.Gady.qty_all_victory} побед в {her.Gady.qty_all} боях,"),
                          m_t.text_magenta(f'( {vik_gady}% )'))
                    percent_vik_in_kv = round((her.Gady.qty_kv_victory / (her.Gady.qty_kv_all / 100)), 3)
                    print(m_t.text_cyan(
                        f'в кв боёв {her.Gady.qty_kv_all}, побед {her.Gady.qty_kv_victory} ({percent_vik_in_kv}%)'))
            fun.push_close()
            clan_var_img = wait_and_stop_img('img/kv/clan_var.png', 0.9)
            save_data_kv()
            #
            if time_raid:
                # print(text_cyan('в цикле рейд!!!'))
                img_raids = locCenterImg('img/kv/raids.png')
                move_to_click(img_raids, 0)
                wait_and_stop_img('img/kv/update.png')

            click_update()

            print('ждем атаки в рейде и кв стр 267')
        if duel_over and clan_raid_img:
            q_duel_start = True
            print(m_t.text_yellow("дуэль в рейде окончена"))
            duel_over = wait_and_stop_img('img/kv/duel_over.png', 0.8)
            pyautogui.moveTo(duel_over, duration=0.5)

            fun.push_close()
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
                    in_clan = fun.pos_clan()
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
                print('тут проверка активности кв стр 328')

            if not check_vs:
                img_raids = locCenterImg('img/kv/raids.png')
                move_to_click(img_raids, 0)
                wait_and_stop_img('img/kv/update.png')
                click_update()
                print('чего ждем? 333 стр')
                # возврат в рейд и ожидание кнопки атаковать

        if q_it_print:
            q_it_print = False
            # print(clan_var_img, 'clan_var_img v', clan_raid_img, 'clan_raid_img v')
            # print(clan_raid_img, 'clan_raid_img v')

        check_vs = locCenterImg('img/kv/_VS.png')

        duel_start = locCenterImg('img/kv/duel_start.png', 0.9)
        duel_over = locCenterImg('img/kv/duel_over.png', 0.8)
        # bomba_img = loc_center_img('img/kv/bomba.png')
        state_kv_vs_img = locCenterImg('img/tests/state_kv_vs.png')

    print('выход из кв')
    print(clan_var_img, 'clan_var_img')
    print(clan_raid_img, 'clan_raid_img')
