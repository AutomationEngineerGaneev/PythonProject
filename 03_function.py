# Функции -  фрагмент программного кода (подпрограмма), к которому можно обратиться из другого места программы

def check_symbols(restricticted_symbols, s): # Объявление функции (в скобочках - параметры функции)
    for symb in restricticted_symbols:
        if symb in s:
            return True
        return False
    # Если функция ничего не возвращает, она возвращает спец.тип None

username ='dfde434343$#'
email ='wewe@wew.ru'

if check_symbols(['#','$#','@'],username):
    print('username has restricticted symbols') #True, because username consist of $# symbols
if check_symbols(restricticted_symbols =['#', '$#', '%'],s= email):
    print('email has restricticted symbols')  #False, because email does not contain '#', '$#', '%' symbols

# if '#' in username:
#     print('username has restricticted symbols')
#
# if '$#' in username:
#     print('username has retricticted symbols')
# if '@' in username:
#     print('username has retricticted symbols')

z = 15
def local(x):
    # x, y - локальные переменные, доступны только во время выполнения функции
    # z - глобальная переменная, доступна во всем модуле (.py файле)
    y = 10
    print('x = {}, y = {}, z = {}'.format(x, y, z))
local(5)


# Когда интерпретатор встречает инструкцию def test - создается переменная test с указателем на объект-функцию,
# поэтому функции можно объявлять внутри других инструкций и даже в других функциях
access = True
if access:
    def render(name):
        return 'Welcome, %s' % name
else:
    def render(name):
        return '%s, sorry. Try to enter again.' % name

print(render('Иван'))

# Объявление функции внутри функции используется для создания декораторов и функций-фабрик,
