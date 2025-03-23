from copy import deepcopy
def draw_field():
    global field, SIZE
    for rw in range(SIZE):
        maze_line = ""
        for cl in range(SIZE):
            if field[rw][cl] == 1:
                maze_line += "#"
            else:
                maze_line += "."
        print(maze_line)
    print()

def neighbors(r: int, c: int) -> int:
    global field, SIZE
    res = 0 if r == 0 or c == 0 else field[r-1][c-1]
    res += 0 if r == 0 else field[r-1][c]
    res += 0 if r == 0 or c == SIZE - 1 else field[r-1][c+1]
    res += 0 if c == 0 else field[r][c - 1]
    res += 0 if c == SIZE - 1 else field[r][c + 1]
    res += 0 if r == SIZE - 1 or c == 0 else field[r + 1][c - 1]
    res += 0 if r == SIZE - 1 else field[r + 1][c]
    res += 0 if r == SIZE - 1 or c == SIZE - 1 else field[r + 1][c + 1]
    return res

def new_generation():
    global field, SIZE
    new_field = list()
    for r in range(SIZE):
        row = list()
        for c in range(SIZE):
            n = neighbors(r, c)
            if n < 2 or n > 3: # 0 regardless of previous value
                row.append(0)
            elif n == 3: # 1 regardless of previous value
                row.append(1)
            else: # n == 2 - previous value
                row.append(field[r][c])
        new_field.append(row)
    field = new_field

def new_generation_bis():
    global field, SIZE
    new_field = list()
    for r in range(SIZE):
        row = list()
        for c in range(SIZE):
            n = neighbors(r, c)
            if (r == 0 and c == 0) or (r == SIZE - 1 and c == 0) or (r == 0 and c == SIZE - 1) or (r == SIZE - 1 and c == SIZE - 1):
                row.append(1)
            elif n < 2 or n > 3: # 0 regardless of previous value
                row.append(0)
            elif n == 3: # 1 regardless of previous value
                row.append(1)
            else: # n == 2 - previous value
                row.append(field[r][c])
        new_field.append(row)
    field = new_field


def how_many() -> int:
    global field
    return sum(sum(row) for row in field)

field_text = open('input_2015_18.txt', 'r', encoding='utf-8').readlines()
start_field = list()
SIZE = len(field_text)
for lin in field_text:
    r = list()
    for i in range(SIZE):
        if lin[i] == '#':
            r.append(1)
        else:
            r.append(0)
    start_field.append(r)
field = deepcopy(start_field)
for step in range(100):
    new_generation()
print('Part 1 answer:', how_many())
field = start_field
for step in range(100):
    new_generation_bis()
print('Part 2 answer:', how_many())
