
"""
3) 
Реализовать программу работы с органическими клетками, состоящими из ячеек.

  Необходимо создать класс Клетка.
  В его конструкторе инициализировать параметр, 
   соответствующий количеству ячеек клетки (целое число).
  
  В классе должны быть реализованы 
  методы перегрузки арифметических операторов: 
   сложение (__add__()),
   вычитание (__sub__()),
   умножение (__mul__()),
   деление (__truediv__()).

  Данные методы должны применяться только к клеткам и выполнять 
   увеличение, 
   уменьшение, 
   умножение и 
   целочисленное (с округлением до целого) деление клеток, соответственно.

  Сложение.
   Объединение двух клеток. 
   При этом число ячеек общей клетки
   должно равняться сумме ячеек исходных двух клеток.

  Вычитание.
   Участвуют две клетки. 
   Операцию необходимо выполнять только 
   если разность количества ячеек двух клеток больше нуля, 
   иначе выводить соответствующее сообщение.

  Умножение.
   Создается общая клетка из двух. 
   Число ячеек общей клетки определяется как 
   произведение количества ячеек этих двух клеток.

  Деление.
   Создается общая клетка из двух. 
   Число ячеек общей клетки определяется как 
   целочисленное деление количества ячеек этих двух клеток.

 В классе необходимо реализовать
  метод make_order(),
   принимающий экземпляр класса 
   и количество ячеек в ряду.
   Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида 
*****\n*****\n*****...,
 где количество ячеек между \n 
 равно переданному аргументу.
  
Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся.

Например, 
 количество ячеек клетки равняется 12, 
 количество ячеек в ряду — 5.
  Тогда метод make_order() 
  вернет строку: 
*****\n*****\n**.

Или, 
 количество ячеек клетки равняется 15,
 количество ячеек в ряду — 5. 
  Тогда метод make_order() 
  вернет строку:
*****\n*****\n*****.

Подсказка: 
 подробный список операторов для перегрузки доступен по ссылке.
"""

class OrganicCell:
    def __init__(self, amount):
        self.amount = int(amount)

    def __str__(self):
        return f'Результат операции с клетками: {self.amount * "*"}'

    def __add__(self, other):
        return OrganicCell(self.amount + other.amount)

    def __sub__(self, other):
        return OrganicCell(self.amount - other.amount 
        if (self.amount - other.amount > 0) 
        else print('Отрицательное количество ячеек'))

    def __mul__(self, other):
        return OrganicCell(int(self.amount * other.amount))

    def __truediv__(self, other):
        return OrganicCell(round(self.amount // other.amount))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.amount / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.amount % cells_in_row)}'
        return row  

org_cells_1 = OrganicCell(120)
org_cells_2 = OrganicCell(30)

print(org_cells_1 + org_cells_2)
print(org_cells_1 - org_cells_2)
print(org_cells_1 / org_cells_2)
print(org_cells_1.make_order(20))
print(org_cells_2.make_order(6))


