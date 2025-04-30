class GameState:
    def __init__(self, p_hp, p_mana, b_hp, b_dmg, tcks = 0, spent = 0):
        self.player_hp = p_hp
        self.player_mana = p_mana
        self.boss_hp = b_hp
        self.boss_dmg = b_dmg
        self.game_ticks = tcks
        self.mana_spent = spent
        self.drain_ticks = 0
        self.poison_ticks = 0
        self.recharge_ticks = 0

    def


text = open('input_2015_21.txt', 'r', encoding='utf-8').readlines()
boss_hp = int(text[0].split(':')[1])
boss_dmg = int(text[1].split(':')[1])
start_pos = GameState(50, 500, boss_hp, boss_dmg)
