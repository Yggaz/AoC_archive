visited, visited2 = set(), set()
santa = [0, 0]
santa2 = [0, 0]
robo = [0, 0]
visited.add((santa[0], santa[1]))
visited2.add((santa[0], santa[1]))
moves = {'^':(-1, 0), 'v':(1, 0), '<':(0, -1), '>':(0, 1)}
cmd = open('input_2015_03.txt', 'r', encoding='utf-8').read().strip()
for i in range(len(cmd)):
    santa[0] += moves[cmd[i]][0]
    santa[1] += moves[cmd[i]][1]
    visited.add((santa[0], santa[1]))
    if i % 2 == 0:
        santa2[0] += moves[cmd[i]][0]
        santa2[1] += moves[cmd[i]][1]
        visited2.add((santa2[0], santa2[1]))
    else:
        robo[0] += moves[cmd[i]][0]
        robo[1] += moves[cmd[i]][1]
        visited2.add((robo[0], robo[1]))
answer1 = len(visited)
print("Part 1 answer:", answer1)
answer2 = len(visited2)
print("Part 2 answer:", answer2)
