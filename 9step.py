# Чтобы программу не пришлось перезапускать после каждого обработанного примера, нужно определить несколько функций.
# определение функции calculate

def calculate():

    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    % for modulo
    ** for exponent
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

    elif operation == '%':
        # Modulo
        print('{} % {} = '.format(number_1, number_2))
        print(number_1 % number_2)

    elif operation == '**':
        # Exponent
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1 ** number_2)
        
    else:
        print('You put an unexisting symbol, please try again')
        again()

    # Определение функции again()
    def again():
        # Ввод пользователя
        calc_again = input('''
            Do you want to calculate again?
            Please type Y for YES or N for NO.
            ''')
        # Если пользователь вводит Y, программа запускает функцию calculate()
        if calc_again.upper() == 'Y': # давайте уберем чувствительность к регистру
            calculate()
        # Если пользователь вводит N, программа попрощается и завершит работу
        elif calc_again.upper() == 'N':
            print('Bye, my dear friend 😂.')
        # Если пользователь вводит другой символ, программа снова запускает функцию again()
        else:
            again()
        # Вызов calculate()
    again()
calculate()
