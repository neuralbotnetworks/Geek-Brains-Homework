# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите 
# в формате чч:мм:сс. 
# Используйте форматирование строк. 


user_sec = int(input('Введите количество времени в секундах: '))

minutes_in_seconds = user_sec // 60
hours = minutes_in_seconds // 60
minutes = minutes_in_seconds % 60
seconds = user_sec % 60
day = hours // 24
hours = hours % 24
year = day // 365
day = day % 365

 

print(f'{year} Год {day} Дней {hours:02}:{minutes:02}:{seconds:02}')