# Answer for part 1: 3176
# Answer for part 2: 14710
class Rule:
    def __init__(self, gin, op, gout):
        self.in1 = gin
        self.operation = op
        self.out = gout

    def ready(self) -> bool:
        return self.in1 in memory.keys() or self.in1.isnumeric()

    def produce(self):
        if self.ready():
            if self.in1.isnumeric():
                operand1 = int(self.in1)
            else:
                operand1 = memory[self.in1]
            match self.operation:
                case 'NOT':
                    memory[self.out] = operand1 ^ 0b1111111111111111
                case 'INPUT':
                    memory[self.out] = operand1

class RuleBin(Rule):
    def __init__(self, gin1, gin2, op, gout):
        self.in2 = gin2
        Rule.__init__(self, gin1, op, gout)

    def ready(self) -> bool:
        return (self.in1 in memory.keys() or self.in1.isnumeric()) and (self.in2 in memory.keys() or self.in2.isnumeric())

    def produce(self):
        if self.ready():
            if self.in1.isnumeric():
                operand1 = int(self.in1)
            else:
                operand1 = memory[self.in1]
            if self.in2.isnumeric():
                operand2 = int(self.in2)
            else:
                operand2 = memory[self.in2]
            match self.operation:
                case 'AND':
                    memory[self.out] = operand1 & operand2
                case 'OR':
                    memory[self.out] = operand1 | operand2
                case 'LSHIFT':
                    memory[self.out] = operand1 << operand2
                case 'RSHIFT':
                    memory[self.out] = operand1 >> operand2


data = open('input_2015_07.txt', 'r', encoding='utf-8').read().splitlines()
memory = dict()
rules = []
for ln in data:
    r = ln.split(' -> ')
    ops = r[0].split(' ')
    if len(ops) == 1:
        rule = Rule(ops[0], 'INPUT', r[1])
    elif len(ops) == 2:
        rule = Rule(ops[1], ops[0], r[1])
    else:
        rule = RuleBin(ops[0], ops[2], ops[1], r[1])
    rules.append(rule)
# for r in rules:
#     if type(r) is RuleBin:
#         print(r.in1, r.operation, r.in2, ' -> ', r.out)
#     else:
#         print(r.operation, r.in1, ' -> ', r.out)
done = False
step = True
while step and not done:
    done = True
    step = False
    for r in rules:
        if r.out not in memory.keys():
            if not r.ready():
                done = False
            else:
                step = True
                r.produce()
answer1 = memory['a']
print('Answer for part 1:', answer1)
for r in rules:
    if r.out == 'b':
        r.in1 = str(answer1)
memory.clear()
done = False
step = True
while step and not done:
    done = True
    step = False
    for r in rules:
        if r.out not in memory.keys():
            if not r.ready():
                done = False
            else:
                step = True
                r.produce()
answer2 = memory['a']
print('Answer for part 2:', answer2)
