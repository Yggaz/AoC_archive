def how_many(eggnog, k = 0, used = 0) -> int:
    global min_used
    res = 0
    for i in range(k, len(containers)):
        if containers[i] == eggnog:
            res += 1
            if min_used > used + 1:
                min_used = used + 1
        elif containers[i] < eggnog:
            res += how_many(eggnog - containers[i], i + 1, used + 1)
    return res

def how_many_bis(eggnog, k = 0, used = 0) -> int:
    global min_used
    res = 0
    if used >= min_used:
        return 0
    for i in range(k, len(containers)):
        if containers[i] == eggnog:
            res += 1
        elif containers[i] < eggnog:
            res += how_many_bis(eggnog - containers[i], i + 1, used + 1)
    return res

min_used = 50
containers = sorted(list(map(int, open('input_2015_17.txt', 'r', encoding='utf-8').readlines())), reverse=True)
#containers = list((20, 15, 10, 5, 5))
#print(how_many(25))
#print(how_many_bis(25))
print(how_many(150))
print(how_many_bis(150))
