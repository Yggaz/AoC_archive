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
for check in list(pmut(["Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory"])):
    if check.index('Alice') > check.index('Bob'):
        cur_happiness = 0
        prev = 'Me'
        for g in check:
            cur_happiness += costs.get((prev, g), 0)
            cur_happiness += costs.get((g, prev), 0)
            prev = g
        if happiness < cur_happiness:
            happiness = cur_happiness
print(happiness)
