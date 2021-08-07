# ====================
#   Функции часть-2
# ====================

# Уточню! Чтобы не было путаницы...
# переменные, в которые функция получает значения - ПАРАМЕТРЫ,
# значения, которые передаются в функцию - АРГУМЕНТЫ:

# def func(param1, param2, ...):
#     pass          <-- тело функции
#     return value  <-- возвращаемое значение
#
# func(arg1, arg1, ...)


def test1(*args):  # *args - принимает любое кол-во аргументов в виде кортежа
    print(args)

# Функцию можно вызвать с любым кол-вом аргументов
test1()
test1(1, 2, 3)
test1(1, 2, 3, 5, 8)


def test2(a=10, b=5):  # именованные параметры со значениями по умолчанию
    print('a =', a, 'b = ', b)

# Если значение не передано, используется значение по умолчанию
test2(1, 2)
test2(1)
test2()


# def test3(**kwargs, *args): <-- ошибка, позиционные всегда идут до именованных
def test3(*args, **kwargs):  # kwargs - принимает все именованные аргументы в виде словаря
    print('in func test3')
    print('args = ', args)
    print('kwargs = ', kwargs)


test3(1, 2, 3, 4, a=5, b=6, c=12)


def test4(a, b, c, *, d, e, f):  # a,b,c - позиционные, d,e,f - именованные (без значений по умолчанию)
    print(a, b, c, d, e, f)


test4(1, 2, 3, d=4, e=5, f=6)
# test4(1, 2, 3, 4, 5, 6)  # <-- ошибка

if __name__ == "__main__":
    # все, что написано тут, не будет выполнено при импорте данного модуля в другой
    pass