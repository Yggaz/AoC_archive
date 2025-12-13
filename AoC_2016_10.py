bots = dict()
directions = dict()
set1 = set()
set2 = set()
fires = []

def give(bot: int, what: int):
    global bots
    bots.setdefault(bot, []).append(what)


def action(bot:int):
    #print('Bot', bot, 'acts!')
    global bots, directions, min1st, max1st
    n1 = min(bots[bot][0], bots[bot][1])
    n2 = max(bots[bot][0], bots[bot][1])
    if len(bots.get(bot, [])) == 2:
        if (n1, n2) == (min1st, max1st):
            print('Part 1 answer:', bot)
        l = directions[bot][0]
        h = directions[bot][1]
        give(h, n2)
        give(l, n1)
        bots[bot] = []

min1st = 17
max1st = 61

data = open('input_2016_10.txt', 'r', encoding='utf-8').readlines()
for lin in data:
    ln = lin.strip().split()
    if ln[0] == 'bot':
        #directions
        # bot 77 gives low to bot 104 and high to bot 203
        #   0  1     2   3  4   5   6   7    8  9  10  11
        bt = int(ln[1])
        lv = int(ln[6]) + (0 if ln[5] == 'bot' else 1000)
        hv = int(ln[11]) + (0 if ln[10] == 'bot' else 1000)
        directions[bt] = tuple((lv, hv))
for lin in data:
    ln = lin.strip().split()
    if ln[0] == 'value':
        # value 53 goes to bot 119
        #     0  1    2  3   4   5
        give(int(ln[5]), int(ln[1]))
move = True
while move:
    move = False
    k = next((key for key, value in bots.items() if len(value) == 2 and key < 1000), None)
    if k is not None:
        move = True
        action(k)

res2 = bots[1000][0] * bots[1001][0] * bots[1002][0]
print('Part 2 answer:', res2)
