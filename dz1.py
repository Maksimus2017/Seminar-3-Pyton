# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

number_n = int(input('Введите длину списка: '))
list_numbers = []
for i in range(number_n):
    new_number = random.randrange(0, 10)
    list_numbers.append(new_number)
print(list_numbers)
sum_n = 0
count = 1
for i in range(1, len(list_numbers), 2):
    sum_n += list_numbers[i]
print(f'Сумма элементов на нечетных позтцтях {sum_n}')

