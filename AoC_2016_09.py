from functools import cache

@cache
def decompress(s:str)->int:
    ob = s.find('(')
    if ob < 0:
        return len(s)
    else:
        cb = s.find(')')
        trg = tuple(map(int, s[ob + 1:cb].split('x')))
        p1 = s[cb+1:cb+1+trg[0]]
        res = len(s[:ob]) + trg[1] * decompress(p1) + decompress(s[cb+1+trg[0]:])
        return res


data = open('input_2016_09.txt', 'r', encoding='utf-8').readlines()
ln = data[0]
res_line = ''
while len(ln) > 0:
    ob = ln.find('(')
    if ob < 0:
        res_line += ln
        ln = ''
    else:
        cb = ln.find(')')
        if cb < 0:
            res_line += ln
            ln = ''
        else:
            res_line += ln[:ob]
            target = tuple(map(int, ln[ob+1:cb].split('x')))
            to_repeat = ln[cb+1:cb+1+target[0]]
            for i in range(target[1]):
                res_line += to_repeat
            ln = ln[cb+1+target[0]:]
res1 = len(res_line)
res2 = decompress(data[0])
print('Part 1 answer:', res1)
print('Part 2 answer:', res2)
print(decompress.cache_info())
