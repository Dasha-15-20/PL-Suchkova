
str1 = input('Введите строку: ')
str2 = ''
a = 0

a = str1.count('а')
str2 = str1.replace('а', '')

print('Количество символов "a":', a)
print('Новая строка:', str2)
