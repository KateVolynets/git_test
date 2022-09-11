side_1=float(input('Enter first side: '))
side_2=float(input('Enter second side: '))
if side_1>0 and side_2>0:
    area= 0.5 * side_2 * side_1
    print('The area of the triangle is', area, sep=" = ")
else:
    print('Error input')