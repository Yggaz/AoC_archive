def abba(list_in: list) -> bool:
    for e in list_in:
        for i in range(len(e) - 3):
            if e[i] == e[i+3] and e[i+1] == e[i+2] and not (e[i] == e[i+1]):
                return True
    return False

def bab(list_out, what) -> bool:
    for e in list_out:
        for i in range(len(e) - 2):
            if e[i] == e[i+2] and e[i] == what[1] and e[i+1] == what[0]:
                return True
    return False

def aba(list_in, list_out:list) -> bool:
    for e in list_in:
        for i in range(len(e) - 2):
            if e[i] == e[i+2] and not (e[i] == e[i+1]):
                if bab(list_out, e[i] + e[i+1] + e[i+2]):
                    return True
    return False

data = open('input_2016_07.txt', 'r', encoding='utf-8').readlines()
ans1 = 0
ans2 = 0
for ln in data:
    tsk = ln.strip().replace(']','[').split('[')
    s_out = list()
    s_in = list()
    for k, s in enumerate(tsk):
        if k % 2 == 0:
            s_out.append(s)
        else:
            s_in.append(s)
    if abba(s_out) and not abba(s_in):
        ans1 += 1
    if aba(s_out, s_in):
        ans2 += 1
print('Answer for part 1:', ans1)
print('Answer for part 2:', ans2)
