# 840 is too low
# 1771 is too low
# 4156 is too high

# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

def fight(mana_spent:int, player_hp:int, player_mana:int, boss_hp:int, shield:int, poison: int, recharge: int, turn:int, hard_mode:bool) -> int:
    #print('Player Turn:', turn, 'Player:', player_hp, 'Mana:', player_mana, 'Boss:', boss_hp, 'Shield left:', shield, 'Poison left:', poison, 'Recharge left:', recharge)
    global boss_dmg
    p_hp = player_hp
    p_mana = player_mana
    b_hp = boss_hp
    new_shield = shield
    new_poison = poison
    new_recharge = recharge
    # 1. Boss turn
    if turn > 1:
        # effects
        if new_poison > 0:
            b_hp -= 3
            new_poison -= 1
            if b_hp <= 0:
                # victory!
                # #print('Turn:', turn - 1, 'Victory - boss died from poison (boss turn)')
                return mana_spent
        if new_shield > 0:
            new_shield -= 1
            boss_damage = boss_dmg - 7
        else:
            boss_damage = boss_dmg
        p_hp -= boss_damage
        if p_hp <= 0:
            # loss!
            # #print('Turn:', turn - 1, 'loss - player killed')
            return 100000
        if new_recharge > 0:
            p_mana += 101
            new_recharge -= 1
    # 2. Player_turn
    # hard mode
        if hard_mode:
            p_hp -= 1
            if p_hp <= 0:
                # loss!
                # #print('Turn:', turn, 'loss - player died (hard mode)')
                return 100000
    # effects
        if new_poison > 0:
            b_hp -= 3
            new_poison -= 1
            if b_hp <= 0:
                # victory!
                # #print('Turn:', turn, 'Victory - boss died from poison (player turn)')
                return mana_spent
        if new_shield > 0:
            new_shield -= 1
        if new_recharge > 0:
            p_mana += 101
            new_recharge -= 1
    # Player move.
    # cast Magic missile!
    if p_mana >= 53:
        #print('Turn:', turn,'Cast Magic missile!')
        if b_hp <= 4:
            #victory!
            #print('Turn:', turn, 'Victory - boss killed by magic missile')
            return mana_spent + 53
        res1 = fight(mana_spent + 53, p_hp, p_mana - 53, b_hp - 4, new_shield, new_poison, new_recharge, turn + 2, hard_mode)
    else:
        res1 = 100000
    # cast Drain!
    if p_mana >= 73:
        #print('Turn:', turn,'Cast Drain!')
        if b_hp <= 2:
            #victory!
            #print('Turn:', turn, 'Victory - boss killed by drain')
            return mana_spent + 73
        res2 = fight(mana_spent + 73, p_hp + 2, p_mana - 73, b_hp - 2, new_shield, new_poison, new_recharge, turn + 2, hard_mode)
    else:
        res2 = 100000
    # Cast Shield!
    if p_mana >= 113 and new_shield == 0:
        #print('Turn:', turn,'Cast Shield!')
        res3 = fight(mana_spent + 113, p_hp, p_mana - 113, b_hp, 6, new_poison, new_recharge, turn + 2, hard_mode)
    else:
        res3 = 100000
    # Cast Poison!
    if p_mana >= 173 and new_poison == 0:
        #print('Turn:', turn,'Cast Poison!')
        res4 = fight(mana_spent + 173, p_hp, p_mana - 173, b_hp, new_shield, 6, new_recharge, turn + 2, hard_mode)
    else:
        res4 = 100000
    # Cast Recharge!
    if p_mana >= 229 and new_recharge == 0:
        #print('Turn:', turn,'Cast Recharge!')
        res5 = fight(mana_spent + 229, p_hp, p_mana - 229, b_hp, new_shield, new_poison, 5, turn + 2, hard_mode)
    else:
        res5 = 100000
        if min(res1, res2, res3, res4, res5) >= 100000:
            # loss!
            #print('Turn:', turn, 'loss - no victory!')
            pass
    return min(res1, res2, res3, res4, res5)


text = open('input_2015_22.txt', 'r', encoding='utf-8').readlines()
boss_hp = int(text[0].split(':')[1])
boss_dmg = int(text[1].split(':')[1])
player_hp = 50
player_mana = 500
#boss_hp = 14
#boss_dmg = 8
#player_hp = 10
#player_mana = 250
print('boss_hp', boss_hp)
print('boss_dmg', boss_dmg)
part1 = fight(0, player_hp, player_mana, boss_hp, 0, 0, 0, 1, False)
part2 = fight(0, player_hp, player_mana, boss_hp, 0, 0, 0, 1, True)
print('Part 1 answer:', part1)
print('Part 2 answer:', part2)