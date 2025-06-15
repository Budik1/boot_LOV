from tkinter import *
from tkinter import ttk

import fun
import my_color_text as m_t
import revision_of_house as r_h
import energy
import arena
import kv_and_raid
import pickle
import creating_photo as c_photo
import baza_dannyx as b_d
import heroes as her
import person
import solid_memory

# from PIL import ImageTk

mark_result = 'o'
mark_start = '.'
date_start_prog = fun.date_utc_now()
her.Active.date_now = fun.date_utc_now()


def verification_date():
    her.Active.check_date = fun.date_utc_now()


def start_prog():
    result, data_to_load = solid_memory.reading_file()
    if result:
        verifi_and_change_data(data_to_load)
    else:
        pass


def displaying_values(*, info=True):
    gady_energy.set(mark_result) if her.Gady.energy_status else gady_energy.set(mark_start)
    gavr_energy.set(mark_result) if her.Gavr.energy_status else gavr_energy.set(mark_start)
    veles_energy.set(mark_result) if her.Veles.energy_status else veles_energy.set(mark_start)
    mara_energy.set(mark_result) if her.Mara.energy_status else mara_energy.set(mark_start)

    gady_case.set(mark_result) if her.Gady.case_status else gady_case.set(mark_start)
    gavr_case.set(mark_result) if her.Gavr.case_status else gavr_case.set(mark_start)
    veles_case.set(mark_result) if her.Veles.case_status else veles_case.set(mark_start)
    mara_case.set(mark_result) if her.Mara.case_status else mara_case.set(mark_start)

    gady_guru.set(mark_result) if her.Gady.guru_status else gady_guru.set(mark_start)
    gavr_guru.set(mark_result) if her.Gavr.guru_status else gavr_guru.set(mark_start)
    veles_guru.set(mark_result) if her.Veles.guru_status else veles_guru.set(mark_start)
    mara_guru.set(mark_result) if her.Mara.guru_status else mara_guru.set(mark_start)

    gady_gift.set(mark_result) if her.Gady.gift_status else gady_gift.set(mark_start)
    gavr_gift.set(mark_result) if her.Gavr.gift_status else gavr_gift.set(mark_start)
    veles_gift.set(mark_result) if her.Veles.gift_status else veles_gift.set(mark_start)
    mara_gift.set(mark_result) if her.Mara.gift_status else mara_gift.set(mark_start)

    gady_game.set(mark_result) if her.Gady.game_status else gady_game.set(mark_start)
    gavr_game.set(mark_result) if her.Gavr.game_status else gavr_game.set(mark_start)
    veles_game.set(mark_result) if her.Veles.game_status else veles_game.set(mark_start)
    mara_game.set(mark_result) if her.Mara.game_status else mara_game.set(mark_start)


