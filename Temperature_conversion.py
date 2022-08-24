counter_1 = int(input('If you want to convert Celsius to Fahrenheit, please press 0 : '))
if counter_1 == 0:
    celsius = float(input('Enter the number of Celsius to be converted to Fahrenheit: '))
    fahrenheit = ((celsius * 9)/5) + 32
    print(fahrenheit,'°F', sep='')
counter_2 = int(input('If you want to convert Fahrenheit to Celsius, please press 1 : '))
if counter_2 == 1:
    fahrenheit = float(input('Enter the number of Fahrenheit to be converted to Celsius: '))
    celsius = (fahrenheit - 32)/1.8
    print(celsius,'°C', sep='')
counter_3 = int(input('If you want to convert Celsius to Kelvin, please press 2 : '))
if counter_3 == 2:
    celsius = float(input('Enter the number of Celsius to be converted to Kelvin: '))
    kelvin = celsius + 273.15
    print(kelvin, 'K', sep='')
counter_4 = int(input('If you want to convert Kelvin to Celsius, please press 3 : '))
if counter_4 == 3:
    kelvin = float(input('Enter the number of Kelvin to be converted to Celsius: '))
    celsius = kelvin - 273.15
    print(celsius, '°C', sep='')
elif counter_1 != 0 and counter_2 != 1 and counter_3 != 2 and counter_4 != 3:
    print()
    print('Please, select an operation')
