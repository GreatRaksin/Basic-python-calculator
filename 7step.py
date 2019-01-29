
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division

''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    # Addition
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
elif operation == '-':
    # Subtraction
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
elif operation == '*':
    # Multiplication
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
elif operation == '/':
    # Division
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
else:
    print('Введен неверный символ')

# if будет выполнять сложение, elif другие действия, else будет возвращать ошибку,
# если символы будут неверными
# попробуйте добавить функцию, которая будет выдавать остаток от деления и возведение в степень
