from fun import locCenterImg, move_to_click
import pyautogui


def backpack():
    gadya = locCenterImg('img/hero/h_gadya.png')
    move_to_click(gadya, 0)