def verifi_and_change_data(data_to_load):
    """
    Получает словарь
    """
    her.Gavr.energy_status = data_to_load['Гавр-энергия']
    her.Gady.energy_status = data_to_load['Гадя-энергия']
    her.Veles.energy_status = data_to_load['Велес-энергия']
    her.Mara.energy_status = data_to_load['Мара-энергия']

    her.Gavr.case_status = data_to_load['Гавр-кейс']
    her.Gady.case_status = data_to_load['Гадя-кейс']
    her.Veles.case_status = data_to_load['Велес-кейс']
    her.Mara.case_status = data_to_load['Мара-кейс']

    her.Gady.guru_status = data_to_load['Гадя-гуру']
    her.Gavr.guru_status = data_to_load['Гавр-гуру']
    her.Veles.guru_status = data_to_load['Велес-гуру']
    her.Mara.guru_status = data_to_load['Мара-гуру']

    her.Gady.gift_status = data_to_load['Гадя-gift']
    her.Gavr.gift_status = data_to_load['Гавр-gift']
    her.Veles.gift_status = data_to_load['Велес-gift']
    her.Mara.gift_status = data_to_load['Мара-gift']

    her.Gady.game_status = data_to_load['Гадя-кости']
    her.Gavr.game_status = data_to_load['Гавр-кости']
    her.Veles.game_status = data_to_load['Велес-кости']
    her.Mara.game_status = data_to_load['Мара-кости']

    her.Gady.isolation_end_date = data_to_load['Гадя-дата-конца карантина']
    her.Gavr.isolation_end_date = data_to_load['Гавр-дата-конца карантина']
    her.Veles.isolation_end_date = data_to_load['Велес-дата-конца карантина']
    her.Mara.isolation_end_date = data_to_load['Мара-дата-конца карантина']

    # print('установлена дата из файла')
    gady_energy_sum.set(her.Gady.energy_sum)
    gavr_energy_sum.set(her.Gavr.energy_sum)
    veles_energy_sum.set(her.Veles.energy_sum)
    mara_energy_sum.set(her.Mara.energy_sum)

    verification_date()
    her.Active.date_now = data_to_load['дата']
    her.Active.max_time_wait_load = data_to_load['max_time_wait_load']
    her.Active.max_time_wait_id = data_to_load['max_time_wait_id']

    # если даты совпадают ставим соответствующий маркер в зависимости от значения состояния события в файле
    if her.Active.date_now == her.Active.check_date:
        gady_energy.set(mark_result) if her.Gady.energy_status else gady_energy.set(mark_start)
        gavr_energy.set(mark_result) if her.Gavr.energy_status else gavr_energy.set(mark_start)
        veles_energy.set(mark_result) if her.Veles.energy_status else veles_energy.set(mark_start)
        mara_energy.set(mark_result) if her.Mara.energy_status else mara_energy.set(mark_start)

        gady_case.set(mark_result) if her.Gady.case_status else gady_case.set(mark_start)
        gavr_case.set(mark_result) if her.Gavr.case_status else gavr_case.set(mark_start)
        veles_case.set(mark_result) if her.Veles.case_status else veles_case.set(mark_start)
        mara_case.set(mark_result) if her.Mara.case_status else mara_case.set(mark_start)

        gady_guru.set(mark_result) if her.Gady.guru_status else gady_guru.set(mark_start)
        gavr_guru.set(mark_result) if her.Gavr.guru_status else gavr_guru.set(mark_start)
        veles_guru.set(mark_result) if her.Veles.guru_status else veles_guru.set(mark_start)
        mara_guru.set(mark_result) if her.Mara.guru_status else mara_guru.set(mark_start)

        gady_gift.set(mark_result) if her.Gady.gift_status else gady_gift.set(mark_start)
        gavr_gift.set(mark_result) if her.Gavr.gift_status else gavr_gift.set(mark_start)
        veles_gift.set(mark_result) if her.Veles.gift_status else veles_gift.set(mark_start)
        mara_gift.set(mark_result) if her.Mara.gift_status else mara_gift.set(mark_start)

        gady_game.set(mark_result) if her.Gady.game_status else gady_game.set(mark_start)
        gavr_game.set(mark_result) if her.Gavr.game_status else gavr_game.set(mark_start)
        veles_game.set(mark_result) if her.Veles.game_status else veles_game.set(mark_start)
        mara_game.set(mark_result) if her.Mara.game_status else mara_game.set(mark_start)

    # иначе обнуляем значения и ставим стартовый маркер
    else:
        her.Active.date_now = her.Active.check_date
        her.Gady.energy_status = 0
        her.Gavr.energy_status = 0
        her.Veles.energy_status = 0
        her.Mara.energy_status = 0

        her.Gady.case_status = 0
        her.Gavr.case_status = 0
        her.Veles.case_status = 0
        her.Mara.case_status = 0

        her.Gady.guru_status = 0
        her.Gavr.guru_status = 0
        her.Veles.guru_status = 0
        her.Mara.guru_status = 0

        her.Gady.gift_status = 0
        her.Gavr.gift_status = 0
        her.Veles.gift_status = 0
        her.Mara.gift_status = 0

        her.Gady.game_status = 0
        her.Gavr.game_status = 0
        her.Veles.game_status = 0
        her.Mara.game_status = 0

        # установка маркера
        gady_energy.set(mark_start)
        gavr_energy.set(mark_start)
        veles_energy.set(mark_start)
        mara_energy.set(mark_start)

        gady_case.set(mark_start)
        gavr_case.set(mark_start)
        veles_case.set(mark_start)
        mara_case.set(mark_start)

        gady_guru.set(mark_start)
        gavr_guru.set(mark_start)
        veles_guru.set(mark_start)
        mara_guru.set(mark_start)

        gady_gift.set(mark_start)
        gavr_gift.set(mark_start)
        veles_gift.set(mark_start)
        mara_gift.set(mark_start)

        gady_game.set(mark_start)
        gavr_game.set(mark_start)
        veles_game.set(mark_start)
        mara_game.set(mark_start)

        print(m_t.tc_magenta("смена дат"))
        save_to_file()


