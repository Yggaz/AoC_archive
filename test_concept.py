import random

count = 0
for _ in range(100):
    # Шаг 1: Выбираем число A равновероятно из {1, 2, 3}
    A = random.randint(1, 3)

    # Шаг 2: Выбираем число B равновероятно из {1, 2, 3}
    B = random.randint(1, 3)

    # Шаг 3: Выбираем число C равновероятно из чисел, отличных от B
    options = [x for x in [1, 2, 3] if x != B]
    C = random.choice(options)

    # Подсчитываем совпадение C с A
    if C == A:
        count += 1

# Вывод результата
print("Число совпадений:", count)