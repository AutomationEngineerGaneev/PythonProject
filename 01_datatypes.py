# Полиморфизм - разное поведение одного и того же метода в разных классах.
# Например, мы можем сложить два числа, и можем сложить две строки.
# При этом получим разный результат, так как числа и строки являются разными классами.

print(2 + 4)
print('2' + '4')
print((2, 4)+(2, 4))

a = 1 / 3
a = a + 2

print(a)
print(type(a))
print(a + a + a)

b_true = True
b_false = False

if b_true:
    print('Okey')
else:
    print('Not Okey')

n = None

s = '1 234567890'
s_new = str(int(s.split()[0]) + 1) + ' ' + \
     s.split()[1]
# Преобразовали число в строке и  прибавили +1
# s_new = 2 234567890
print(s_new)
print(type(s))
s = 'Hello' + 'World'

s = f'Value of {a=}'
# тоже самое
print('Welcome, {}, to our conference'.format(a))
print(s)

print(s[0])
print(s[1:5])  # slice
print(s[10:-1])  # slice until the penultimate symbol(size of str -1 symbol)

list_of_something = [1, 2, 3, 4, 'abc', [1, True]]
print(list_of_something)
print(list_of_something[0])
print(list_of_something[5][0])
print(list_of_something[3:4])
print(list_of_something[3:-1])
# словари или Json
dictionary = {
    'key': 'value',
    'Moscow': 'Москва',
    'l': list_of_something
}

print(dictionary)
print(dictionary['Moscow'])
print(dictionary['l'])
print(dictionary['l'][5][0])
#         Set (множество)
b = set(['a', 'b', 'c', 'c', 'a', 'e'])
print('b = ', b)
# Множество — «контейнер», содержащий не повторяющиеся элементы в случайном порядке.
