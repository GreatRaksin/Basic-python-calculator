# добавим перечень операций, которые можно использовать в калькуляторе
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

# Addition
print('{} + {} = '.format(number_1, number_2))
print(number_1 + number_2)
# Subtraction
print('{} - {} = '.format(number_1, number_2))
print(number_1 - number_2)
# Multiplication
print('{} * {} = '.format(number_1, number_2))
print(number_1 * number_2)
# Division
print('{} / {} = '.format(number_1, number_2))
print(number_1 / number_2)

# если запустить код, то ничего происходить не будет. У нас не созданы условия
