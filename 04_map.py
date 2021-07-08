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


# map(func_link, <итератор>) --> итератор,
# каждый элемент которого - результат применения функции funk_link к элементам исходного итератора
print(list(map(len, ['mother', 'father', 'daughter', 'son'])))
print(list(map(lambda x: x / 2, [2, 4, 5, 10])))
# lambda - лямбда-функция (безымянная функция).

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

map(lambda x: x['name'], dict_a)  # Вернет: ['python', 'java']

map(lambda x: x['points'] * 10, dict_a)  # Вернет: [100, 80]

map(lambda x: x['name'] == "python", dict_a)  # Вернет: [True, False]

