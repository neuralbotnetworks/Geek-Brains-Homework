# 1)
#  Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#  В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
#  Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

_, working_hours, rate_per_hour, bonus = argv

print('-' * 60)
print("Количество часов:                       ", working_hours, 'ч.')
print("Плата за 1 час работы:                  ", rate_per_hour, '$')
print("Премия:                                 ", bonus, '$')
print('-' * 60)

working_hours = float(working_hours)
rate_per_hour = float(rate_per_hour)
bonus = float(bonus)

print('Заработная плата сотрудника составляет: ', (working_hours * rate_per_hour) + bonus, '$')
print('-' * 60)
