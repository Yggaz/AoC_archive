from itertools import permutations as pmut

# There are 8 people: Alice, Bob, Carol, David, Eric, Frank, George, Mallory
# Alice would sit on place 1: we won't move her. Bob must precede Carol. So we need to test 7!/2 = 2520 combinations
# I need a structure
cost_text = open('input_2015_13.txt', 'r', encoding='utf-8').readlines()
costs = dict()
happiness = 0
for ln in cost_text:
    lin = ln.strip().replace('.','').replace('would gain ','').replace('would lose ','-').replace(' happiness units by sitting next to','').split(' ')
    costs[(lin[0], lin[2])] = int(lin[1])
#for k in costs.keys():
#    print(k, costs[k])
for check in list(pmut(["Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory"])):
    if check.index('Bob') < check.index('Carol'):
        cur_happiness = 0
        #sit = list()
        prev = 'Alice'
        for g in check:
            #sit.append((prev, g))
            cur_happiness += costs[(prev, g)]
            cur_happiness += costs[(g, prev)]
            prev = g
        #sit.append((prev, 'Alice'))
        cur_happiness += costs[(prev, 'Alice')]
        cur_happiness += costs[('Alice', prev)]
        if happiness < cur_happiness:
            happiness = cur_happiness
            #print(cur_happiness)
            #print(sit)
print(happiness)
