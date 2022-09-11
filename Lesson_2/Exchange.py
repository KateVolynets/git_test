counter_1 = int(input('If you want to convert the  UAH to the  USD, please press 0 : '))
if counter_1 == 0:
    uah = float(input('Enter the amount of UAH that you want to change: '))
    if uah < 0:
        print('Please enter the amount greater than zero')
    else:
        usd = uah * 0.027
        print(usd, '$', sep='')
print()
counter_2 = int(input('If you want to convert the USD to the UAH, please press 1 : '))
if counter_2 == 1:
    usd = float(input('Enter the amount of USD that you want to change: '))
    if usd < 0:
        print('Please enter the amount greater than zero')
    else:
        uah = usd * 36.85
        print(uah, '₴', sep='')
print()
counter_3 = int(input('If you want to convert the UAH to the EUR, please press 2 : '))
if counter_3 == 2:
    uah = float(input('Enter the amount of UAH that you want to change: '))
    if uah < 0:
        print('Please enter the amount greater than zero')
    else:
        eur = uah * 0.027
        print(eur, '€', sep='')
print()
counter_4 = int(input('If you want to convert the  EUR to the UAH, please press 3 : '))
if counter_4 == 3:
    eur = float(input('Enter the amount of EUR that you want to change: '))
    if eur >= 0:
        uah = eur * 37.18
        print(uah, '₴', sep='')
    else:
        print('Please enter the amount greater than zero')
elif counter_1 != 0 and counter_2 != 1 and counter_3 != 2 and counter_4 != 3:
    print()
    print('Please, select an operation')
