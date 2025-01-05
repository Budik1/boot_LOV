from tkinter import *
from tkinter import ttk

import fun
from fun import my_print_to_file, date_utc_now, attack_guru
import my_text as m_t
import revision_of_house as r_h
import energy
import arena
import kv_and_raid
import pickle
import creating_photo as c_photo

# from PIL import ImageTk

mark_result = 'o'
mark_start = '.'
date_start_prog = date_utc_now()

gady_energy_status, gady_case_status = 0, 0
gavr_energy_status, gavr_case_status = 0, 0
veles_energy_status, veles_case_status = 0, 0
mara_energy_status, mara_case_status = 0, 0
gady_guru_status, gavr_guru_status, veles_guru_status, mara_guru_status = 0, 0, 0, 0
gady_gift_status, gavr_gift_status, veles_gift_status, mara_gift_status = 0, 0, 0, 0
gady_game_status, gavr_game_status, veles_game_status, mara_game_status = 0, 0, 0, 0

state_of_play = {
    'дата': date_start_prog,
    'Гавр-энергия': gavr_energy_status,
    'Гадя-энергия': gady_energy_status,
    'Велес-энергия': veles_energy_status,
    'Мара-энергия': mara_energy_status,

    'Гавр-кейс': gavr_case_status,
    'Гадя-кейс': gady_case_status,
    'Велес-кейс': veles_case_status,
    'Мара-кейс': mara_case_status,

    'Гадя-гуру': gady_guru_status,
    'Гавр-гуру': gavr_guru_status,
    'Велес-гуру': veles_guru_status,
    'Мара-гуру': mara_guru_status,

    'Гадя-gift': gady_gift_status,
    'Гадя-кости': gady_game_status,
    'Гавр-gift': gavr_gift_status,
    'Гавр-кости': gavr_game_status,
    'Велес-gift': veles_gift_status,
    'Велес-кости': veles_game_status,
    'Мара-gift': mara_gift_status,
    'Мара-кости': mara_game_status,

}


# my_print_to_file('')
# my_print_to_file('*******                      *******')
# my_print_to_file("******* перезапуск программы *******")
# my_print_to_file('*******                      *******')
# my_print_to_file('')


