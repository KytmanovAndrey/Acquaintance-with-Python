# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#
# 10 -> 1 2 4 8

num_n = input("Введите число N: ")
while not num_n.isdigit():
    print("Некорректный ввод")
    num_n = input("Введите число N: ")
num_n = int(num_n)
power = 1
print(f'{num_n} ->', end=' ')
while num_n >= power:
    print(power, end=' ')
    power *= 2