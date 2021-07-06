# filter(filter_func, <итератор>) --> итератор с отфильтровыванием элементов функцией filter_func
print(list(filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))
# Отбрасываем все элементы длиной НОЛЬ
print(list(filter(len, ['', 'not null', 'bla', '', '10'])))

a = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x : x % 2 == 0, a))) # Вернет: [2, 4, 6]


# Обработка объектов:
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

print(list(filter(lambda x : x['name'] == 'python', dict_a))) # Вернет: [{'name': 'python', 'points': 10}]


