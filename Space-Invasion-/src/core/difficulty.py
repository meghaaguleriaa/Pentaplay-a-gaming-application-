def get_enemy_speed(wave):
    return min(2 + (wave - 1) * 0.1, 3)


def get_shoot_interval(wave):
    return max(1200 - (wave - 1) * 50, 850)


def get_max_shooters(wave):
    return min(2 + (wave - 1) // 5, 3)