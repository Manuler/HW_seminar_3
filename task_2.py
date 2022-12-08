# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

lst_len = int(input('Введите размер списка: '))
list = []
count = 0
while count <= lst_len - 1:
    tmp = int(input(f'Введите значение для элемента списка с индексом {count}: \n'))
    list.append(tmp)
    count +=1
print(f'\nЗаполненный список: {list}')

def nums_pair_product(nums):
    prod = []
    half_len = len(nums) // 2
    for i in range(0, half_len):
        prod.append(nums[i] * nums[-i -1])
    if len(nums) % 2 != 0:
        prod.append(nums[half_len] ** 2)
    return prod

print(nums_pair_product(list))