def save_to_file():
    # создаётся библиотека содержащая значения состояние событий
    data_to_save = {
        'дата': her.Active.date_now,
        'max_time_wait_load': her.Active.max_time_wait_load,
        'max_time_wait_id': her.Active.max_time_wait_id,

        'Гадя-энергия': her.Gady.energy_status,
        'Гавр-энергия': her.Gavr.energy_status,
        'Велес-энергия': her.Veles.energy_status,
        'Мара-энергия': her.Mara.energy_status,

        'Гадя-кейс': her.Gady.case_status,
        'Гавр-кейс': her.Gavr.case_status,
        'Велес-кейс': her.Veles.case_status,
        'Мара-кейс': her.Mara.case_status,

        'Гадя-гуру': her.Gady.guru_status,
        'Гавр-гуру': her.Gavr.guru_status,
        'Велес-гуру': her.Veles.guru_status,
        'Мара-гуру': her.Mara.guru_status,

        'Гадя-gift': her.Gady.gift_status,
        'Гавр-gift': her.Gavr.gift_status,
        'Велес-gift': her.Veles.gift_status,
        'Мара-gift': her.Mara.gift_status,

        'Гадя-кости': her.Gady.game_status,
        'Гавр-кости': her.Gavr.game_status,
        'Велес-кости': her.Veles.game_status,
        'Мара-кости': her.Mara.game_status,

        'Гадя-дата-конца карантина': her.Gady.isolation_end_date,
        'Гавр-дата-конца карантина': her.Gavr.isolation_end_date,
        'Велес-дата-конца карантина': her.Veles.isolation_end_date,
        'Мара-дата-конца карантина': her.Mara.isolation_end_date,
    }
    print('запись')
    # print(f'{her.Gady.isolation_end_date} для Гади')
    # print(f'{her.Gavr.isolation_end_date} для Гавра')
    # print(f'{her.Veles.isolation_end_date} для Велеса')
    # print(f'{her.Mara.isolation_end_date} для Мары')
    file1 = open('config.txt', 'wb')
    pickle.dump(data_to_save, file1)
    file1.close()


def reading_file():
    try:
        file1 = open('config.txt', 'rb')
        data_to_load = pickle.load(file1)
        file1.close()
        result = True, data_to_load
        verifi_and_change_data(data_to_load)
    except:
        print(m_t.tc_red('Config поврежден или не создан)))'))
        result = False
        data_to_load = False
        save_to_file()
    return result, data_to_load


def arena_battles():
    value = gady_var_time.get()
    if value:
        print(value)
        # print(type(value))
    attempts = 0
    while True:
        arena.battle_in_arena()
        attempts += 1
        print(f'попытка {attempts}, Бой {b_d.quantity_battles}')


def revision():
    hero = r_h.revision_of_house()
    if hero == 'Gavr':
        gavr_case.set(mark_result)
        her.Gavr.case_status = 1
    elif hero == 'Gadya':
        gady_case.set(mark_result)
        her.Gady.case_status = 1
    elif hero == 'Veles':
        veles_case.set(mark_result)
        her.Veles.case_status = 1
    elif hero == 'Mara':
        mara_case.set(mark_result)
        her.Mara.case_status = 1
    print(m_t.tc_green('запись состояния'))
    save_to_file()


def en_gold():
    hero = energy.energy_gold()
    if hero == 'Gavr':
        if her.Gavr.energy_status != 1:
            gavr_energy.set(mark_result)
            her.Gavr.energy_status = 1
    elif hero == 'Gadya':
        if her.Gady.energy_status != 1:
            gady_energy.set(mark_result)
            her.Gady.energy_status = 1
    elif hero == 'Veles':
        if her.Veles.energy_status != 1:
            veles_energy.set(mark_result)
            her.Veles.energy_status = 1
    elif hero == 'Mara':
        if her.Mara.energy_status != 1:
            mara_energy.set(mark_result)
            her.Mara.energy_status = 1

    # print(text_green('запись состояния'))
    save_to_file()


