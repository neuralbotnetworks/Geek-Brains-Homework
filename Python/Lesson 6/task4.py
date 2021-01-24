# Реализуйте базовый класс Car.

#  У данного класса должны быть следующие 

# атрибуты:
#  speed,
#  color,
#  name,
#  is_police (булево). 
# 
#  А также 
# 
# методы: 
#  go, 
#  stop, 
#  turn(direction)

# которые должны сообщать, что машина 
#  поехала, 
#  остановилась, 
#  повернула (куда).

# Опишите несколько 
# 
# дочерних классов: 
#  TownCar, 
#  SportCar,
#  WorkCar,
#  PoliceCar.

# Добавьте 
# в базовый класс 
# метод 
#  show_speed,
# 
#  который должен показывать текущую скорость автомобиля.

# Для классов 
# TownCar и 
# WorkCar 

# переопределите метод 
# show_speed.

# При значении скорости свыше 

# 60 (TownCar) и 
# 40 (WorkCar) 
# 
# должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. 
# Выполните вызов методов и также покажите результат.



class Car:

    speed: float
    color: str
    name: str
    is_police: bool

    def go(self):
        return print('Движение')

    def stop(self):
        return print('Остановка')

    def turn(self, direction):
        return print(f'Поворот в {direction}')

    def show_speed(self):
        return self.speed


class PoliceCar(Car):
    is_police = True
    name = 'GM'
    color = 'Black'
    speed = 150

class TownCar(Car):
    is_police = False
    name = "VW"
    color = "White"
    speed = 90

    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости!! ' + str(self.speed)
        return str(self.speed)

class WorkCar(Car):
    is_police = False
    name = 'ГАз NEXT'
    color = 'Green'
    speed = 60

    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости!! ' + str(self.speed)
        return str(self.speed)

class SportCar(Car):
    is_police = False
    name = 'Porshe 911 Targa 4S'
    color = 'Gray'
    speed = 180.0



tc = TownCar()
pc = PoliceCar()
sc = SportCar()
wc = WorkCar()

print(tc.__dict__)
print(pc.__dict__)
print(wc.__dict__)
print(sc.__dict__)

pc.go()
print(wc.turn(direction = 'не туда'))

sc.speed = 150

print(tc.__dict__)
print(pc.__dict__)
print(wc.__dict__)
print(sc.__dict__)
