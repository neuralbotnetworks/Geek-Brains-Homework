# 5.
#  Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.

import os

DIR = 'Python/Lesson 5/files/'
file_r = os.path.join(DIR, 'task5.txt')
file_w = os.path.join(DIR, 'task5.txt')
nums = []

print('-' * 60)
while True:
    try:
        num = int(input('Введите числа, каждое с новой строки: '))
        nums.append(str(num))
    except ValueError:
        print('-' * 60)
        print('Числа записаны в файл task5.txt')
        break

with open(file_w, 'w', encoding='utf-8') as file_write:
    print(f'{" ".join(nums)}', file=file_write)

with open(file_r, 'r', encoding='utf-8') as file_read:
    nums_list = file_read.readline().split()
    nums_sum = 0
    for num in nums_list:
        nums_sum += int(num)
print('-' * 60)
print(f'Сумма чисел:{nums_sum}')
print('-' * 60)