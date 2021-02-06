"""
 1.) 
 Реализовать класс «Дата», 
  функция-конструктор которого 
  должна принимать дату 
  в виде строки формата 
  «day-month-year".
  
В рамках класса реализовать два метода.

 Первый, с декоратором 
 @classmethod, 
  должен извлекать 
  число, месяц, год и 
  преобразовывать их тип к типу «Число». 

 Второй, с декоратором 
 @staticmethod,
  должен проводить validation
  date, month and year
  (например, месяц — от 1 до 12).
 
Проверить работу 
 полученной структуры 
 на реальных данных.
"""

from classes import Date

d = Date(())
d1 = Date('20-01-2021')
d2 = Date('22-11-2021')
d3 = Date.get_extract('02 февраля 2021')
d4 = Date.get_extract('31 апреля 2021')

print(d1.dmy)
print(d2.dmy)
print(d3.dmy)
print(d4.dmy)
print(d.get_check('30-02-2021'))
print(d.get_check('11-02-2021'))
print(Date.get_check(d.get_check(d3.dmy)))
print(Date.get_check(d.get_check(d4.dmy)))