ingr = list()
ingr_text = open('input_2015_15.txt', 'r', encoding='utf-8').readlines()
max_result = 0
max_result_500 = 0
best_variant = (0, 0, 0, 0)
best_variant_500 = (0, 0, 0, 0)
for l in ingr_text:
    l1 = l.split(':')
    l2 = l1[1].replace(',', '').split()
    ingr.append((l1[0], int(l2[1]), int(l2[3]), int(l2[5]), int(l2[7]), int(l2[9])))

for a in range(1, 98):  # Первое число может быть от 1 до 97
    for b in range(1, 99 - a):  # Второе число может быть от 1 до (98 - a)
        for c in range(1, 100 - a - b):  # Третье число может быть от 1 до (99 - a - b)
            d = 100 - a - b - c  # Четвертое число - остаток до 100
            if d > 0:
                capacity = a * ingr[0][1] + b * ingr[1][1] + c * ingr[2][1] + d * ingr[3][1]
                durability = a * ingr[0][2] + b * ingr[1][2] + c * ingr[2][2] + d * ingr[3][2]
                flavor = a * ingr[0][3] + b * ingr[1][3] + c * ingr[2][3] + d * ingr[3][3]
                texture = a * ingr[0][4] + b * ingr[1][4] + c * ingr[2][4] + d * ingr[3][4]
                calories = a * ingr[0][5] + b * ingr[1][5] + c * ingr[2][5] + d * ingr[3][5]
                result = max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)
                if result > max_result:
                    max_result = result
                    best_variant = (a, b, c, d)
                if calories == 500 and result > max_result_500:
                    max_result_500 = result
                    best_variant_500 = (a, b, c, d)


print(best_variant)
print(max_result)
print(best_variant_500)
print(max_result_500)
