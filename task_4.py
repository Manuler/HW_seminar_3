# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

def dec_to_bin(num):
    bin_num = ''
    while num > 0:
        bin_num = f'{num % 2}{bin_num}'
        num = num // 2
    return bin_num

def dec_to_bin_rec(num):
    return f'{dec_to_bin_rec(num//2)}{num % 2}' if num > 0 else ''

dec_num = int(input("Введите число: "))
print(dec_to_bin(dec_num))
print(dec_to_bin_rec(dec_num))
