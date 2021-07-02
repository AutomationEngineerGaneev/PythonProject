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

s='1234567890'
print(type(s))
s= 'Hello' + 'World'

s=f'Value of {a=}'
print(s)


print(s[0])
print(s[1:5]) #slice
print(s[10:-1]) #size of str -1 symbol


list_of_something =[1,2,3,4,'abc',[1,True]]
print(list_of_something)
print(list_of_something[0])
print(list_of_something[5][0])
print(list_of_something[3:4])
print(list_of_something[3:-1])

dictionary = {
    'key': 'value',
    'Moscow':'Москва',
    'l': list_of_something
}

print(dictionary)
print(dictionary['Moscow'])
print(dictionary['l'])
print(dictionary['l'][5][0])

