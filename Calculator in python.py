# Calculator in Python

import sys

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

print('''
1 - Sum
2 - Subtraction
3 - Multiplication
4 - Division
S - Stop
''')

while True:
    print("Type one of the things above")

    tipo = input().lower()

    if tipo == 's':
        sys.exit()
    else:
        num1 = int(input("Type a number: "))
        num2 = int(input("Type a second number: "))

        if tipo == '1':
            result = soma(num1,  num2)
        elif tipo == '2':
            result = subtracao(num1, num2)
        elif tipo == '3':
            result = multiplicacao(num1, num2)
        elif tipo == '4':
            result = divisao(num1, num2)
        print(result)
        
