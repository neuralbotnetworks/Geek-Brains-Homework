
# Реализовать класс Stationery (канцелярская принадлежность).
# 
# Определить в нем 
#  + атрибут title (название) и 
#  + метод draw (отрисовка).
# 
#  Метод выводит сообщение “Запуск отрисовки.”
#  Создать три дочерних класса 
#  + Pen (ручка),
#  + Pencil (карандаш),
#  + Handle (маркер).
# 
#  В каждом из классов реализовать переопределение метода draw.

# Для каждого из классов 
# метод должен выводить 
# уникальное сообщение.
# 
# Создать экземпляры классов и проверить, 
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Вы используете: {self.title}. Запуск отрисовки'


class Pen(Stationery):
    pass

class Pencil(Stationery):
    pass

class Handle(Stationery):
    pass

p = Pen(title = 'Ручку')
pc = Pencil(title = 'Карандаш')
h = Handle(title = 'Маркер')

print(h.draw())
print(p.draw())
print(pc.draw())
