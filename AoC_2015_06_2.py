import numpy as np
lamps = np.zeros((1000, 1000), dtype=np.int64)
for ln in open('input_2015_06.txt', 'r', encoding='utf-8').read().splitlines():
    match ln[:7]:
        case 'turn on':
            lights = ln[8:].split(' through ')
            f = list(map(int, lights[0].split(',')))
            t = list(map(int, lights[1].split(',')))
            lamps[f[0]:t[0]+1, f[1]:t[1]+1] += 1
        case 'turn of':
            lights = ln[9:].split(' through ')
            f = list(map(int, lights[0].split(',')))
            t = list(map(int, lights[1].split(',')))
            lamps[f[0]:t[0]+1, f[1]:t[1]+1] -= 1
            wrong = np.where(lamps < 0)
            lamps[wrong] = 0
        case 'toggle ':
            lights = ln[7:].split(' through ')
            f = list(map(int, lights[0].split(',')))
            t = list(map(int, lights[1].split(',')))
            lamps[f[0]:t[0]+1, f[1]:t[1]+1] += 2
answer2 = np.sum(lamps)
print('Answer for Part 2:', answer2)
