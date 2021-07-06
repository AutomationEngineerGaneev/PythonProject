def create_apartment(title, number_of_rooms, area, region, street, house, apartment_number, price):
    # словарь или Json
    return {
        'title': title,
        'number_of_rooms': number_of_rooms,
        'area': area,
        'region': region,
        'street': street,
        'house': house,
        'apartment_number': apartment_number,
        'price': price
    }

def test_create_apartment():
    # словарь или Json
    data = {
        'title': '2-х комнатная квартира',
        'number_of_rooms': 2,
        'area': 47,
        'region': 'Вахитовский район',
        'street': 'Вишневского',
        'house': '51',
        'apartment_number': '44',
        'price': 4_300_000
    }
    # A -> Act
    result = create_apartment(
        data['title'],
        data['number_of_rooms'],
        data['area'],
        data['region'],
        data['street'],
        data['house'],
        data['apartment_number'],
        data['price']
    )
    # сравниваем содержимое
    # A -> Assert
    assert result == data
    print(result,data)
print()
def test_simple0():
    mylist = 1, 2, 3, 4, 5
    # тоже самое, кортеж mylist = (1, 2, 3, 4, 5)
    assert 3 in mylist

def test_simple():
    mylist = [1, 2, 3, 4, 5]
    assert 3 in mylist


def test_simple1():
    mylist = [1, 2, 3, 4, 5]
    assert 2 in mylist


def test_simple2():
    dict = {'key': 'value',
            'Moscow': 'Москва', }
    assert 'Moscow' in dict


def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]
    print()
    print('В обратную сторону  ',list(reversed([1, 2, 3, 4])))



def test_len():
    actual = ['bl', 'direction', 'day']
    expected = ['bl', 'direction', 'day']

    assert len(actual) == len(expected)
    print()
    print('Длина actual  ',len(actual),'Длина actual  ', len(expected))
