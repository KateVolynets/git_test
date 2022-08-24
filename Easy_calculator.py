number_1, number_2 = float(input('Enter the first number: ')), float(input('Enter the second number: '))
counter_1 = int(input('If you want to add two numbers, please press 0 : '))
if counter_1 == 0:
    res = number_1 + number_2
    print(number_1, '+', number_2, '=', res)
print()
counter_2 = int(input('If you want to minus two numbers, please press 1 : '))
if counter_2 == 1:
    res = number_1 - number_2
    print(number_1, '-', number_2, '=', res)
print()
counter_3 = int(input('If you want to multiply two numbers, please press 2 : '))
if counter_3 == 2:
    res = number_1 * number_2
    print(number_1, '*', number_2, '=', res)
print()
counter_4 = int(input('If you want raise the first number to the power of the second number, please press 3 : '))
if counter_4 == 3:
    res = number_1 ** number_2
    print(number_1, '^', number_2, '=', res)
print()
counter_5 = int(input('If you want to divide the first number by the second, please press 4 : '))
if counter_5 == 4:
    if number_2 == 0:
        print("Can't divide by zero")
    else:
        res = number_1/number_2
        print(number_1, '/', number_2, '=', int(res))
print()
counter_6 = int(input('If you want to perform integer division the first number by the second, please press 5 : '))
if counter_6 == 5:
    if number_2 == 0:
        print("Can't divide by zero")
    else:
        res = number_1 // number_2
        print(number_1, '//', number_2, '=', int(res))
print()
counter_7 = int(input('If you want to modulo the first number by the second, please press 6 : '))
if counter_7 == 6:
    if number_2 == 0:
        print("Can't divide by zero")
    else:
        res = number_1 % number_2
        print(number_1, '%', number_2, '=', int(res))
if number_1 != number_2:
    print()
    counter_8 = int(input('If you want to divide the first number by the second, please press 7 : '))
    if counter_8 == 7:
        if number_1 == 0:
            print("Can't divide by zero")
        else:
            res = number_2/number_1
            print(number_2, '/', number_1, '=', int(res))
    print()
    counter_9 = int(input('If you want to perform integer division the first number by the second, please press 8 : '))
    if counter_9 == 8:
        if number_1 == 0:
            print("Can't divide by zero")
        else:
            res = number_2 // number_1
            print(number_2, '//', number_1, '=', int(res))
    print()
    counter_10 = int(input('If you want to modulo the first number by the second, please press 9 : '))
    if counter_10 == 9:
        if number_1 == 0:
            print("Can't divide by zero")
        else:
            res = number_2 % number_1
            print(number_2, '%', number_1, '=', int(res))
    if counter_8 != 7 and counter_9 != 8 and counter_10 != 9:
        print()
        print('Please, select an operation')
else:
    if counter_1 != 0 and counter_2 != 1 and counter_3 != 2 and counter_4 != 3 and counter_5 != 4 and counter_6 != 5 \
         and counter_7 != 6:
        print()
        print('Please, select an operation')