def verifi_and_change_data(data_to_load):
    """
    Получает словарь
    """
    global gady_game_status, gavr_game_status, veles_game_status, mara_game_status
    global gady_gift_status, gavr_gift_status, veles_gift_status, mara_gift_status
    global gady_guru_status, gavr_guru_status, veles_guru_status, mara_guru_status
    global gady_energy_status, gavr_energy_status, veles_energy_status, mara_energy_status
    global gady_case_status, gavr_case_status, veles_case_status, mara_case_status
    global date_start_prog

    gavr_energy_status, gavr_case_status = data_to_load['Гавр-энергия'], data_to_load['Гавр-кейс']
    gady_energy_status, gady_case_status = data_to_load['Гадя-энергия'], data_to_load['Гадя-кейс']
    veles_energy_status, veles_case_status = data_to_load['Велес-энергия'], data_to_load['Велес-кейс']
    mara_energy_status, mara_case_status = data_to_load['Мара-энергия'], data_to_load['Мара-кейс']

    gady_guru_status = data_to_load['Гадя-гуру']
    gavr_guru_status = data_to_load['Гавр-гуру']
    veles_guru_status = data_to_load['Велес-гуру']
    mara_guru_status = data_to_load['Мара-гуру']

    gady_gift_status = data_to_load['Гадя-gift']
    gavr_gift_status = data_to_load['Гавр-gift']
    veles_gift_status = data_to_load['Велес-gift']
    mara_gift_status = data_to_load['Мара-gift']

    gady_game_status = data_to_load['Гадя-кости']
    gavr_game_status = data_to_load['Гавр-кости']
    veles_game_status = data_to_load['Велес-кости']
    mara_game_status = data_to_load['Мара-кости']

    date_ver = data_to_load['дата']
    # если даты совпадают ставим соответствующий маркер в зависимости от значения состояния события в файле
    if date_ver == date_start_prog:
        gady_energy.set(mark_result) if gady_energy_status else gady_energy.set(mark_start)
        gavr_energy.set(mark_result) if gavr_energy_status else gavr_energy.set(mark_start)
        veles_energy.set(mark_result) if veles_energy_status else veles_energy.set(mark_start)
        mara_energy.set(mark_result) if mara_energy_status else mara_energy.set(mark_start)

        gady_case.set(mark_result) if gady_case_status else gady_case.set(mark_start)
        gavr_case.set(mark_result) if gavr_case_status else gavr_case.set(mark_start)
        veles_case.set(mark_result) if veles_case_status else veles_case.set(mark_start)
        mara_case.set(mark_result) if mara_case_status else mara_case.set(mark_start)

        gady_guru.set(mark_result) if gady_guru_status else gady_guru.set(mark_start)
        gavr_guru.set(mark_result) if gavr_guru_status else gavr_guru.set(mark_start)
        veles_guru.set(mark_result) if veles_guru_status else veles_guru.set(mark_start)
        mara_guru.set(mark_result) if mara_guru_status else mara_guru.set(mark_start)

        gady_gift.set(mark_result) if gady_gift_status else gady_gift.set(mark_start)
        gavr_gift.set(mark_result) if gavr_gift_status else gavr_gift.set(mark_start)
        veles_gift.set(mark_result) if veles_gift_status else veles_gift.set(mark_start)
        mara_gift.set(mark_result) if mara_gift_status else mara_gift.set(mark_start)

        gady_game.set(mark_result) if gady_game_status else gady_game.set(mark_start)
        gavr_game.set(mark_result) if gavr_game_status else gavr_game.set(mark_start)
        veles_game.set(mark_result) if veles_game_status else veles_game.set(mark_start)
        mara_game.set(mark_result) if mara_game_status else mara_game.set(mark_start)

    # иначе обнуляем значения и ставим стартовый маркер
    else:
        gady_energy_status, gady_case_status = 0, 0
        gavr_energy_status, gavr_case_status = 0, 0
        veles_energy_status, veles_case_status = 0, 0
        mara_energy_status, mara_case_status = 0, 0
        gady_guru_status, gavr_guru_status, veles_guru_status, mara_guru_status = 0, 0, 0, 0
        gady_gift_status, gavr_gift_status, veles_gift_status, mara_gift_status = 0, 0, 0, 0
        gady_game_status, gavr_game_status, veles_game_status, mara_game_status = 0, 0, 0, 0
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
        gady_game.set(mark_start)
        gavr_gift.set(mark_start)
        gavr_game.set(mark_start)
        veles_gift.set(mark_start)
        veles_game.set(mark_start)
        mara_gift.set(mark_start)
        mara_game.set(mark_start)

        print(m_t.text_magenta("смена дат"))
        save_to_file()


def save_to_file():
    global gady_game_status, gavr_game_status, veles_game_status, mara_game_status
    global gady_gift_status, gavr_gift_status, veles_gift_status, mara_gift_status
    global gady_guru_status, gavr_guru_status, veles_guru_status, mara_guru_status
    global gady_energy_status, gavr_energy_status, veles_energy_status, mara_energy_status
    global gady_case_status, gavr_case_status, veles_case_status, mara_case_status
    global date_start_prog
    # создаётся библиотека содержащая значения состояние событий
    data_to_save = {
        'дата': date_start_prog,
        'Гавр-энергия': gavr_energy_status,
        'Гадя-энергия': gady_energy_status,
        'Велес-энергия': veles_energy_status,
        'Мара-энергия': mara_energy_status,

        'Гавр-кейс': gavr_case_status,
        'Гадя-кейс': gady_case_status,
        'Велес-кейс': veles_case_status,
        'Мара-кейс': mara_case_status,

        'Гадя-гуру': gady_guru_status,
        'Гавр-гуру': gavr_guru_status,
        'Велес-гуру': veles_guru_status,
        'Мара-гуру': mara_guru_status,

        'Гадя-gift': gady_gift_status,
        'Гадя-кости': gady_game_status,
        'Гавр-gift': gavr_gift_status,
        'Гавр-кости': gavr_game_status,
        'Велес-gift': veles_gift_status,
        'Велес-кости': veles_game_status,
        'Мара-gift': mara_gift_status,
        'Мара-кости': mara_game_status,

    }
    # verifi_and_change_data(data_to_load)
    print('запись')
    file1 = open('config.txt', 'wb')
    pickle.dump(data_to_save, file1)
    file1.close()


def read_from_file():
    global gady_game_status, gavr_game_status, veles_game_status, mara_game_status
    global gady_gift_status, gavr_gift_status, veles_gift_status, mara_gift_status
    global gady_guru_status, gavr_guru_status, veles_guru_status, mara_guru_status
    global gady_energy_status, gavr_energy_status, veles_energy_status, mara_energy_status
    global gady_case_status, gavr_case_status, veles_case_status, mara_case_status
    global date_start_prog

    try:
        file1 = open('config.txt', 'rb')
        data_to_load = pickle.load(file1)
        file1.close()

        verifi_and_change_data(data_to_load)


    except:
        print(m_t.text_red('Config поврежден или не создан)))'))
        save_to_file()


