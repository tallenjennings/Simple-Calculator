"""simple calculator"""


#define functions

#addition
def add(a, b):
    return a + b

#subtraction
def subtract(a, b):
     return a - b

#multiply
def multiply(a, b):
    return a * b

#division
def divide(a, b):
    return a / b

#power
def power(a, b):
    return pow(a, b)

#User input
def calc():
    print('1 for add')
    print('2 for subtract')
    print('3 for multiply')
    print('4 for divide')
    print('5 for power')

    choice = input(':')
    
    num1 = int(input('First number: '))
    num2 = int(input('Second number: '))


    #using functions
    if choice == '1':
        print(add(num1, num2))

    elif choice == '2':
        print(subtract(num1, num2))

    elif choice == '3':
        print(multiply(num1, num2))

    elif choice == '4':
        print(divide(num1, num2))

    elif choice == '5':
         print(power(num1, num2))

    else:
        print('Invalid Selection')

#call program
calc()
