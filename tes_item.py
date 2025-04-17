import heroes as her
import fun
from fun import move_to_click, locCenterImg
import baza_dannyx as b_d
import os


def her_viewer():
    fun.selection_hero()
    her.Hero.get_name(her.Active.hero_activ)
    print(f'моя переменная {her.Active.hero_activ}')
    print(f'{her.Hero.get_name(her.Active.hero_activ)}')


def define_lvl():
    lvl_list = b_d.lvl_list

    for value in lvl_list:
        fail_name = f'img/energy/lvl/{value}lvl.png'
        lvl = fun.locCenterImg(fail_name, confidence=0.99)
        if lvl:
            print(f'уровень героя {value}')
            return value
    else:
        print("уровень не определен")
        return None


def get_task_list(*, lvl, option):  # option
    # option = gold or xp
    a = f"img/lvl_archive/f 9/t1g.png"
    files_list = os.listdir(f'img/lvl_archive/f {lvl}')
    if option == 'x':
        task_x_list = list(filter(lambda x: 'x' in x, files_list))  # создание списка с признаком "х"
        print(f'{task_x_list= } {option=}')
        return task_x_list
    elif option == 'g':
        task_x_list = list(filter(lambda x: 'x' in x, files_list))  # создание списка с признаком "х"
        m_list = list(filter(lambda x: x not in task_x_list, files_list))  # удаление из основного списка списка "х"
        m_list.remove(f'{lvl}lvl.png')
        print(f'{m_list=} {option=}')


def get_task_set(*, lvl, option):
    task_all_list = os.listdir(f'img/lvl_archive/f {lvl}')
    task_all_set = set(task_all_list)
    if option == 'x':
        task_x_set = set(filter(lambda x: 'x' in x, task_all_list))
        print(f'{task_x_set= }')
    elif option == 'g':
        task_x_set = set(filter(lambda x: 'x' in x, task_all_list))
        task_g_set = task_all_set - task_x_set
        task_g_set.remove(f'{lvl}lvl.png')
        print(f'{task_g_set= }')


# get_task_set(lvl=25, option='x')
# get_task_list(lvl=25, option='g')
# define_lvl()

def info_task_hero():
    lvl = define_lvl()
    get_task_list(lvl=lvl, option='x')

# info_task_hero()

def mara_guru():
    con = 0.87
    guru = fun.locCenterImg('img/city/i_am_guru.png', confidence=con)
    while not guru:
        arr = locCenterImg('img/city/arrow_right.png')
        move_to_click(arr, 0)
        x, y = arr
        y -= 30
        pos =  x, y
        fun.move_mause(pos=pos)
        guru = fun.locCenterImg('img/city/test_guru.png', confidence=con)
    fun.move_mause(pos=guru)
    fun.move_to_click(pos_click=guru, z_p_k=0)
    x, y = guru
    x -= 26
    y -= 46
    fun.move_mause(pos=(x, y), speed=0.5)
    x_demo, y_demo = x, y
    change_x = 20
    change_y = 20
    x_demo += change_x
    y_demo += change_y
    fun.move_mause(pos=(x_demo, y_demo), speed=0.5)
    fun.foto('img/city/button_at.png', (x, y, change_x, change_y))
    attack = fun.locCenterImg('img/city/button_at.png')
    fun.move_to_click(pos_click=attack, z_p_k=0.5)


mara_guru()