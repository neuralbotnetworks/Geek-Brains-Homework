# Создать список и 
# заполнить его элементами различных типов данных. 

# Реализовать скрипт проверки типа данных каждого элемента. 

# Использовать функцию type() для проверки типа. 

# Элементы списка можно не запрашивать у пользователя,а указать явно, в программе.

l_bool = True
l_dict = {'name':"Chesare", 'age': 33}
l_float = 3.14
l_int = 2
l_list = [13, 60.60 ,'another_text']
l_str = 'text_string'
l_tuple = 31, 6.06, 'text_text'


all_list = [l_bool, l_dict, l_float, l_int, l_list, l_str, l_tuple]

for variable in all_list:
    print(type(variable))
