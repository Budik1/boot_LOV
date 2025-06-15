import pyautogui
import fun
from fun import mouse_move_to_click, click_update, wait_and_stop_img
from fun import one_in_two, date_utc_now
import my_color_text as m_t
import time
import pickle
import heroes as her

"""

"""
"""
Если КВ  
"""
# minutes_verifi = 0.1
is_raid_today = False   # хранится в файле
                        # обнуляется со сменой суток


def verifi_time_raid():
    # global minutes_verifi
    hour_now = int(time.strftime('%H'))
    minutes_now = int(time.strftime('%M'))
    # if minutes_verifi != minutes_now:
    #     hour_oo = o_in_oo(hour_now)
    #     minutes_oo = o_in_oo(minutes_now)
    #     # print(hour_oo, ':', minutes_oo)
    #     minutes_verifi = int(time.strftime('%M'))
    if hour_now == 21 and minutes_now >= 45:
        return True
    elif hour_now == 22 and minutes_now <= 45:
        return True
    else:
        return False


def status_kv():
    """
    КВ ожидается и идет - это одна картинка?
    """
    state_kv_vs = fun.locCenterImg('img/kv/kv_stat/state_kv_vs.png')
    state_kv_victory = fun.locCenterImg('img/kv/kv_stat/state_kv_victory.png')
    state_kv_def = fun.locCenterImg('img/kv/kv_stat/state_kv_def.png')
    if state_kv_vs:
        return True
    else:
        return False


def status_raid():
    """
    небыл - True, был - False
    если небыл;
        можно проверять время
    return: True - если идет
            False если рано\прошёл
    """
    global is_raid_today

    if not is_raid_today:
        # если еще небыло - проверить время
        #      если время - проверить наличие
        # вернуть
        time_raid = verifi_time_raid()
        if time_raid:
            state_raid = fun.locCenterImg('img/kv/kv_stat/state_raid.png')  # не начат
            state_raid_victory = fun.locCenterImg('img/kv/kv_stat/state_raid_victory.png')
            state_raid_vs = fun.locCenterImg('img/kv/kv_stat/state_raid_vs.png')  # vs в рейде
            if state_raid:
                #
                pass
            elif state_raid_vs:
                #
                pass
            elif state_raid_victory:
                # если победа или поражение в рейде
                is_raid_today = True
        print()
