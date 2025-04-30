from time import time
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
steps = 0
t0 = time()

while medicine != "e":
    for reactant, products in replacements:
        if products in medicine:
            medicine = medicine.replace(products, reactant, 1)
            steps += 1
print('Part 2 answer:', steps)
print("Elapsed time: %s seconds" % round(time() - t0, 3))
