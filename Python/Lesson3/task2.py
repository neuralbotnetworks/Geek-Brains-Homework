# 2)
#  Реализовать функцию,
#  принимающую несколько параметров,
#  описывающих данные пользователя:
#   - имя,
#   - фамилия,
#   - год рождения,
#   - город проживания,
#   - email,
#   - телефон.

#  Функция должна
#  принимать параметры как
#  именованные аргументы.
# 
#  Реализовать вывод данных о пользователе одной строкой.


def user_info():

    #global user_name, user_sername, user_year_birth, user_city, user_email, user_tel

    user_name = input("Введите Ваше имя: ")
    user_sername = input("Введите Вашу фамилию: ")
    user_year_birth = input('Введите год Вашего рождения: ')
    user_city = input('Введите город Вашего проживания: ')
    user_email = input('Введите ваш электронный почтовый ящик: ')
    user_tel = input('Введите ваш номер телефона: ')
    
    user_input = (
' Здравствуйте ' + user_sername + ' ' + user_name + '!' + \
' Вы родились в ' + user_year_birth + ' году.' + \
' Проживаете в городе ' + user_city + '.' + \
' Ваш почтовый яшик: ' + user_email + '.' + \
' Номер телефона: ' + user_tel)

    return user_input

print(user_info())


 