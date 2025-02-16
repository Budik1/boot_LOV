import datetime


class Hero:

    def __init__(self, name=None):
        self.name = name
        self.energy_status = 0
        self.case_status = 0
        self.guru_status = 0
        self.gift_status = 0
        self.game_status = 0

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

        self.isolation_end_date = 0

        # print('установлена старт дата')
        # print(f'Hero {self} kreate')

    def get_qty_all_victory(self):
        return self.qty_all_victory

    def get_qty_all(self):
        return self.qty_all

    # def get_percent_victory_kv(self):
    #     return round()

    def set_duel_qty(self):
        self.qty_all += 1
        self.qty_kv_all += 1

    def introduce(self):
        print(f'меня зовут {self.name}')


Gady = Hero('Гадя')
Gavr = Hero('Гавр')
Veles = Hero('Велес')
Mara = Hero('Мара')


class Active:
    hero_activ = None


# Hero.get_qty_all_victory(Active.hero_activ)