def en_xp():
    hero = energy.energy_xp()
    if hero == 'Gavr':
        if her.Gavr.energy_status != 1:
            gavr_energy.set(mark_result)
            her.Gavr.energy_status = 1
    elif hero == 'Gadya':
        if her.Gady.energy_status != 1:
            gady_energy.set(mark_result)
            her.Gady.energy_status = 1
    elif hero == 'Veles':
        if her.Veles.energy_status != 1:
            veles_energy.set(mark_result)
            her.Veles.energy_status = 1
    elif hero == 'Mara':
        if her.Mara.energy_status != 1:
            mara_energy.set(mark_result)
            her.Mara.energy_status = 1
    save_to_file()


def guru():
    hero = fun.attack_guru()
    if hero == 'Gadya':
        gady_guru.set(mark_result)
        her.Gady.guru_status = 1
    if hero == 'Gavr':
        gavr_guru.set(mark_result)
        her.Gavr.guru_status = 1
    if hero == 'Veles':
        veles_guru.set(mark_result)
        her.Veles.guru_status = 1
    elif hero == 'Mara':
        mara_guru.set(mark_result)
        her.Mara.guru_status = 1
    save_to_file()


def mark_gift():
    hero = fun.selection_hero()
    if hero == 'Gadya':
        gady_gift.set(mark_result)
        her.Gady.gift_status = 1
    if hero == 'Gavr':
        gavr_gift.set(mark_result)
        her.Gavr.gift_status = 1
    if hero == 'Veles':
        veles_gift.set(mark_result)
        her.Veles.gift_status = 1
    elif hero == 'Mara':
        mara_gift.set(mark_result)
        her.Mara.gift_status = 1
    save_to_file()


def marks_k():
    hero = fun.selection_hero()
    if hero == 'Gadya':
        gady_game.set(mark_result)
        her.Gady.game_status = 1
    if hero == 'Gavr':
        gavr_game.set(mark_result)
        her.Gavr.game_status = 1
    if hero == 'Veles':
        veles_game.set(mark_result)
        her.Veles.game_status = 1
    elif hero == 'Mara':
        mara_game.set(mark_result)
        her.Mara.game_status = 1
    save_to_file()


def change_gady():
    person.change_acc(hero_name_in_file='gady')
    save_to_file()


def change_gavr():
    person.change_acc(hero_name_in_file='gavr')
    save_to_file()


def change_veles():
    person.change_acc(hero_name_in_file='veles')
    save_to_file()


def change_mara():
    person.change_acc(hero_name_in_file='mara')
    save_to_file()


root = Tk()

root.title('помощник "L_O_V"')
root.geometry("300x230+1000+50")  # Ширина x Высота + координата X + координата Y
root.resizable(False, False)

gady_var_time = StringVar()
gavr_var_time = StringVar()

gady_guru = StringVar()
gavr_guru = StringVar()
veles_guru = StringVar()
mara_guru = StringVar()

gady_case = StringVar()
gavr_case = StringVar()
veles_case = StringVar()
mara_case = StringVar()

gady_energy = StringVar()
gavr_energy = StringVar()
veles_energy = StringVar()
mara_energy = StringVar()

gady_energy_sum = IntVar()
gavr_energy_sum = IntVar()
veles_energy_sum = IntVar()
mara_energy_sum = IntVar()

# gady_energy_sum = her.Gady.energy_sum
# gavr_energy_sum = her.Gavr.energy_sum
# veles_energy_sum = her.Veles.energy_sum
# mara_energy_sum = her.Mara.energy_sum


gady_gift = StringVar()
gavr_gift = StringVar()
veles_gift = StringVar()
mara_gift = StringVar()

gady_game = StringVar()
gavr_game = StringVar()
veles_game = StringVar()
mara_game = StringVar()

reading_file()

step_line = 25
line0, line1, line2, line3, line4 = step_line * 0, step_line * 1, step_line * 2, step_line * 3, step_line * 4
line5, line6, line7, line8, line9 = step_line * 5, step_line * 6, step_line * 7, step_line * 8, step_line * 9

# ttk.Label(text='(С)').place(x=0, y=line0 + 2)
ttk.Label(text='(E)').place(x=0, y=line1 + 2)

# ttk.Button(text="сбор сундуков", width=14, command=revision).place(x=17, y=line0)

