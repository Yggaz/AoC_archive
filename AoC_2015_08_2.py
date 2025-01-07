# 1355 is too high
# 1350
import re
data = open('input_2015_08.txt', 'r', encoding='utf-8').read().splitlines()
char_lines = 0
char_memory = 0
char_extra = 0
for ln in data:
    old = ln
    char_lines += len(ln)
    ln = ln[1:-1].replace(r'\"', '"')
    ln = ln.replace(r'\\', '\\')
    # ASCII
    ln = re.sub(r"\\x[a-f,0-9][a-f,0-9]", 'X', ln)
    char_memory += len(ln)
    # Part 2
    # " -> \" - any quote gives +1 symbol
    q = old.count('"')
    # \ -> \\ - any slash gives +1 symbol
    s = old.count('\\')
    # quotes - any string has 2 symbols extra
    char_extra += q + s + 2
answer1 = char_lines - char_memory
answer2 = char_extra
print('Answer for part 1:', answer1)
print('Answer for part 2:', answer2)
