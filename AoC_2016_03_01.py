triangles = 0
triangles_2 = 0
data = open('input_2016_03.txt', 'r', encoding='utf-8').readlines()
column = 0
t1 = list()
t2 = list()
t3 = list()
for ln in data:
    raw = list(map(int, ln.split()))
    row = sorted(raw)
    triangles += 1 if row[2] < row[1] + row[0] else 0
    t1.append(raw[0])
    t2.append(raw[1])
    t3.append(raw[2])
    if column == 2:
        column = 0
        t1.sort()
        t2.sort()
        t3.sort()
        triangles_2 += 1 if t1[2] < t1[1] + t1[0] else 0
        triangles_2 += 1 if t2[2] < t2[1] + t2[0] else 0
        triangles_2 += 1 if t3[2] < t3[1] + t3[0] else 0
        t1 = list()
        t2 = list()
        t3 = list()
    else:
        column += 1
print('Answer for part 1:', triangles)
print('Answer for part 2:', triangles_2)
