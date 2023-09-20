# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
import math
# 4 4 -> 2 2
# 5 6 -> 2 3

from math import sqrt

num_s = input("Введите сумму чисел: ")
while not num_s.isdigit() or int(num_s) < 2:
    print("Некорректный ввод")
    num_s = input('Введите сумму чисел: ')
num_s = int(num_s)
num_p = input("Введите произведение чисел: ")
while not num_p.isdigit() or int(num_p) < 1:
    print("Некорректный ввод")
    num_p = input('Введите произведение чисел: ')
num_p = int(num_p)
if num_s ** 2 - 4 * num_p >= 0:
    num_x = (num_s + math.sqrt(num_s * num_s - 4 * num_p)) / 2
    num_y = num_s - num_x
    if num_x - int(num_x) == 0:
        print(f'сумма {num_s}, произведение {num_p} -> эти числа {int(num_y)} и {int(num_x)}')
    else:
        print('решений нет в натуральных числах')
else:
    print('решений нет')
