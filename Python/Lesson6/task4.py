# Реализуйте базовый класс Car.
#  У данного класса должны быть следующие атрибуты:
#  + speed,
#  + color,
#  + name,
#  + is_police (булево). 
# 
#  А также методы: 
#  + go, 
#  + stop, 
#  + turn(direction)

#  Kоторые должны сообщать, что машина 
#  + поехала, 
#  + остановилась, 
#  + повернула (куда).

# Опишите несколько дочерних классов: 
#  + TownCar, 
#  + SportCar,
#  + WorkCar,
#  + PoliceCar.

# Добавьте в базовый класс метод 
#  + show_speed,
# который должен показывать текущую скорость автомобиля.

# Для классов 
# TownCar и WorkCar 
# переопределите метод 
# show_speed.

# При значении скорости свыше 
# 60 (TownCar) и 40 (WorkCar) 
# должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, 
# передайте значения атрибутов.
# Выполните доступ к атрибутам, 
# выведите результат. 
# Выполните вызов методов и также 
# покажите результат.

class Car:
    def __init__(self, name, color, speed, is_police):
#        print('New construction action')
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def car_go(self):
        return f'{self.color} автомобиль {self.name} движется.'

    def car_stop(self):
        return f'{self.color} автомобиль {self.name} остановился.'

    def car_turn(self, direction):
        return f'{self.color} автомобиль {self.name} повернул {direction}'

    def car_show_speed(self):
        return f'{self.color} автомобиль {self.name} движется со скоростью {self.speed} км/ч.'

class WorkCar(Car):
    def car_show_speed(self):
        if self.speed > 40:
            return f'{self.color} автомобиль {self.name} превысил скорость на {self.speed - 40} км/ч.'
        return f'{self.color} автомобиль {self.name} движется со скоростью {self.speed} км/ч.'
 
class TownCar(Car):
    def car_show_speed(self):
        if self.speed > 60:
            return f'{self.color} автомобиль {self.name} превысил скорость на {self.speed - 60} км/ч.'
        return f'{self.color} автомобиль {self.name} движется со скоростью {self.speed} км/ч.'


sportcar = Car('Porshe 911 Targa 4S', 'Серый', 220, False)
policecar = Car('General Motors', 'Чёрный', 150, True)
towncar = TownCar('Volkswagen Tiguan', 'Белый', 55, False)
workcar = WorkCar('Газ Next', 'Зелёный', 70, False)

print(towncar.__dict__)
print(policecar.__dict__)
print(workcar.__dict__)
print(sportcar.__dict__)

towncar.speed = 90
sportcar.speed = 150
print(policecar.car_go())
print(policecar.car_turn(direction = 'не туда!'))
print(workcar.car_turn(direction = 'вправо.'))
workcar.speed = 20
print(workcar.car_show_speed())
print(towncar.car_show_speed())
print(sportcar.car_show_speed())
