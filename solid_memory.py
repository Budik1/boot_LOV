import pickle
import heroes as her
import my_color_text as mct

def setting_updatable_value(*, read_date):
    her.Gady.energy_count_used_now = read_date['Gady.energy_count_used_now']
    her.Gavr.energy_count_used_now = read_date['Gavr.energy_count_used_now']
    her.Veles.energy_count_used_now = read_date['Veles.energy_count_used_now']
    her.Mara.energy_count_used_now = read_date['Mara.energy_count_used_now']

    her.Gady.energy_sum = read_date['Gady.energy_sum']
    her.Gavr.energy_sum = read_date['Gavr.energy_sum']
    her.Veles.energy_sum = read_date['Veles.energy_sum']
    her.Mara.energy_sum = read_date['Mara.energy_sum']

    her.Gavr.energy_status = read_date['Гавр-энергия']
    her.Gady.energy_status = read_date['Гадя-энергия']
    her.Veles.energy_status = read_date['Велес-энергия']
    her.Mara.energy_status = read_date['Мара-энергия']

    her.Gavr.case_status = read_date['Гавр-кейс']
    her.Gady.case_status = read_date['Гадя-кейс']
    her.Veles.case_status = read_date['Велес-кейс']
    her.Mara.case_status = read_date['Мара-кейс']

    her.Gady.guru_status = read_date['Гадя-гуру']
    her.Gavr.guru_status = read_date['Гавр-гуру']
    her.Veles.guru_status = read_date['Велес-гуру']
    her.Mara.guru_status = read_date['Мара-гуру']

    her.Gady.gift_status = read_date['Гадя-gift']
    her.Gavr.gift_status = read_date['Гавр-gift']
    her.Veles.gift_status = read_date['Велес-gift']
    her.Mara.gift_status = read_date['Мара-gift']

    her.Gady.game_status = read_date['Гадя-кости']
    her.Gavr.game_status = read_date['Гавр-кости']
    her.Veles.game_status = read_date['Велес-кости']
    her.Mara.game_status = read_date['Мара-кости']

    her.Gady.isolation_end_date = read_date['Гадя-дата-конца карантина']
    her.Gavr.isolation_end_date = read_date['Гавр-дата-конца карантина']
    her.Veles.isolation_end_date = read_date['Велес-дата-конца карантина']
    her.Mara.isolation_end_date = read_date['Мара-дата-конца карантина']


def setting_cumulative_value(*, read_data):
    pass

def save_to_file():
    # создаётся библиотека содержащая значения состояние событий
    data_to_save = {
        'дата': her.Active.date_now,

        'Gady.energy_sum': her.Gady.energy_sum,
        'Gavr.energy_sum': her.Gavr.energy_sum,
        'Veles.energy_sum': her.Veles.energy_sum,
        'Mara.energy_sum': her.Mara.energy_sum,

        'Gady.energy_count_used_now': her.Gady.energy_count_used_now,
        'Gavr.energy_count_used_now': her.Gavr.energy_count_used_now,
        'Veles.energy_count_used_now': her.Veles.energy_count_used_now,
        'Mara.energy_count_used_now': her.Mara.energy_count_used_now,

        'Гадя-энергия': her.Gady.energy_status,
        'Гавр-энергия': her.Gavr.energy_status,
        'Велес-энергия': her.Veles.energy_status,
        'Мара-энергия': her.Mara.energy_status,

        'Гадя-кейс': her.Gady.case_status,
        'Гавр-кейс': her.Gavr.case_status,
        'Велес-кейс': her.Veles.case_status,
        'Мара-кейс': her.Mara.case_status,

        'Гадя-гуру': her.Gady.guru_status,
        'Гавр-гуру': her.Gavr.guru_status,
        'Велес-гуру': her.Veles.guru_status,
        'Мара-гуру': her.Mara.guru_status,

        'Гадя-gift': her.Gady.gift_status,
        'Гавр-gift': her.Gavr.gift_status,
        'Велес-gift': her.Veles.gift_status,
        'Мара-gift': her.Mara.gift_status,

        'Гадя-кости': her.Gady.game_status,
        'Гавр-кости': her.Gavr.game_status,
        'Велес-кости': her.Veles.game_status,
        'Мара-кости': her.Mara.game_status,

        'Гадя-дата-конца карантина': her.Gady.isolation_end_date,
        'Гавр-дата-конца карантина': her.Gavr.isolation_end_date,
        'Велес-дата-конца карантина': her.Veles.isolation_end_date,
        'Мара-дата-конца карантина': her.Mara.isolation_end_date,
    }
    print('запись')
    # print(f'{her.Gady.isolation_end_date} для Гади')
    # print(f'{her.Gavr.isolation_end_date} для Гавра')
    # print(f'{her.Veles.isolation_end_date} для Велеса')
    # print(f'{her.Mara.isolation_end_date} для Мары')
    file1 = open('config.txt', 'wb')
    pickle.dump(data_to_save, file1)
    file1.close()


def reading_file():
    try:
        file1 = open('config.txt', 'rb')
        data_to_load = pickle.load(file1)
        file1.close()
        result = True, data_to_load
        setting_updatable_value(read_date=data_to_load)
        setting_cumulative_value(read_data=data_to_load)
    except:
        print(mct.tc_red('Config поврежден или не создан)))'))
        result = False, False
        save_to_file()
    return result
