from tkinter import *
from tkinter import ttk

import fun
import solid_memory
import energy
import person
import arena
import kv_and_raid
import different_events
import pickle
import revision_of_house as r_h
import creating_photo as c_photo
import my_color_text as m_t
import baza_dannyx as b_d
import heroes as her

# from PIL import ImageTk

mark_result = 'o'
mark_start = '.'


def start_prog():
    result, data_to_load = solid_memory.reading_file()
    if result:
        try:
            solid_memory.setting_recoverable_value(read_date=data_to_load)
            solid_memory.setting_cumulative_value(read_data=data_to_load)
        except:
            print(m_t.tc_red('start_prog()'))
            print(m_t.tc_red('Config не полный'))
        displaying_values(info=False)
    else:
        print(m_t.tc_red('start_prog()'))
        print(m_t.tc_red('Config поврежден или не создан)))'))
        displaying_values()


def displaying_values(*, info=True):
    gady_energy_sum.set(f'/  {her.Gady.energy_sum}')
    gavr_energy_sum.set(f'/  {her.Gavr.energy_sum}')
    veles_energy_sum.set(f'/  {her.Veles.energy_sum}')
    mara_energy_sum.set(f'/  {her.Mara.energy_sum}')

    gady_en_now.set(her.Gady.energy_count_now)
    gavr_en_now.set(her.Gavr.energy_count_now)
    veles_en_now.set(her.Veles.energy_count_now)
    mara_en_now.set(her.Mara.energy_count_now)

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

    if info:
        solid_memory.save_to_file(info=True)
    else:
        solid_memory.save_to_file(info=False)
    return


def foto_lvl():
    num = lvl_num.get()
    different_events.creating_photo_lvl(lvl_num=num)
    return


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
    hero = fun.selection_hero()
    if hero == 'Gavr':
        if her.Gavr.case_status == 1:
            print('Уже выполнен')
        else:
            r_h.revision_of_house()
            gavr_case.set(mark_result)
            her.Gavr.case_status = 1
    elif hero == 'Gadya':
        if her.Gady.case_status == 1:
            print('Уже выполнен')
        else:
            r_h.revision_of_house()
            gady_case.set(mark_result)
            her.Gady.case_status = 1
    elif hero == 'Veles':
        if her.Veles.case_status == 1:
            print('Уже выполнен')
        else:
            r_h.revision_of_house()
            veles_case.set(mark_result)
            her.Veles.case_status = 1
    elif hero == 'Mara':
        if her.Mara.case_status == 1:
            print('Уже выполнен')
        else:
            r_h.revision_of_house()
            mara_case.set(mark_result)
            her.Mara.case_status = 1
    print(m_t.tc_green('запись состояния'))
    displaying_values(info=False)


def en_gold():
    hero = energy.energy(target_task='gold_task')
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
    displaying_values(info=False)


def en_xp():
    hero = energy.energy(target_task='xp_task')
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
    displaying_values(info=False)


def guru():
    # hero = fun.attack_guru()
    hero = fun.selection_hero(show_name=False)
    if hero == 'Gadya':
        if her.Gady.guru_status == 1:
            print('Уже выполнен')
        else:
            different_events.attack_guru()
            gady_guru.set(mark_result)
            her.Gady.guru_status = 1
    if hero == 'Gavr':
        if her.Gavr.guru_status == 1:
            print('Уже выполнен')
        else:
            different_events.attack_guru()
            gavr_guru.set(mark_result)
            her.Gavr.guru_status = 1
    if hero == 'Veles':
        if her.Veles.guru_status == 1:
            print('Уже выполнен')
        else:
            different_events.attack_guru()
            veles_guru.set(mark_result)
            her.Veles.guru_status = 1
    elif hero == 'Mara':
        if her.Mara.guru_status == 1:
            print('Уже выполнен')
        else:
            different_events.attack_guru()
            mara_guru.set(mark_result)
            her.Mara.guru_status = 1
    displaying_values(info=False)


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
    displaying_values(info=False)


def game_of_craps():
    hero = fun.selection_hero()
    if hero == 'Gadya':
        different_events.craps()
        gady_game.set(mark_result)
        her.Gady.game_status = 1
    if hero == 'Gavr':
        different_events.craps()
        gavr_game.set(mark_result)
        her.Gavr.game_status = 1
    if hero == 'Veles':
        different_events.craps()
        veles_game.set(mark_result)
        her.Veles.game_status = 1
    elif hero == 'Mara':
        different_events.craps()
        mara_game.set(mark_result)
        her.Mara.game_status = 1
    displaying_values(info=False)
    return


