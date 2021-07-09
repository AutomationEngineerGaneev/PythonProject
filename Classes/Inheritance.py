# Наследование подразумевает, что дочерний класс содержит все атрибуты родительского класса,
# при этом некоторые из них могут быть переопределены или добавлены в дочернем.

# Общую информацию выносим в Класс-предок (родитель)
class Person:
    def __init__(self,name,surname):
        self.surname = surname
        self.name = name


class  Employe(Person):
    def __init__(self, name, surname,salary):
        # Явно вызываем конструктор родительского класса
        Person.__init__(self, name, surname)
        self.salary = salary

        def get_full_name(self):
            return self.name + ' ' + self.surname

        def set_name(self, new_name):
            self.name = new_name


employe = Employe('Ivan','Ivanov',3000)
print(employe.surname)