def arena_battles():
    attempts = 0
    while True:
        arena.battle_in_arena()
        attempts += 1
        print(f'попытка {attempts}, Бой {arena.quantity_battles}')


def revision():
    global gady_case_status, gavr_case_status, veles_case_status, mara_case_status

    hero = r_h.revision_of_house()
    if hero == 'Gavr':
        gavr_case.set(mark_result)
        gavr_case_status = 1
    elif hero == 'Gadya':
        gady_case.set(mark_result)
        gady_case_status = 1
    elif hero == 'Veles':
        veles_case.set(mark_result)
        veles_case_status = 1
    elif hero == 'Mara':
        mara_case.set(mark_result)
        mara_case_status = 1
    print(m_t.text_green('запись состояния'))
    save_to_file()


def en_gold():
    global gady_energy_status, gavr_energy_status, veles_energy_status, mara_energy_status

    name_hero = energy.energy_gold()
    if name_hero == 'Gavr':
        if gavr_energy_status != 1:
            gavr_energy.set(mark_result)
            gavr_energy_status = 1
    elif name_hero == 'Gadya':
        if gady_energy_status != 1:
            gady_energy.set(mark_result)
            gady_energy_status = 1
    elif name_hero == 'Veles':
        if veles_energy_status != 1:
            veles_energy.set(mark_result)
            veles_energy_status = 1
    elif name_hero == 'Mara':
        print('mara_energy_status = ', mara_energy_status)

        if mara_energy_status != 1:
            mara_energy.set(mark_result)
            mara_energy_status = 1
    # print(text_green('запись состояния'))
    save_to_file()


def en_xp():
    global gady_energy_status, gavr_energy_status, veles_energy_status, mara_energy_status

    name_hero = energy.energy_xp()
    if name_hero == 'Gavr':
        if gavr_energy_status != 1:
            gavr_energy.set(mark_result)
            gavr_energy_status = 1
    elif name_hero == 'Gadya':
        if gady_energy_status != 1:
            gady_energy.set(mark_result)
            gady_energy_status = 1
    elif name_hero == 'Veles':
        if veles_energy_status != 1:
            veles_energy.set(mark_result)
            veles_energy_status = 1
    elif name_hero == 'Mara':
        if mara_energy_status != 1:
            mara_energy.set(mark_result)
            mara_energy_status = 1
    save_to_file()


def guru():
    global gady_guru_status, gavr_guru_status, veles_guru_status, mara_guru_status
    hero = attack_guru()
    if hero == 'Gadya':
        gady_guru.set(mark_result)
        gady_guru_status = 1
    if hero == 'Gavr':
        gavr_guru.set(mark_result)
        gavr_guru_status = 1
    if hero == 'Veles':
        veles_guru.set(mark_result)
        veles_guru_status = 1
    elif hero == 'Mara':
        mara_guru.set(mark_result)
        mara_guru_status = 1
    save_to_file()


def mark_gift():
    global gady_gift_status, gavr_gift_status, veles_gift_status, mara_gift_status
    hero = fun.selection_hero()
    if hero == 'Gadya':
        gady_gift.set(mark_result)
        gady_gift_status = 1
    if hero == 'Gavr':
        gavr_gift.set(mark_result)
        gavr_gift_status = 1
    if hero == 'Veles':
        veles_gift.set(mark_result)
        veles_gift_status = 1
    elif hero == 'Mara':
        mara_gift.set(mark_result)
        mara_gift_status = 1
    save_to_file()


def marks_k():
    global gady_game_status, gavr_game_status, veles_game_status, mara_game_status
    hero = fun.selection_hero()
    if hero == 'Gadya':
        gady_game.set(mark_result)
        gady_game_status = 1
    if hero == 'Gavr':
        gavr_game.set(mark_result)
        gavr_game_status = 1
    if hero == 'Veles':
        veles_game.set(mark_result)
        veles_game_status = 1
    elif hero == 'Mara':
        mara_game.set(mark_result)
        mara_game_status = 1
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

gady_gift = StringVar()
gady_game = StringVar()
gavr_gift = StringVar()
gavr_game = StringVar()
veles_gift = StringVar()
veles_game = StringVar()
mara_gift = StringVar()
mara_game = StringVar()

