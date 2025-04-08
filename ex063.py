print(' - Sequência de Fibonacci - ')
numA = 0
numB = 1
cont = 0

limite = int(input('Quantos termos deseja ver na sequência? '))

while cont < limite:
    numC = numA + numB
    print(f'{numA}', end=' -> ')
    numA = numB
    numB = numC
    cont += 1

print('FIM')