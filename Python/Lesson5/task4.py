# 4.
#  Создать (не программно) текстовый файл 
# со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4

#  Необходимо написать программу, 
# открывающую файл на чтение и 
# считывающую построчно данные.
#  При этом английские числительные 
# должны заменяться на русские.
#  Новый блок строк должен 
# записываться в новый текстовый файл.

import os

DIR = 'Python/Lesson 5/files'
file_r = os.path.join(DIR, 'task4.txt')
file_w = os.path.join(DIR, 'new_task4.txt')
translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'
}

with open(file_r, 'r', encoding='utf-8') as file_read:
    lines = file_read.readlines()

with open(file_w, 'a', encoding='utf-8') as files_write:
    for line in lines:
        row = line.split()
        row[0] = translate[row[0]]
        print(' '.join(row), file=files_write)