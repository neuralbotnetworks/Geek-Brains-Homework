# 6. Необходимо создать (не программно) 
# текстовый файл, 
# где каждая строка описывает учебный предмет и наличие лекционных, 
# практических и лабораторных занятий по этому предмету и их количество.
#  Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#  Сформировать словарь, содержащий 
# название предмета и общее количество занятий по нему.
#  Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import os
import re

sep_line = ('-'* 60 + '\n')
DIR = 'Python/Lesson 5/files/'
file_r = os.path.join(DIR, 'task6.txt')

def lessons(calc_line: str):
    line_lessons = re.sub(r'\D', ' ', calc_line)
    number_of_lessons = 0
    for hour in line_lessons.split():
        number_of_lessons += int(hour)
    return number_of_lessons

lesson_name = {}
with open(file_r, 'r', encoding='utf-8') as file_read:
    for line in file_read.readlines():
        listed_line = line.split(': ')
        lesson_name[listed_line[0]] = lessons(listed_line[1])

print(f'\
{sep_line}\
Уроков в первой четверти:\n\
{sep_line}\
{lesson_name}\n\
{sep_line}')
