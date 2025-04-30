data = open('input_2016_01.txt', 'r', encoding='utf-8').read().split(', ')
left_turn = {'N':'E', 'W':'N', 'S':'W', 'E':'S'}
right_turn = {'N':'W', 'W':'S', 'S':'E', 'E':'N'}
step = {'N':(1, 0), 'W':(0, -1), 'S':(-1, 0), 'E':(0, 1)}
dir = 'N'
posX = 0
posY = 0
visited = set()
visited.add((posX, posY))
p2solved = False
for cmd in data:
    trn = cmd[:1]
    if trn == 'L':
        dir = left_turn[dir]
    else:
        dir = right_turn[dir]
    mv = int(cmd[1:])
    for p in range(mv):
        posX += step[dir][0]
        posY += step[dir][1]
        if not p2solved and (posX, posY) in visited:
            print('Part 2 answer:', abs(posX) + abs(posY))
            p2solved = True
        else:
            visited.add((posX, posY))
print('Part 1 answer:', abs(posX) + abs(posY))
