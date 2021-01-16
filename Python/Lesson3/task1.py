# 1)
#  Реализовать функцию,
#  принимающую два числа (позиционные аргументы)
#  и выполняющую их деление.
#  Числа запрашивать у пользователя,
#  предусмотреть обработку ситуации деления на ноль.


def user_int_result():
    try:
        int1 = int(input('Введите первое число: '))
        int2 = int(input('Введите второе число: '))
        calc_result = int1 / int2
        return calc_result
    except ZeroDivisionError:    
        err_z_d_e = print('Я не буду выполнять такие вычисления')
        return err_z_d_e

print(user_int_result())