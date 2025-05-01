hex_chars = '0123456789ABCDEF'
dir_1 = {}
dir_2 = {}
for i in range(1, 10):
    if i > 3:
       dir_1[(i, 'U')] = i - 3
    if i < 7:
        dir_1[(i, 'D')] = i + 3
    if i not in (1, 4, 7):
        dir_1[(i, 'L')] = i - 1
    if i not in (3, 6, 9):
        dir_1[(i, 'R')] = i + 1

for i in range(1, 14):
    if i in (6, 7, 8, 10, 11, 12):
        dir_2[(i, 'U')] = i - 4
    if i in (3, 13):
        dir_2[(i, 'U')] = i - 2
    if i in (2, 3, 4, 6, 7, 8):
        dir_2[(i, 'D')] = i + 4
    if i in (1, 11):
        dir_2[(i, 'D')] = i + 2
    if i in (3, 4, 6, 7, 8, 9, 11, 12):
        dir_2[(i, 'L')] = i - 1
    if i in (2, 3, 5, 6, 7, 8, 10, 11):
        dir_2[(i, 'R')] = i + 1

data = open('input_2016_02.txt', 'r', encoding='utf-8').read().splitlines()
code_1 = 0
code_2 = ''
cur_button = 5
for ln in data:
    for l in range(len(ln)):
        if (cur_button, ln[l]) in dir_1.keys():
            cur_button = dir_1[(cur_button, ln[l])]
    code_1 = code_1 * 10 + cur_button
cur_button = 5
for ln in data:
    for l in range(len(ln)):
        if (cur_button, ln[l]) in dir_2.keys():
            cur_button = dir_2[(cur_button, ln[l])]
    code_2 += hex_chars[cur_button]

print('Part 1 answer:', code_1)
print('Part 2 answer:', code_2)

