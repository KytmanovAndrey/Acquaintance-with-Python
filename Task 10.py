# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2

from random import randint

num_n = input("Введите число монеток: ")
while not num_n.isdigit():
    print("Некорректный ввод, введите число")
    num_n = input("Введите число монеток: ")
num_n = int(num_n)
print(f'{num_n} -> ', end='')
count_tails = 0
count_heads = 0
for i in range(num_n,0,-1):
    value = randint(0, 1)
    print(f'{value} ', end='')
    if value == 0:
        count_tails += 1
    else:
        count_heads += 1
if count_tails > count_heads:
    print(f'\n{count_heads}')
else:
    print(f'\n{count_tails}')
