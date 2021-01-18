# 5)
#  Программа запрашивает у пользователя
# строку чисел,
# разделенных пробелом.
# 
#  При нажатии Enter должна выводиться сумма чисел.
# 
#  Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# 
#  Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме.
# 
#  Но если вместо числа вводится специальный символ,
# выполнение программы завершается.
# 
#  Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и
# после этого завершить программу.

def calc(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += int(num)
        except ValueError:
            flag = True
    return sum, flag

calc_result = 0

while True:
    user_nums = input('Введите числа через пробел: ').split(' ')
    sum, stop_flag = calc(*user_nums)
    calc_result += sum
    print(f'Cумма чисел: {calc_result}')

    if stop_flag:
        break