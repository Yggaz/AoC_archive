from itertools import permutations as p
data = open('input_2015_09.txt', 'r', encoding='utf-8').read().splitlines()
distance = {}
places = set()
for d in data:
    lin = d.split(' = ')
    place = lin[0].split(' to ')
    places.add(place[0])
    places.add(place[1])
    distance[(place[0], place[1])] = int(lin[1])
    distance[(place[1], place[0])] = int(lin[1])
min_distance = None
max_distance = None
min_path = None
max_path = None
for path in p(places):
    cur_distance = 0
    for i in range(len(path) - 1):
        cur_distance += distance[(path[i], path[i + 1])]
    if min_distance is None or cur_distance < min_distance:
        min_distance = cur_distance
        min_path = path
    if max_distance is None or cur_distance > max_distance:
        max_distance = cur_distance
        max_path = path
print(min_distance)
print(*min_path)
print(max_distance)
print(*max_path)