def change_color(*, her_active):
    if her_active == 'Gadya':
        label_1.configure(background='yellow')
    else:
        label_1.configure(background='white')
    if her_active == 'Gavr':
        label_2.configure(background='yellow')
    else:
        label_2.configure(background='white')
    if her_active == 'Veles':
        label_3.configure(background='yellow')
    else:
        label_3.configure(background='white')
    if her_active == 'Mara':
        label_4.configure(background='yellow')
    else:
        label_4.configure(background='white')


def change_gady():
    person.change_acc(hero_name_in_file='gady')
    displaying_values(info=False)
    change_color(her_active=fun.selection_hero(show_name=False))


def change_gavr():
    person.change_acc(hero_name_in_file='gavr')
    displaying_values(info=False)
    change_color(her_active=fun.selection_hero(show_name=False))


def change_veles():
    person.change_acc(hero_name_in_file='veles')
    displaying_values(info=False)
    change_color(her_active=fun.selection_hero(show_name=False))


def change_mara():
    person.change_acc(hero_name_in_file='mara')
    displaying_values(info=False)
    change_color(her_active=fun.selection_hero(show_name=False))


def rapport():
    q_ty_en_gady = her.Gady.energy_count_all
    q_ty_en_gavr = her.Gavr.energy_count_all
    q_ty_en_veles = her.Veles.energy_count_all
    q_ty_en_mara = her.Mara.energy_count_all
    print(f'Всего потрачено')
    print(f'Gady  - {q_ty_en_gady}')
    print(f'Gavr  - {q_ty_en_gavr}')
    print(f'Veles - {q_ty_en_veles}')
    print(f'Mara  - {q_ty_en_mara}')
    return


def rapport_i():
    print(different_events.numbers_lvl_list())


root = Tk()

root.title('помощник "L_O_V"')
root.geometry("300x230+1000+50")  # Ширина x Высота + координата X + координата Y
root.resizable(False, False)

gady_var_time = StringVar()
gavr_var_time = StringVar()

lvl_num = StringVar()

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

gady_energy_sum = StringVar()
gavr_energy_sum = StringVar()
veles_energy_sum = StringVar()
mara_energy_sum = StringVar()

gady_en_now = IntVar()
gavr_en_now = IntVar()
veles_en_now = IntVar()
mara_en_now = IntVar()

gady_gift = StringVar()
gavr_gift = StringVar()
veles_gift = StringVar()
mara_gift = StringVar()

gady_game = StringVar()
gavr_game = StringVar()
veles_game = StringVar()
mara_game = StringVar()

# ---------------------------------------------
start_prog()
# ---------------------------------------------

step_line = 25
line0, line1, line2, line3, line4 = step_line * 0, step_line * 1, step_line * 2, step_line * 3, step_line * 4
line5, line6, line7, line8, line9 = step_line * 5, step_line * 6, step_line * 7, step_line * 8, step_line * 9

# ttk.Label(text='(С)').place(x=0, y=line0 + 2)
ttk.Label(text='(E)').place(x=0, y=line1 + 2)

# ttk.Button(text="сбор сундуков", width=14, command=revision).place(x=17, y=line0)

ttk.Button(text="энергия в золото", width=16, command=en_gold).place(x=17, y=line1)
ttk.Button(text="фото уровня", width=16, command=foto_lvl).place(x=0, y=line8)
ttk.Entry(textvariable=lvl_num, width=3).place(x=110, y=line8)
ttk.Button(text='(I)', width=2, command=rapport_i).place(x=139, y=line8)
ttk.Button(text="рапорт E", width=11, command=rapport).place(x=220, y=line8)
ttk.Button(text="дроп рейда", width=11, command=c_photo.drop_in_raid).place(x=220, y=line7)

ttk.Button(text="энергия в опыт", width=16, command=en_xp).place(x=190, y=line1)

ttk.Button(text="арена", command=arena_battles).place(x=119, y=line0)

ttk.Button(text="КВ", command=kv_and_raid.kv).place(x=119, y=line2)

