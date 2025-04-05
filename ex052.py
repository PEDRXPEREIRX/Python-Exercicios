#Faca um programa que leia um numero inteiro e diga se ele é ou nao um numero primo

num = int(input('Informe um número: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[1;33m', end=' ')
        total += 1
    else:
        print('\033[1;31m', end=' ')
    print(i, end=' ')

if total == 2:
    print(f'\n\033[mO número {num} é um número primo :)')
else:
    print(f'\n\033[mO número {num} não é um número primo :|')