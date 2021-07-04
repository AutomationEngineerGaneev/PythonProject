# список из чисел
numbers = [10, 15, 21, 33, 42, 55]
# lambda используется к каждому элементу в нашем списке:
mapped_numbers = list(map(lambda x: x * 2 + 3, numbers))
# Мы использовали list(), чтобы объект map был выведен как список, а не <map object at 0x7fc250003a58>.
print(mapped_numbers)
# ответ [23, 33, 45, 69, 87, 113]

# Метод strip() возвращает копию строки,
# удаляя как начальные, так и конечные символы.
str1 = 'android is awesome'
print(str1.strip('an'))
print(str1.strip('ome'))

# список в нижнем регистре:
list_of_words = ['one', 'two', 'list', '', 'dict']
# Перевести все строки в верхний регистр:
upper_list_of_words = list(map(str.upper,list_of_words))
print(upper_list_of_words)

