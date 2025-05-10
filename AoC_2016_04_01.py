letters = 'abcdefghijklmnopqrstuvwxyz'
rooms = open('input_2016_04.txt', 'r', encoding='utf-8').readlines()
part1_sum = 0
for room in rooms:
    chunks = room.strip().split('-')
    last = len(chunks) - 1
    room_id = int(chunks[last].split('[')[0])
    checksum = chunks[last][-6:-1]
    freq = dict()
    for c in range(last):
        for cnk in chunks[c]:
            freq[cnk] = freq.get(cnk, 0) + 1
    check_charge = sorted(freq.items(), key=lambda item: (1000-item[1], item[0]))
    v_check = ''
    for j in range(5):
        v_check += check_charge[j][0]
    if v_check == checksum:
        real_name = ''
        north = False
        part1_sum += room_id
        shift = room_id % 26
        for c in range(last):
            wrd = ''
            for cnk in chunks[c]:
                i = letters.find(cnk)
                wrd += letters[(i + shift) % 26]
            real_name += wrd
            if wrd == 'object':
                north = True
            real_name += ' '
        if north:
            print(real_name, room_id)
print('Answer for part 1:', part1_sum)
