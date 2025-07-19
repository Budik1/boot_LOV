import os





# Указываем путь к директории
directory = "C:/py_bot/boot_LOV_2/img/energy/lvl"
# Получаем список файлов
files = os.listdir(directory)
# Выводим список файлов
print(files)
lvl_dig_list = []
for name in files:
    dig = extraction_digit(item=name)
    lvl_dig_list.append(dig)
print(lvl_dig_list)