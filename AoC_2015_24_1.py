from itertools import combinations
from math import prod

def find_combinations(r = 5):
    global packages, target_sum
    result = []
    for combo in combinations(packages, r):
        if sum(combo) == target_sum:
            result.append(combo)
    return result


packages = list(map(int, open('input_2015_24.txt', 'r', encoding='utf-8').readlines()))
target_sum = sum(packages) // 3

cur_best = 5
while True:
    combinations_found = find_combinations(cur_best)
    if len(combinations_found) > 0:
        break
    else:
        cur_best += 1

best_qe = max(packages) ** 5
for combo in combinations_found:
    cur_qe = prod(combo)
    if cur_qe < best_qe:
        best_qe = cur_qe
print('Part 1 answer:', best_qe)

target_sum = sum(packages) // 4

cur_best = 4
while True:
    combinations_found = find_combinations(cur_best)
    if len(combinations_found) > 0:
        break
    else:
        cur_best += 1

best_qe = max(packages) ** 6
for combo in combinations_found:
    cur_qe = prod(combo)
    if cur_qe < best_qe:
        best_qe = cur_qe
print('Part 2 answer:', best_qe)