read_from_file()
step_line = 25
line0, line1, line2, line3, line4 = step_line * 0, step_line * 1, step_line * 2, step_line * 3, step_line * 4
line5, line6, line7, line8, line9 = step_line * 5, step_line * 6, step_line * 7, step_line * 8, step_line * 9

ttk.Label(text='(С)').place(x=0, y=line0 + 2)
ttk.Label(text='(E)').place(x=0, y=line1 + 2)

ttk.Button(text="сбор сундуков", width=14, command=revision).place(x=17, y=line0)

ttk.Button(text="энергия в золото", width=16, command=en_gold).place(x=17, y=line1)
ttk.Button(text="фото уровня", width=16, command=c_photo.creating_photo_lvl).place(x=17, y=line8)

ttk.Button(text="энергия в опыт", width=16, command=en_xp).place(x=190, y=line1)

ttk.Button(text="арена", width=14, command=arena_battles).place(x=202, y=line0)

ttk.Button(text="КВ", command=kv_and_raid.kv).place(x=119, y=line2)
ttk.Button(text="ГУРУ", command=guru).place(x=119, y=line0)

step_other = -4
column_C = 110  # 50
column_E = 70
column_G = 90
column_P = 50  # 110
column_K = 130
column_name = 0

ttk.Label(text='C').place(x=column_C, y=line3)  # сундуки
ttk.Label(text='E').place(x=column_E, y=line3)  # энергия
ttk.Label(text='G').place(x=column_G, y=line3)  # бой с гуру
ttk.Button(text='P', width=1, command=mark_gift).place(x=column_P, y=line3)  # подарки
ttk.Button(text='K', width=1, command=marks_k).place(x=column_K, y=line3)  # кости

n_line = 3
" Gadya"
name_hero = " Gadya"
n_line += 1
line = step_line * n_line
ttk.Label(text=name_hero).place(x=column_name, y=line)  # + step_other
ttk.Label(textvariable=gady_case).place(x=column_C, y=line)  # + step_other
ttk.Label(textvariable=gady_energy).place(x=column_E, y=line)  # + step_other
ttk.Label(textvariable=gady_guru).place(x=column_G, y=line)  # + step_other
ttk.Label(textvariable=gady_gift).place(x=column_P, y=line)  # + step_other
ttk.Label(textvariable=gady_game).place(x=column_K, y=line)  # + step_other

ttk.Entry(textvariable=gady_var_time, width=5).place(x=220, y=line)  # + step_other

# " Гавр"
n_line += 1
name_hero = " Гавр"
line = step_line * n_line  # + 1
ttk.Label(text=name_hero).place(x=0, y=line + step_other)
ttk.Label(textvariable=gavr_case).place(x=column_C, y=line + step_other)
ttk.Label(textvariable=gavr_energy).place(x=column_E, y=line + step_other)
ttk.Label(textvariable=gavr_guru).place(x=column_G, y=line + step_other)
ttk.Label(textvariable=gavr_gift).place(x=column_P, y=line + step_other)
ttk.Label(textvariable=gavr_game).place(x=column_K, y=line + step_other)

ttk.Entry(textvariable=gavr_var_time, width=5).place(x=220, y=line + step_other)

" Велес"
n_line += 1
name_hero = " Велес"
line = step_line * n_line + 1
ttk.Label(text=name_hero).place(x=column_name, y=line + step_other * 2)
ttk.Label(textvariable=veles_case).place(x=column_C, y=line + step_other * 2)
ttk.Label(textvariable=veles_energy).place(x=column_E, y=line + step_other * 2)
ttk.Label(textvariable=veles_guru).place(x=column_G, y=line + step_other * 2)
ttk.Label(textvariable=veles_gift).place(x=column_P, y=line + step_other * 2)
ttk.Label(textvariable=veles_game).place(x=column_K, y=line + step_other * 2)

# " Мара"
n_line += 1
name_hero = " Мара"
line = step_line * n_line + 1
ttk.Label(text=name_hero).place(x=column_name, y=line + step_other * 3)
ttk.Label(textvariable=mara_case).place(x=column_C, y=line + step_other * 3)
ttk.Label(textvariable=mara_energy).place(x=column_E, y=line + step_other * 3)
ttk.Label(textvariable=mara_guru).place(x=column_G, y=line + step_other * 3)
ttk.Label(textvariable=mara_gift).place(x=column_P, y=line + step_other * 3)
ttk.Label(textvariable=mara_game).place(x=column_K, y=line + step_other * 3)

root.mainloop()
