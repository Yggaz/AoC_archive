text = open('input_2015_21.txt', 'r', encoding='utf-8').readlines()
boss_hp = int(text[0].split(':')[1])
boss_dmg = int(text[1].split(':')[1])
boss_armor = int(text[2].split(':')[1])
weapons = range(4,12)
weapon_low_costs = [8, 10, 25, 40, 65, 90, 124, 174]
for i, w in enumerate(weapons):
    damage_dealt = w - boss_armor
    turns_to_victory = boss_hp // damage_dealt
    if damage_dealt * turns_to_victory < boss_hp:
        turns_to_victory += 1
    damage_limit = damage_dealt
    target_def = boss_dmg - damage_dealt
    if target_def < 0:
        target_def = 0
    print("Sword ", i, "(", weapon_low_costs[i], ")",  " dmg: ", damage_dealt, "  Turns to fight: ", turns_to_victory, " Target def:", target_def)

# Too difficult to program
