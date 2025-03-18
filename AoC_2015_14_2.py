max_distance = 0
leader = ''

class Deer:
    def __init__(self, cname, nspeed, nrun, nrest):
        self.name = cname
        self.run = nrun
        self.rest = nrest
        self.speed = nspeed
        self.distance = 0
        self.state = 'RUN'
        self.timer = self.run
        self.points = 0

    def tick(self):
        global max_distance
        global leader
        self.timer -= 1
        if self.state == 'RUN':
            self.distance += self.speed
            if self.distance > max_distance:
                max_distance = self.distance
                leader = self.name
        if self.timer == 0:
            if self.state == 'RUN':
                self.state = 'REST'
                self.timer = self.rest
            else:
                self.state = 'RUN'
                self.timer = self.run

    def award(self):
        global max_distance
        if self.distance == max_distance:
            self.points += 1



deer_text = open('input_2015_14.txt', 'r', encoding='utf-8').readlines()
ticks = 2503
deers = dict()
for ln in deer_text:
    lin = ln.strip().replace(' km/s for','').replace(' can fly','').replace('seconds, but then must rest for ','').replace(' seconds.','').split(' ')
    deers[lin[0]] = Deer(lin[0], int(lin[1]), int(lin[2]), int(lin[3]))
for t in range(ticks):
    for d in deers.keys():
        deers[d].tick()
    for d in deers.keys():
        deers[d].award()
print('Current distance leader: ', leader, ':', max_distance)
pts = 0
for d in deers.keys():
    if deers[d].points > pts:
        leader = d
        pts = deers[d].points
print('Current points leader: ', leader, ':', pts)
