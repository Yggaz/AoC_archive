letters = list()
for i in range(8):
    letters.append(dict())
data = open('input_2016_06.txt', 'r', encoding='utf-8').readlines()
for ln in data:
    for c in range(len(ln.strip())):
        letters[c][ln[c]] = letters[c].get(ln[c], 0) + 1
answer1 = ''
answer2 = ''
for i in range(8):
    # print(sorted(letters[i].items(), key=lambda item: item[1], reverse=True))
    answer1 += max(letters[i], key = letters[i].get)
    answer2 += min(letters[i], key=letters[i].get)
print('Answer for part 1:', answer1)
print('Answer for part 2:', answer2)
