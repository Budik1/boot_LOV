from colorama import init, Fore, Style

init()


def tc_red(text):
    text_color_red = Fore.RED + text + Style.RESET_ALL
    return text_color_red


def tc_green(text):
    text_color_green = Fore.GREEN + text + Style.RESET_ALL
    return text_color_green


def tc_yellow(text):
    text_color_yellow = Fore.YELLOW + text + Style.RESET_ALL
    return text_color_yellow


def tc_blue(text):
    text_color_blue = Fore.BLUE + text + Style.RESET_ALL
    return text_color_blue


def tc_magenta(text):
    text_color_magenta = Fore.MAGENTA + text + Style.RESET_ALL
    return text_color_magenta


def tc_cyan(text):
    text_color_cyan = Fore.CYAN + text + Style.RESET_ALL
    return text_color_cyan
