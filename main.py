import math


# adds two numbers
def add(x, y):
    return x + y


# subtracts two numbers
def subtract(x, y):
    return x - y


# multiplies two numbers
def multiply(x, y):
    return x * y


# divides two numbers
def divide(x, y):
    return x / y

# squares a number,
def square(x):
    return x * x

def square_root(x):
    return math.sqrt(x)


operations = ['add', 'subtract', 'multiply', 'divide', '', 'square', 'square root']


def calculator():
    print('Which operation would you like to do? Press "Enter" to break.')
    choice = input().lower()
    if choice not in operations:
        print('Invalid Input Try Again')
        calculator()
    if choice == '':
        return
    if choice == 'square' or choice == 'square root':
        try:
            x = int(input('X: '))
        except:
            print('That is not a number')
            calculator()
        if choice == 'square':
            print(str(x) + ' squared is ' + str(square(x)))
        if choice == 'square root':
            print('The square root of ' + str(x) + ' is ' + str(square_root(x)))
        print("Would you like to do another calculation? 'yes/no'")
        answer = input().lower()
        if answer == 'yes':
            calculator()
        else:
            return

    try:
        x = int(input('X: '))
    except:
        print('That is not a number')
        calculator()
    try:
        y = int(input('Y: '))
    except:
        print('That is not a number')
        calculator()
    if choice == 'add':
        print(str(x) + ' + ' + str(y) + ' = ' + str(add(x, y)))

    if choice == 'subtract':
        print(str(x) + ' - ' + str(y) + ' = ' + str(subtract(x, y)))

    if choice == 'multiply':
        print(str(x) + ' * ' + str(y) + ' = ' + str(multiply(x, y)))

    if choice == 'divide':
        print(str(x) + ' / ' + str(y) + ' = ' + str(divide(x, y)))

    print("Would you like to do another calculation? 'yes/no'")
    answer = input().lower()
    if answer == 'yes':
        calculator()
    else:
        return


calculator()
