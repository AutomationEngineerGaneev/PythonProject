if 8 / 3 == 2:
    print('Ok 1')
elif 8 / 3 == 2.66666666:
    print('Ok 2')
else:
    print('Not ok')

password = ''  # not known

if not password:
    true_password = '12345'
else:
    true_password = password

true_password = password if  password else '12345'
print(true_password)

