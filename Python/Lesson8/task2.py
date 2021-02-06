"""
 2.
  Создайте собственный класс-исключение, 
 обрабатывающий ситуацию деления на нуль. 
 
  Проверьте его работу на данных, 
 вводимых пользователем.
 
  При вводе пользователем нуля в 
 качестве делителя программа 
 должна корректно обработать 
 эту ситуацию и не завершиться с ошибкой.
"""
from classes import DevideZero

while True:
    try:
        a = float(input('Делимое: '))
        b = float(input('Делитель: '))
        print(f'{DevideZero.get_divide(a, b)}')
    except ValueError:
        print('Это не число!')
        continue
    proceed = input('Если хотите продолжить введите: "Y"\n')
    if proceed.lower() != 'y':
        break
