deer_text = open('input_2015_14.txt', 'r', encoding='utf-8').readlines()
ticks = 2503
max_dist = 0
leader = ''
for ln in deer_text:
    lin = ln.strip().replace(' km/s for','').replace(' can fly','').replace('seconds, but then must rest for ','').replace(' seconds.','').split(' ')
    speed = int(lin[1])
    run = int(lin[2])
    rest = int(lin[3])
    dist = run * speed
    cycle = run + rest
    cycles = ticks // cycle
    time_left = ticks % cycle
    if time_left > run:
        time_left = run
    dist_left = time_left * speed
    total_dist = dist * cycles + dist_left
    if total_dist > max_dist:
        max_dist = total_dist
        leader = lin[0]
        print('Current leader: ', leader, ':', total_dist)
print('Winner: ', leader, ':', max_dist)