step_other = -4
step_column = 22
column_G = 10 + step_column * 2
column_C = 10 + step_column * 3
column_P = 10 + step_column * 4
column_K = 10 + step_column * 5
column_cE = 10 + step_column * 6
column_qE = 10 + step_column * 7
# column_E = 10 + step_column * 3
column_name = 0
width_name = 6

ttk.Button(text='P', width=2, command=mark_gift).place(x=column_P, y=line3)  # подарки
# ttk.Label(text='E').place(x=column_E, y=line3)  # энергия
ttk.Button(text='G', width=2, command=guru).place(x=column_G, y=line3)  # бой с гуру
ttk.Button(text='C', width=2, command=revision).place(x=column_C, y=line3)  # сундуки
ttk.Button(text='K', width=2, command=game_of_craps).place(x=column_K, y=line3)  # кости
ttk.Label(text='cE', width=2).place(x=column_cE, y=line3)  # количество энергии
ttk.Label(text='qE', width=2).place(x=column_qE, y=line3)  # количество энергии
line_number = 3

" Gadya"
name_hero = " Gadya"
line_number += 1
line = step_line * line_number
ttk.Button(text=name_hero, width=width_name, command=change_gady).place(x=column_name, y=line)
ttk.Label(textvariable=gady_gift).place(x=column_P, y=line)
# ttk.Label(textvariable=gady_energy).place(x=column_E, y=line)
ttk.Label(textvariable=gady_guru).place(x=column_G, y=line)
ttk.Label(textvariable=gady_case).place(x=column_C, y=line)
ttk.Label(textvariable=gady_game).place(x=column_K, y=line)
ttk.Label(textvariable=gady_en_now).place(x=column_cE, y=line)
label_1 = ttk.Label()
label_1.configure(textvariable=gady_energy_sum)
label_1.place(x=column_qE, y=line)

ttk.Entry(textvariable=gady_var_time, width=5).place(x=220, y=line)

# " Гавр"
line_number += 1
name_hero = " Гавр"
line = step_line * line_number  # + 1
ttk.Button(text=name_hero, width=width_name, command=change_gavr).place(x=0, y=line)
ttk.Label(textvariable=gavr_gift).place(x=column_P, y=line)
# ttk.Label(textvariable=gavr_energy).place(x=column_E, y=line)
ttk.Label(textvariable=gavr_guru).place(x=column_G, y=line)
ttk.Label(textvariable=gavr_case).place(x=column_C, y=line)
ttk.Label(textvariable=gavr_game).place(x=column_K, y=line)
ttk.Label(textvariable=gavr_en_now).place(x=column_cE, y=line)
label_2 = ttk.Label()
label_2.configure(textvariable=gavr_energy_sum)
label_2.place(x=column_qE, y=line)

ttk.Entry(textvariable=gavr_var_time, width=5).place(x=220, y=line + step_other)

" Велес"
line_number += 1
name_hero = " Велес"
line = step_line * line_number
ttk.Button(text=name_hero, width=width_name, command=change_veles).place(x=column_name, y=line)
ttk.Label(textvariable=veles_gift).place(x=column_P, y=line)
# ttk.Label(textvariable=veles_energy).place(x=column_E, y=line)
ttk.Label(textvariable=veles_guru).place(x=column_G, y=line)
ttk.Label(textvariable=veles_case).place(x=column_C, y=line)
ttk.Label(textvariable=veles_game).place(x=column_K, y=line)
ttk.Label(textvariable=veles_en_now).place(x=column_cE, y=line)
label_3 = ttk.Label()
label_3.configure(textvariable=veles_energy_sum)
label_3.place(x=column_qE, y=line)

# " Мара"
line_number += 1
name_hero = " Мара"
line = step_line * line_number
ttk.Button(text=name_hero, width=width_name, command=change_mara).place(x=column_name, y=line)
ttk.Label(textvariable=mara_gift).place(x=column_P, y=line)
# ttk.Label(textvariable=mara_energy).place(x=column_E, y=line)
ttk.Label(textvariable=mara_guru).place(x=column_G, y=line)
ttk.Label(textvariable=mara_case).place(x=column_C, y=line)
ttk.Label(textvariable=mara_game).place(x=column_K, y=line)
ttk.Label(textvariable=mara_en_now).place(x=column_cE, y=line)
label_4 = ttk.Label()
label_4.configure(textvariable=mara_energy_sum)
label_4.place(x=column_qE, y=line)

root.mainloop()
