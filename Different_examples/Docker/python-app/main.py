import calendar

print('Добро подаловать в СУПЕР календарь\n')

year = int(input('Пожалуйста введите год: '))
month = int(input('Введите номер любого месяца: '))

print(calendar.month(year, month))

print('Всего хорошего!')