# 3272728 is too high
# 776160 is too low
trg = 36000000
mul = 10
mul2 = 11
primes = list()

def sigma(n:int) -> int:
    s = 1 + n
    tst = 2
    while tst * tst <= n:
        if n % tst == 0:
            s += tst
            if tst * tst < n:
                s += n // tst
        tst += 1
    return s

def sigma_bis(n:int) -> int:
    s = n
    tst = 2
    while tst * tst <= n:
        if n % tst == 0:
            if tst * 50 >= n:
                s += tst
            if tst * tst < n:
                tst_p = n // tst
                if tst_p * 50 >= n:
                    s += tst_p
        tst += 1
    return s


cur = 800000
while sigma(cur)*mul < trg:
    cur += 1
print('Part 1 answer:', cur)


cur = 750000
while sigma_bis(cur) * mul2 < trg:
    cur += 1
print('Part 2 answer:', cur)
#cur = 776160
#print('Result:', sigma_bis(cur))
