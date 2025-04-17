import datetime
import baza_dannyx as b_d


class Hero:

    def __init__(self, name, task_gold, task_xp):
        self.name = name
        self.energy_status = 0
        self.case_status = 0
        self.guru_status = 0
        self.gift_status = 0
        self.game_status = 0
        self.task_gold = task_gold
        self.task_xp = task_xp
        self.is_raid_today = False

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

    def set_duel_qty(self):
        self.qty_all += 1
        self.qty_kv_all += 1

    def set_isolation_end_date(self):
        day_now = datetime.datetime.now()
        self.isolation_end_date = day_now + datetime.timedelta(days=10)
        print(f'установлен карантин на 10 дней для {Hero.get_name(Active.hero_activ)}')



Gady = Hero('Гадя', b_d.tasks_gold_v, b_d.tasks_xp_v)
Gavr = Hero('Гавр', b_d.tasks_gold_gavr, b_d.tasks_xp_gavr)
Veles = Hero('Велес', b_d.tasks_gold_vel, b_d.tasks_xp_vel)
Mara = Hero('Мара', b_d.tasks_gold_mar, b_d.tasks_xp_mar)


class Active:
    hero_activ = None

# Hero.get_qty_all_victory(Active.hero_activ)
