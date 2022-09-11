number_student=int(input('Enter number of students: '))
number_apple=float(input('Enter number of apples: '))
if number_apple>0 and number_student>0:
    number_apple_for_student= number_apple//number_student
    number_apple_in_basket=number_apple%number_student
    print('The number of apples that students received', number_apple_for_student, sep=" = ")
    print('The number of apples left in the basket', number_apple_in_basket, sep=" = ")
elif number_apple==0 or number_student==0:
    print("Can't share")
else:
    print('Incorrect input')