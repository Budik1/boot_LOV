from heroes import Hero, Active

def about_energy_costs_for_the_task(*, value_energy):
    return (f'потрачено сейчас {value_energy}, '
            f'сегодня {Hero.get_en_now(Active.hero_activ)} '
            f'из {Hero.get_en_sum(Active.hero_activ)}, '
            f'всего {Hero.get_energy_count_all(Active.hero_activ)}')
