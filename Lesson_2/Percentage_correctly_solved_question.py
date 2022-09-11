number_questions = int(input('Please, enter the total number of questions: '))
correctly_answered = int(input('Please, enter the number of correctly answered questions: '))
if number_questions <= 0 or correctly_answered < 0:
    print("The number of questions and answered must be greater than 0")
elif number_questions == correctly_answered:
    print('Congratulations, you answered all questions correctly ', 100, '%', sep='')
elif correctly_answered == 0:
    print("Don't be discouraged, try taking the test again ", 0, '%', sep='')
elif correctly_answered > number_questions != 0 and correctly_answered != 0:
    print('The number of correct answers cannot exceed the number of questions')
else:
    percentage_of_correctly_solved_tasks = (correctly_answered/number_questions) * 100
    if percentage_of_correctly_solved_tasks % 10 == 0:
        percentage_of_correctly_solved_tasks = int(percentage_of_correctly_solved_tasks)
    print('Percentage of correctly solved tasks = ', percentage_of_correctly_solved_tasks, '%', sep='')
