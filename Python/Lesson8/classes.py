'''
 1 Задание
 «Дата»
'''
class Date:
    def __init__(self, dmy):
        self.dmy = dmy

    @classmethod
    def get_extract(cls, instr): 
        day, month, year = instr.split()
        mdict = {'01':('января', 'Января'),
                 '02':('февраля', 'Февраля'),
                 '03':('марта', 'Марта'),
                 '04':('апреля', 'Апреля'),
                 '05':('мая', 'Мая'),
                 '06':('июня', 'Июня'),
                 '07':('июля', 'Июля'),
                 '08':('августа', 'Августа'),
                 '09':('сентября', 'Сентября'),
                 '10':('октября', 'Октября'),
                 '11':('ноября', 'Ноября'),
                 '12':('декабря', 'Декабря')
                }
        for k, v in mdict.items():
            if month in v:
                month = k
                break
        if Date.get_check('-'.join([day, month, year])):
            return cls('-'.join([day, month, year]))
        else:
            return cls(f'Не верная дата')
    
    @staticmethod
    def get_check(string):
        from datetime import date as dt
        try:
            day, month, year = string.split('-')
        except ValueError:
            return 'Ошибка значения'
        try:
            dt(int(year), int(month), int(day))
            return 'Дата верна'
        except ValueError:
            return 'Ошибка значения'
'''
2 задание
Клаcc-исключение, деления на ноль
'''
class DevideZero(Exception):
    def __init__(self,):
        self.msg = "На ноль делить нельзя!"

    @staticmethod
    def get_divide(dividend, divider):
        try:
            if divider == 0:
                raise DevideZero
            return dividend / divider
        except DevideZero as er:
            print(er.msg)
        else:
            return dividend / divider
"""
3 Задание
Класс-исключение, наличия чисел
"""
class NumberChecker(Exception):
    def __init__(self, txt):
        self.txt = txt

"""
4,5,6 Задание
«Склад Оргтехники»
"""

"""
7 Задание
Сложение и Умножение комплексных чисел
"""

class ComplexNumber:
    def __init__(self, r, im):
        self.number = complex(r, im)

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number