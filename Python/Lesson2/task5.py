# 5) Реализовать структуру «Рейтинг»,
# представляющую собой 
# не возрастающий набор натуральных чисел. 
# У пользователя необходимо 
# запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, 
# то новый элемент с тем же значением должен 
# разместиться после них.
#
# Подсказка. 
# 
# Например, набор натуральных чисел: 7, 5, 3, 3, 2. 
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 46, 79, 666, 3, 3, 2,]

user_el = map(int, input('Введите элемент: ').split( ))

my_list.extend(user_el)
my_list.sort(reverse = 1)

print(' '.join(map(str, my_list)))


# my_list.append(user_el)
# my_list = sorted(my_list)
# str_rev = my_list[::-1]