# 1355 is too high
# 1350
import re
data = open('input_2015_08.txt', 'r', encoding='utf-8').read().splitlines()
char_lines = 0
char_memory = 0
for ln in data:
    char_lines += len(ln)
    # ASCII
    asc = re.finditer(r"\\x[a-f,0-9][a-f,0-9]", ln[1:-1], re.IGNORECASE)
    a = 0
    for m in asc:
        # print(m.span(), ':', m.group())
        a += 4 - 1
    # \"
    quote = re.finditer(r"\\\"", ln[1:-1])
    b = 0
    for m in quote:
        # print(m.span(), ':', m.group())
        b += 2 - 1
    # \\
    slash = re.finditer(r"\\\\", ln[1:-1])
    c = 0
    for m in slash:
        # print(m.span(), ':', m.group())
        c += 2 - 1
    char_memory += len(ln) - (a + b + c + 2)
    # print('string: ', ln)
    # print('input:  ', len(ln))
    # print('minus:  ', a + b + c + 2)
    # print('memory: ', len(ln) - (a + b + c + 2))
answer1 = char_lines - char_memory
print('Answer for part 1:', answer1)
