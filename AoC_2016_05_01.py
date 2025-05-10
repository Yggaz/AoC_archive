from hashlib import md5
passw = ''
passw2 = list('_' * 8)
d = 0
j = 1469590
while d < 8:
    j+= 1
    #md5_value = md5(('abc'+str(j)).encode()).hexdigest()
    md5_value = md5(('ojvtpuvg'+str(j)).encode()).hexdigest()
    if md5_value[0:5] == '00000':
        print(j)
        sym = md5_value[5]
        if len(passw) < 8:
            passw += sym
        if sym < '8':
            p = int(sym)
            if passw2[p] == '_':
                passw2[p] = md5_value[6]
                d += 1
answer2 = ''
for d in passw2:
    answer2 += d
print('Part 1 answer:', passw)
print('Part 2 answer:', answer2)