# 1)
#  Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#  В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
#  Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

_, working_hours, rate_per_hour, bonus = argv


print("Количество отработаных часов: ", working_hours)
print("Плата за 1 час работы: ", rate_per_hour)
print("Премия: ", bonus)

working_hours = float(working_hours)
rate_per_hour = float(rate_per_hour)
bonus = float(bonus)

print((working_hours * rate_per_hour) + bonus)
