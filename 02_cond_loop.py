if 8 / 3 == 2:
    print('Ok 1')
elif 8 / 3 == 2.66666666:
    print('Ok 2')
else:
    print('Not ok')

# password = ''  # not known
password = '5432'  # not known

if not password:
    true_password = '12345'
else:
    true_password = password

true_password = password if password else '12345'
print(true_password)

# for i in 1: так делать нельзя , нужно ходить по спискам или словарям,строкам
# for i in [1, 2, 3, 4, 5, 6]:
# for i in range(10):
for i in range(1, 11):
    print(i * i)
# Четные числа попадают
for i in range(1, 11):
    if i % 2 == 0:
        print(i * i)

    # List Comprehension
lc = [i * i for i in range(1, 11) if i % 2 == 0]
print(lc)
