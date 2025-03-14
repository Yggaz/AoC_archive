elem_names = dict()
elem_digits = dict()
elem_decay = dict()
for lin in open('look_and_say.txt', 'r', encoding='utf-8').read().splitlines():
    el = lin.split(',')
    elem_names[el[1]] = el[0]
    elem_digits[el[0]] = el[1]
    elem_decay[el[0]] = list(el[2].split('.'))
start_elem = elem_names['1113222113']
cur_list = [start_elem]
answer1 = 0
for i in range(50):
    next_list = []
    for e in cur_list:
        for d in elem_decay[e]:
            next_list.append(d)
    cur_list = next_list
    if i == 39:
        answer1 = sum(len(elem_digits[e]) for e in cur_list)
answer2 = sum(len(elem_digits[e]) for e in cur_list)
print('Answer for part 1:', answer1)
print('Answer for part 2:', answer2)
