# Это и есть функцяи декоратор
def new_decorator(function_to_decorate):
    def wrapper():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()  # Сама функция
        print("А я - код, срабатывающий после")

    return wrapper


# Вот так просто мы можем декорировать любую функцию
@new_decorator
def simple_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")
#
#
# # Вызываем декорируемую функцию:
simple_function()

# new_decorator(simple_function)()

# Пример использования декоратора @property
class Alphabet:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print('Getting value')
        return self._value

    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value

    # passing the value


x = Alphabet('Peter')
print(x.value)

x.value = 'Diesel'

del x.value