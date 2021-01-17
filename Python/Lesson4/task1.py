# 1)
#  Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#  В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
#  Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

task1, working_hours, rate_per_hour, bonus = argv

print("Имя скрипта: ", task1)
print("Количество отработаных часов: ", working_hours)
print("Плата за 1 час работы: ", rate_per_hour)
print("Премия: ", bonus)

working_hours = int(working_hours)
rate_per_hour = int(rate_per_hour)
bonus = int(bonus)

print((working_hours * rate_per_hour) + bonus)
