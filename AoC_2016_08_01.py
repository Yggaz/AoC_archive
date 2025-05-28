# 50 pixels wide and 6 pixels tall
def rect (a, b):
    global screen
    for r in range(b):
        for c in range(a):
            screen[r][c] = 1
    #print('Rect: A =', a, ', B =', b)

def rotate_row(rw, offset):
    global screen
    for o in range(offset):
        src = screen[rw][49]
        for i in range(49):
            screen[rw][49 - i] = screen[rw][49 - i - 1]
        screen[rw][0] = src
        #Мы будем сдвигать элементы вправо на 1. Нам понадобится ровно 50 сдвигов. При этом последний - нетипичный.
        #1. Записать элемент 49.
        #2. 48-й сдвинуть в 49-й
        #3. 47-й сдвинуть в 48-й
        #...
        #49. 0-й сдвинуть в 1-й
        #50. записанный 49-й записать в 0-й

def rotate_column(cl, offset):
    global screen
    for o in range(offset):
        src = screen[5][cl]
        for i in range(5):
            screen[5 - i][cl] = screen[5 - i - 1][cl]
        screen[0][cl] = src


screen = [[0 for i in range(50)] for j in range(6)]
data = open('input_2016_08.txt', 'r', encoding='utf-8').readlines()
for cmd in data:
    cmd_list = cmd.strip().split(' ')
    if cmd_list[0] == 'rect':
        a, b = map(int, cmd_list[1].split('x'))
        rect(a, b)
    elif cmd_list[1] == 'row':
        off = int(cmd_list[4])
        rw = int(cmd_list[2].split('=')[1])
        rotate_row(rw, off)
    elif cmd_list[1] == 'column':
        off = int(cmd_list[4])
        cl = int(cmd_list[2].split('=')[1])
        rotate_column(cl, off)
ans1 = sum(sum(r) for r in screen)
print('Answer for part 1:', ans1)
print('Answer for part 2:')
for r in range(6):
    r_out = ''
    for c in range(50):
        if screen[r][c] == 1:
            r_out += '*'
        else:
            r_out += ' '
    print(r_out)
