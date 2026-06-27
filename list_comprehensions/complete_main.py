def get_critical_hits(damage_rolls):
    return [roll * 2 for roll in damage_rolls if roll >= 50]
