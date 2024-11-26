from fun import loc_center_img, move_to_click
import pyautogui


def backpack():
    gadya = loc_center_img('img/hero/h_gadya.png')
    move_to_click(gadya, 0)