ttk.Button(text="энергия в золото", width=16, command=en_gold).place(x=17, y=line1)
ttk.Button(text="фото уровня", width=16, command=c_photo.creating_photo_lvl).place(x=10, y=line8)
ttk.Button(text="фото", width=16, command=c_photo.state_kv).place(x=190, y=line8)
ttk.Button(text="дроп рейда", width=16, command=c_photo.drop_in_raid).place(x=190, y=line7)

ttk.Button(text="энергия в опыт", width=16, command=en_xp).place(x=190, y=line1)

ttk.Button(text="арена", command=arena_battles).place(x=119, y=line0)

ttk.Button(text="КВ", command=kv_and_raid.kv).place(x=119, y=line2)

step_other = -4
step_column = 22
column_P = 10 + step_column * 2
column_E = 10 + step_column * 3
column_G = 10 + step_column * 4
column_C = 10 + step_column * 5
column_K = 10 + step_column * 6
column_qE = 10 + step_column * 7
column_name = 0
width_name = 6

ttk.Button(text='P', width=2, command=mark_gift).place(x=column_P, y=line3)  # подарки
ttk.Label(text='E').place(x=column_E, y=line3)  # энергия
ttk.Button(text='G', width=2, command=guru).place(x=column_G, y=line3)  # бой с гуру
ttk.Button(text='C', width=2, command=revision).place(x=column_C, y=line3)  # сундуки
ttk.Button(text='K', width=2, command=marks_k).place(x=column_K, y=line3)  # кости
ttk.Button(text='qE', width=2).place(x=column_qE, y=line3)  # количество энергии
line_number = 3

" Gadya"
name_hero = " Gadya"
line_number += 1
line = step_line * line_number
ttk.Button(text=name_hero, width=width_name, command=change_gady).place(x=column_name, y=line)
ttk.Label(textvariable=gady_gift).place(x=column_P, y=line)
ttk.Label(textvariable=gady_energy).place(x=column_E, y=line)
ttk.Label(textvariable=gady_guru).place(x=column_G, y=line)
ttk.Label(textvariable=gady_case).place(x=column_C, y=line)
ttk.Label(textvariable=gady_game).place(x=column_K, y=line)
ttk.Label(textvariable=gady_energy_sum).place(x=column_qE, y=line)

ttk.Entry(textvariable=gady_var_time, width=5).place(x=220, y=line)

# " Гавр"
line_number += 1
name_hero = " Гавр"
line = step_line * line_number  # + 1
ttk.Button(text=name_hero, width=width_name, command=change_gavr).place(x=0, y=line)
ttk.Label(textvariable=gavr_case).place(x=column_C, y=line)
ttk.Label(textvariable=gavr_energy).place(x=column_E, y=line)
ttk.Label(textvariable=gavr_guru).place(x=column_G, y=line)
ttk.Label(textvariable=gavr_gift).place(x=column_P, y=line)
ttk.Label(textvariable=gavr_game).place(x=column_K, y=line)
ttk.Label(textvariable=gavr_energy_sum).place(x=column_qE, y=line)

ttk.Entry(textvariable=gavr_var_time, width=5).place(x=220, y=line + step_other)

" Велес"
line_number += 1
name_hero = " Велес"
line = step_line * line_number
ttk.Button(text=name_hero, width=width_name, command=change_veles).place(x=column_name, y=line)
ttk.Label(textvariable=veles_case).place(x=column_C, y=line)
ttk.Label(textvariable=veles_energy).place(x=column_E, y=line)
ttk.Label(textvariable=veles_guru).place(x=column_G, y=line)
ttk.Label(textvariable=veles_gift).place(x=column_P, y=line)
ttk.Label(textvariable=veles_game).place(x=column_K, y=line)
ttk.Label(textvariable=veles_energy_sum).place(x=column_qE, y=line)

# " Мара"
line_number += 1
name_hero = " Мара"
line = step_line * line_number
ttk.Button(text=name_hero, width=width_name, command=change_mara).place(x=column_name, y=line)
ttk.Label(textvariable=mara_case).place(x=column_C, y=line)
ttk.Label(textvariable=mara_energy).place(x=column_E, y=line)
ttk.Label(textvariable=mara_guru).place(x=column_G, y=line)
ttk.Label(textvariable=mara_gift).place(x=column_P, y=line)
ttk.Label(textvariable=mara_game).place(x=column_K, y=line)
ttk.Label(textvariable=mara_energy_sum).place(x=column_qE, y=line)

root.mainloop()
