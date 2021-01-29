
"""
Реализовать 
проект расчета суммарного расхода ткани на производство одежды.
 Основная сущность (класс) этого проекта — одежда,
  которая может иметь определенное название. 
  К типам одежды в этом проекте относятся пальто и костюм.
  У этих типов одежды существуют параметры:
   размер (для пальто) и 
   рост (для костюма).
  Это могут быть обычные числа: V и H, соответственно. 
Для определения расхода ткани
 по каждому типу одежды 
 использовать формулы: 
 для пальто (V/6.5 + 0.5),
 для костюма (2*H + 0.3). 

Проверить работу этих методов на 
реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
 реализовать абстрактные классы для основных классов проекта, 
проверить на практике работу декоратора 
@property.
"""

class Сlothes:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    def get_coat_square(self):
        return self.V / 6.5 + 0.5
    
    def get_jacket_square(self):
        return self.H * 2 + 0.3

    @property
    def get_full_square(self):
        return str(f'Общая площадь ткани: \n {(self.get_coat_square()) + (self.get_jacket_square())}')


class Coat(Сlothes):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.square_c = round(self.get_coat_square())

    def __str__(self):
        return f'Площадь ткани необходимая для пошива пальто {self.square_c}'


class Jacket(Сlothes):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.square_j = round(self.get_jacket_square())

    def __str__(self):
        return f'Площадь ткани необходимая для пошива костюма {self.square_j}'

coat = Coat(5, 9)
jacket = Jacket(2, 3)
print(coat)
print(jacket)
print(coat.get_full_square)
print(jacket.get_full_square)
print(jacket.get_coat_square())
print(jacket.get_jacket_square())