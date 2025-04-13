text = open('input_2015_19.txt', 'r', encoding='utf-8').readlines()
replacements = list()
res = set()
part_two = False
for lin in text:
    if part_two:
        medicine = lin.strip()
    elif len(lin) < 5:
        part_two = True
    else:
        l = lin.strip().split(' => ')
        replacements.append((l[0], l[1]))
for rep in replacements:
    s_idx = 0
    position = medicine.find(rep[0], s_idx)
    while position >= 0:
        res.add(medicine[:position] + rep[1] + medicine[position + len(rep[0]):])
        s_idx = position + 1
        position = medicine.find(rep[0], s_idx)
print('Part1 answer:', len(res))
