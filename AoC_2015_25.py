row, col = map(int, open('input_2015_25.txt', 'r', encoding='utf-8').readlines())
cd = 20151125
r = 0
c = 0
d = 0
while True:
    if c == d:
        d += 1
        r = d
        c = 0
    else:
        r -= 1
        c += 1
    cd = (cd * 252533) % 33554393
    if r+1 == row and c+1 == col:
        break
print(r+1, c+1, cd)
