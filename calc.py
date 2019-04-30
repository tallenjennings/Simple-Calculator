"""simple calculator"""


#User input to choose function
def calc():
    print('1 for add')
    print('2 for subtract')
    print('3 for multiply')
    print('4 for divide')
    print('5 for power')

    choice = input(':')
    
    #Using functions to 
    if choice == '1':
        print(add(int(input('First number: ')), int(input('Second number: '))))
    elif choice == '2':
        print(subtract(int(input('First number: ')), int(input('Second number: '))))
    elif choice == '3':
        print(multiply(int(input('First number: ')), int(input('Second number: '))))
    elif choice == '4':
        print(divide(int(input('First number: ')), int(input('Second number: '))))
    elif choice == '5':
        print(power(int(input('First number: ')), int(input('Second number: '))))
    else:
        print('Invalid Selection')

#Define functions
#Addition
def add(a, b):
    return a + b

#Subtraction
def subtract(a, b):
     return a - b

#Multiply
def multiply(a, b):
    return a * b

#Division
def divide(a, b):
    return a / b

#Power
def power(a, b):
    return pow(a, b)

#Call program
cont = 'y'
while cont.lower() == 'y':
    calc()
    cont = input('Continue?y/n:')
    if cont == 'n':
        break
    


