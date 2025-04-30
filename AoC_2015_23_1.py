def step(addr: int) -> int:
    global prg, memory
    if addr >= len(prg):
        return -1
    elif prg[addr][0] == 'jmp':
        res = addr + prg[addr][2]
    elif prg[addr][0] == 'hlf':
        memory[prg[addr][1]] = memory[prg[addr][1]] // 2
        res = addr + 1
    elif prg[addr][0] == 'tpl':
        memory[prg[addr][1]] *= 3
        res = addr + 1
    elif prg[addr][0] == 'jie':
        if memory[prg[addr][1]] % 2 == 0:
            res = addr + prg[addr][2]
        else:
            res = addr + 1
    elif prg[addr][0] == 'jio':
        if memory[prg[addr][1]] == 1:
            res = addr + prg[addr][2]
        else:
            res = addr + 1
    elif prg[addr][0] == 'inc':
        memory[prg[addr][1]] += 1
        res = addr + 1
    return res


prg_text = open('input_2015_23.txt', 'r', encoding='utf-8').readlines()
prg = list()
for rw in prg_text:
    prt = rw.split()
    cmd = prt[0]
    if cmd == 'jmp':
        reg = ''
        offset = int(prt[1])
    elif len(prt[1]) > 1:
        reg = prt[1][0]
        offset = int(prt[2])
    else:
        reg = prt[1]
        offset = 0
    prg.append((cmd, reg, offset))

memory = {'a':0, 'b': 0}
s = 0
while s >= 0:
    s = step(s)
print('Part 1 answer:', memory['b'])
memory['a'] = 1
memory['b'] = 0
s = 0
while s >= 0:
    s = step(s)
print('Part 2 answer:', memory['b'])

