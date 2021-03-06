# 2)
#  Представлен список чисел.
#  Необходимо вывести элементы исходного списка,
#  значения которых больше предыдущего элемента.
#  
# Подсказка: 
#   элементы, удовлетворяющие условию, оформить в виде списка.
#
#  Для формирования списка использовать генератор.
# 
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].



def max_dig(l):
    for i in range (1, len(l)):
        if l[i] >l[i - 1]:
            yield l[i]

lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_lst =[el for el in max_dig(lst)]
print('-' * 60)
print('Исходный список: \n', lst)
print('-' * 60)
print("Числа co значеними больше предыдущих: \n", new_lst)
print('-' * 60)