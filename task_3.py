# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
#     - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

# lst = [1.1, 1.2, 3.1, 5.1, 10.01]
# for i in range (len(lst)):
#     lst[i] -= int(lst[i])
#
# print(round(max(lst) - min(lst), 2))

import random
l =[round(random.uniform(0,10),2) for i in range(5)]
print(l)
lst_final = [int(str(i).split(".")[1]) if len(str(i).split(".")[1]) > 1 else int(str(i).split(".")[1])*10 for i in l]
print(f'Список из рандомных чисел{l}')
print(f'Список из дробных частей {lst_final}')
print(f'Разница между максимальным и минимальным значением: 0,{max(lst_final)-min(lst_final)}')