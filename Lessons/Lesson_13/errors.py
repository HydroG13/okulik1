def calc(x, y):
    try:
        return int(x) / int(y)

    except (ZeroDivisionError, ValueError) as err:
        print( x, y)
        raise  err
        # return f'Ошибка: {err}'
        # return 'Ошибка ввода данных'
    # except ZeroDivisionError:
    #     return 'На ноль делить нельзя'
    # except ValueError:
    #     return 'неверный формат ввода'

# print(calc(int(input('number')), int(input('number'))))
# print('Hello')
print(calc(input('number'), (input('number'))))
print('Hello')