# 1.
#  Создать программно файл в текстовом формате, 
# записать в него построчно данные, 
# вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.

import os

DIR = 'Python/Lesson 5/files'
file_path = os.path.join(DIR, 'task1.txt')
file = open(file_path, 'a',  encoding='utf-8')

print('-' * 60)
while True:
    user_input = input('Жмите кнопки: ')

    if not user_input:
        file.close()
        print('The End!')
        break

    file.write(f'{user_input}\n')
print('-' * 60)
