# Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
def next_char(char):
    return chr(ord(char) + 1)

def next_passw(passw):
    rev = passw[::-1]
    l = 0
    while rev[l] == 'z':
        l +=1
    res = 'a' * l + next_char(rev[l]) + rev[l+1:len(rev)]
    return res[::-1]

def rule1(passw):
    heads = set()
    for l in range(len(passw) - 2):
        if passw[l+1] == next_char(passw[l]) and passw[l+2] == next_char(passw[l+1]):
            heads.add(l)
    return bool(heads)

def rule2(passw):
    passed = True
    for l in range(len(passw)):
        passed = passed and passw[l] != 'i' and passw[l] != 'o'  and passw[l] != 'l'
        if not passed:
            break
    return passed

def rule3(passw):
    heads = set()
    for l in range(len(passw) - 1):
        if passw[l] == passw[l + 1]:
            heads.add(l)
    if heads:
        res = (max(heads) - min(heads)) > 1
    else:
        res = False
    return res

def next_good_passw(passw):
    found = False
    tst = passw
    while not found:
        tst = next_passw(tst)
        found = rule1(tst) and rule2(tst) and rule3(tst)
    return tst

print(next_good_passw('vzbxkghb'))
print(next_good_passw(next_good_passw('vzbxkghb')))

