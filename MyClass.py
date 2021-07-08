# =================================
#       Основы ООП
# =================================

# class - шаблон для создания объектов
# Классы содержат атрибуты - данные, и методы - функции для обработки данных
class Person:
    # функция-конструктор - запускается автоматически при создании объекта (экземпляра класса)
    def __init__(self, name, surname, category):
        self.category = category
        self.surname = surname
        self.name = name

    # метод
    def next_category(self):
        self.category = str(int(self.category.split()[0]) + 1) + ' ' + \
                        self.category.split()[1]

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


p1 = Person('Artur', 'Ganeev', '3 A')
# Выводим текущий класс первого ученика
print(p1.category)
# Вызываем метод, который переводит ученика в следующий класс
p1.next_category()
# Проверяем, изменился ли класс
print(p1.category)
print(p1.name)
print(p1.surname)
print(p1.get_full_name())
p1.name = 'Вася'
print(p1.name)



persons = [Person('Artur', 'Ganeev', '3 A'),
           Person('Ivan', 'Ivanov', '1 A')]
for person in persons:
    person.next_category()
for num, person in enumerate(persons, start=1):
    print(f"{num}) {person.get_full_name()} класс: {person.category}")
