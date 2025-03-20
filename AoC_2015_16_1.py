target = {'children: ':3,'cats: ':7, 'samoyeds: ':2, 'pomeranians: ':3, 'akitas: ':0, 'vizslas: ':0, 'goldfish: ':5, 'trees: ':3, 'cars: ':2, 'perfumes: ':1}
sue_text = open('input_2015_16.txt', 'r', encoding='utf-8').readlines()
print(target)
for sue in sue_text:
    good_one = True
    good_two = True
    for k in target.keys():
        present = k in sue
        if present:
            how_many = int(sue.split(k)[1].split(',')[0])
            good_one = good_one and target[k] == how_many
            # the cats and trees readings indicates that there are greater than that many
            if k in ('cats: ', 'trees: '):
                good_two = good_two and target[k] < how_many
            # the pomeranians and goldfish readings indicate that there are fewer than that many
            elif k in ('pomeranians: ', 'goldfish: '):
                good_two = good_two and target[k] > how_many
            else:
                good_two = good_two and target[k] == how_many
    if good_one:
        print('Part 1:')
        print(sue)
    if good_two:
        print('Part 2:')
        print(sue)
