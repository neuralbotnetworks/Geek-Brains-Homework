# 3.
#  Создать текстовый файл (не программно), 
# построчно записать фамилии сотрудников и величину их окладов.
#  Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
#  Выполнить подсчет средней величины дохода сотрудников.

import os

DIR = 'Python/Lesson 5/files'
files_dir = os.path.join(DIR, 'task3.txt')
file = open(files_dir, 'r', encoding='utf-8')
lines = file.readlines()

sum = 0
print('-' * 60)

for row in lines:
    line = row.split()

    if (float(line[1]) < 20000):
        print(f'{line[0]} за 2019 год, в месяц зарабатывал {float(line[1]) // 12}$')

    sum += float(line[1])

print('-' * 60)
print(f'В среднем ребятки зарабатывали по {sum // 12}$ в месяц')

file.close()
print('-' * 60)
