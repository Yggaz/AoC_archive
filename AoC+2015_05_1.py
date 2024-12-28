import re
nice1 = 0
nice2 = 0
for ln in open('input_2015_05.txt', 'r', encoding='utf-8').read().splitlines():
    vowels = len(re.findall(r'[aeiou]', ln)) > 2
    dbl = len(re.findall(r'(.)\1+', ln)) > 0
    blocked = ln.find('ab') >= 0 or ln.find('cd') >= 0 or ln.find('pq') >= 0 or ln.find('xy') >= 0
    if vowels and dbl and not blocked:
        nice1 += 1
    match = re.search(r'(?P<sgl>.).(?P=sgl)', ln)
    if match:
        match = re.search(r'(?P<dbl>..).*(?P=dbl)', ln)
        if match:
            nice2 += 1
print('Part 1 answer:', nice1)
print('Part 2 answer:', nice2)
