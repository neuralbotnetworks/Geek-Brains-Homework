# 2.
#  Создать текстовый файл (не программно),
#  сохранить в нем несколько строк,
#  выполнить подсчет количества строк,
#  количества слов в каждой строке.


import os

DIR = 'Python/Lesson 5/files'
files_dir = os.path.join(DIR, 'task2.txt')
file = open(files_dir, 'r', encoding='utf-8')
lines = file.readlines()

print('-' * 60)
print(f'В файле {len(lines)} строк(и)')
print('-' * 60)

i = 1
for string in lines:
    print(f'В {i} строке, количество слов: {len(string.split())} ')
    i+=1

file.close()
print('-' * 60)