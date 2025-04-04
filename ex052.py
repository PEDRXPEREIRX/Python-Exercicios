#Faca um programa que leia um numero inteiro e diga se ele é ou nao um numero primo
from math import sqrt
num = int(input('Digite um número: '))

if num < 2:
    print(f'{num} não é primo')
else:
    primo = True

    for i in range(2, int(sqrt(num)) + 1):
        if num % 1 == 0:
            primo = False
            break

    if primo:
        print(f'{num} é primo')
    else:
        print(f'{num} não é primo')