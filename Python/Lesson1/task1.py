# Поработайте с переменными, 
# создайте несколько, 
# выведите на экран, 
# запросите у пользователя несколько чисел и строк и 
# сохраните в переменные, 
# выведите на экран.

object1 = ('text_nadpisi')
object2 = ('Кириллица_текст')
object3 = 333666999

print(object1)
print(object2)
print(object3)

user_num = int(input('Число введи '))
user_num2 = int(input('Введи число '))
user_str = input('И текст ')
user_str2 = input('Ещё, но другой ')

print('Сумма чисел', user_num + user_num2)
print(f'Ты ввёл число {user_num} и {user_num2}, и две строки: сначала {user_str} потом {user_str2}')