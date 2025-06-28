import datetime
import baza_dannyx as b_d


class Hero:

    def __init__(self, name, task_gold, task_xp, energy_sum, name_in_file=None):
        self.name = name
        self.energy_status = 0  # переменная
        self.case_status = 0
        self.guru_status = 0
        self.gift_status = 0
        self.game_status = 0
        self.task_gold = task_gold
        self.task_xp = task_xp
        self.is_raid_today = False
        self.name_in_file = name_in_file

        self.energy_sum = energy_sum # общее значение энергии при старте суток
        self.energy_count_now = 0 # потрачено сегодня
        self.energy_count_all = 0  # потрачено всего
        self.energy_task_value = 0 # потрачено на задание

        # к-в боёв общее
        self.qty_all = 0
        # к-во боёв в текущей кв
        self.qty_kv_all = 0

        # к-во побед общее
        self.qty_all_victory = 0
        #  к-во побед в текущей кв
        self.qty_kv_victory = 0

        # час старта кв
        self.hour_start_kv = 0
        #
        self.hour_start_kv_ver = 0

        # дата старта кв
        self.date_start_kv = 0
        # #
        self.isolation_end_date = 0

    def get_qty_all_victory(self):
        return self.qty_all_victory

    def get_qty_all(self):
        return self.qty_all

    def get_name(self):
        return f' {self.name}'

    def get_task_gold(self):
        return self.task_gold

    def get_task_xp(self):
        return self.task_xp

    def get_isolation_end_date(self):
        return self.isolation_end_date

    def get_en_sum(self):
        return self.energy_sum

    def get_en_now(self):
        return self.energy_count_now

    def get_hero_name_in_file(self):
        return self.name_in_file

    def get_energy_count_all(self):
        return self.energy_count_all

    def set_energy_count_all(self, value):
        self.energy_count_all += value

    def set_en_now(self, value):
        self.energy_count_now += value

    def set_duel_qty(self):
        self.qty_all += 1
        self.qty_kv_all += 1

    def set_isolation_end_date(self):
        day_now = datetime.datetime.now()
        self.isolation_end_date = day_now + datetime.timedelta(days=10)
        print(f'установлен карантин на 10 дней для {Hero.get_name(Active.hero_activ)}')



Gady = Hero('Гадя', b_d.tasks_gold_v, b_d.tasks_xp_v, energy_sum=b_d.gady_energy_sum, name_in_file='gady')
Gavr = Hero('Гавр', b_d.tasks_gold_gavr, b_d.tasks_xp_gavr, energy_sum=b_d.gavr_energy_sum, name_in_file='gavr')
Veles = Hero('Велес', b_d.tasks_gold_vel, b_d.tasks_xp_vel, energy_sum=b_d.veles_energy_sum, name_in_file='veles')
Mara = Hero('Мара', b_d.tasks_gold_mar, b_d.tasks_xp_mar, energy_sum=b_d.mara_energy_sum, name_in_file='mara')


class Active:
    hero_activ = None
    check_date = ''
    date_now = ''
    max_time_wait_load = 8
    max_time_wait_id = 9

# Hero.get_qty_all_victory(Active.hero_activ)
