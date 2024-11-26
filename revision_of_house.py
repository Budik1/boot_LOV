import pyautogui
from time import sleep
from fun import move_to_click, find_link_i, exit_to_fountain, selection_hero, wait_and_stop_img
import my_text as m_t


def next_haus():
    # print('next_haus')
    sleep(2)
    n_haus = pyautogui.locateCenterOnScreen('img/next_haus.png', confidence=0.8)
    while not n_haus:
        sleep(0.1)
        n_haus = pyautogui.locateCenterOnScreen('img/next_haus.png', confidence=0.8)
    move_to_click(n_haus, 0)


def go_in_haus():
    # print('go_in_haus')
    sleep(2)
    link = find_link_i()
    x, y = link
    x += 240
    y += 220
    haus = x, y
    to_fountain = pyautogui.locateCenterOnScreen('img/to_fountain_from_houses.png', confidence=0.85)
    while not to_fountain:
        sleep(0.25)
        to_fountain = pyautogui.locateCenterOnScreen('img/to_fountain_from_houses.png', confidence=0.85)
        if to_fountain:
            print(to_fountain, 'to_fountain v go_in_haus')
    sleep(0.5)
    path_haus = pyautogui.locateCenterOnScreen('img/path_haus.png', confidence=0.9)
    # print(path_haus, 'path_haus до')
    it = 0
    while not path_haus and it < 3:
        print('поиск дорожки к дому')
        sleep(0.2)
        it += 0.5
        path_haus = pyautogui.locateCenterOnScreen('img/path_haus.png', confidence=0.9)
    if path_haus:
        # print(path_haus, 'path_haus')
        while path_haus:
            move_to_click(haus, 0)
            sleep(1.5)
            path_haus = pyautogui.locateCenterOnScreen('img/path_haus.png', confidence=0.9)
        out_haus = pyautogui.locateCenterOnScreen('img/go_out_haus.png', confidence=0.9)
        while not out_haus:
            sleep(0.1)
            out_haus = pyautogui.locateCenterOnScreen('img/go_out_haus.png', confidence=0.9)
        return 1
    else:
        pyautogui.move(20, 20)
        return 0


def to_house():
    # print('to_house')
    ik_haus = wait_and_stop_img('img/ik_haus.png')
    # sleep(2)
    # ik_haus = pyautogui.locateCenterOnScreen('img/ik_haus.png', confidence=0.9)
    # while not ik_haus:
    #     sleep(0.5)
    #     ik_haus = pyautogui.locateCenterOnScreen('img/ik_haus.png', confidence=0.9)

    return ik_haus


def find_sunduk():
    # print('find_sunduk')
    sleep(2)
    it = 0
    sunduk_1 = pyautogui.locateCenterOnScreen('img/sunduk_1.png', confidence=0.9)
    sunduk_2 = pyautogui.locateCenterOnScreen('img/sunduk_2.png', confidence=0.9)
    sunduk_3 = pyautogui.locateCenterOnScreen('img/sunduk_3.png', confidence=0.9)
    while not sunduk_1 and not sunduk_2 and not sunduk_3 and it < 5:
        # print(bool(sunduk_1), 'sunduk_1', bool(sunduk_2), 'sunduk_2', bool(sunduk_3), 'sunduk_3', it)
        sleep(1)
        it += 1
        sunduk_1 = pyautogui.locateCenterOnScreen('img/sunduk_1.png', confidence=0.9)
        sunduk_2 = pyautogui.locateCenterOnScreen('img/sunduk_2.png', confidence=0.9)
        sunduk_3 = pyautogui.locateCenterOnScreen('img/sunduk_3.png', confidence=0.9)
    if sunduk_1:
        return sunduk_1
    elif sunduk_2:
        return sunduk_2
    if sunduk_3:
        return sunduk_3
    else:
        return None


def go_out_haus():
    # print('go_out_haus')
    out_haus_img = wait_and_stop_img('img/go_out_haus.png')
    # sleep(2)
    # out_haus_img = pyautogui.locateCenterOnScreen('img/go_out_haus.png', confidence=0.9)
    # while not out_haus_img:
    #     sleep(0.1)
    #     out_haus_img = pyautogui.locateCenterOnScreen('img/go_out_haus.png', confidence=0.9)
    move_to_click(out_haus_img, 0)


def revision_of_house():
    hero_v_r_h = selection_hero()
    if hero_v_r_h:
        sum_vi = 0
        find_su = 0
        find_su_color = str(find_su)
        link = find_link_i()
        x, y = link
        y += 470
        x += 40
        friend = x, y
        move_to_click(friend, 0.3)
        sleep(1)
        ik_haus = to_house()
        move_to_click(ik_haus, 0.3)  # переход на экран домов
        while find_su < 10:  # sum_vi < 15 and
            vizit = go_in_haus()
            if vizit:
                sum_vi += 1
                sum_vi_color = str(sum_vi)
                sunduk = find_sunduk()
                if sunduk:
                    move_to_click(sunduk, 0.2)
                    find_su += 1
                    find_su_color = str(find_su)
                    close_img = wait_and_stop_img('img/everything/close.png', 0.89)
                    # close = pyautogui.locateCenterOnScreen('img/everything/close.png', confidence=0.89)
                    # sleep(0.2)
                    # close_1 = pyautogui.locateCenterOnScreen('img/everything/close.png', confidence=0.89)
                    # while not close or close != close_1:
                    #     sleep(0.1)
                    #     close = pyautogui.locateCenterOnScreen('img/everything/close.png', confidence=0.89)
                    #     sleep(0.1)
                    #     close_1 = pyautogui.locateCenterOnScreen('img/everything/close.png', confidence=0.89)
                    # sleep(2)
                    # close = pyautogui.locateCenterOnScreen('img/everything/close.png', confidence=0.89)
                    move_to_click(close_img, 0.3)
                print(m_t.text_blue(sum_vi_color), "осмотрено / найдено ", m_t.text_red(find_su_color))

                go_out_haus()
                if sum_vi < 14:
                    next_haus()
            else:
                sum_vi += 1
                sum_vi_color = str(sum_vi)
                print(m_t.text_blue(sum_vi_color), "/", m_t.text_red(find_su_color))
                next_haus()
        exit_to_fountain()
        return hero_v_r_h
