volume_1, temperature_1 = float(input('Enter the amount of water in the first bowl: ')),\
                          float(input('Enter the temperature of the water in the first bowl: '))
print()
volume_2, temperature_2 = float(input('Enter the amount of water in the second bowl: ')),\
                          float(input('Enter the temperature of the water in the second bowl: '))
print()
if volume_1 <= 0 and volume_2 <= 0:
    print('The volume of water must be greater than zero')
else:
    average_temperature = (volume_1 * temperature_1 + volume_2 * temperature_2)/(volume_1 + volume_2)
    volume = volume_1 + volume_2
    print('The average mixture temperature is ', average_temperature, '°C', sep='')
    print('The mixture volume is ', volume, 'L', sep='')
