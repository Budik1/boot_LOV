from colorama import init, Fore, Style

init()


def text_red(text):
    text_color_red = Fore.RED + text + Style.RESET_ALL
    return text_color_red


def text_green(text):
    text_color_green = Fore.GREEN + text + Style.RESET_ALL
    return text_color_green


def text_yellow(text):
    text_color_yellow = Fore.YELLOW + text + Style.RESET_ALL
    return text_color_yellow


def text_blue(text):
    text_color_blue = Fore.BLUE + text + Style.RESET_ALL
    return text_color_blue


def text_magenta(text):
    text_color_magenta = Fore.MAGENTA + text + Style.RESET_ALL
    return text_color_magenta


def text_cyan(text):
    text_color_cyan = Fore.CYAN + text + Style.RESET_ALL
    return text_color_cyan
