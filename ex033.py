num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

menorNum = num1
maiorNum = num1

if num2 < menorNum:
    menorNum = num2
if num3 < menorNum:
    menorNum = num3

if num2 > maiorNum:
    maiorNum = num2
if num3 > maiorNum:
    maiorNum = num3

print(f'O menor número digitado foi {menorNum} e o maior foi {maiorNum}!')