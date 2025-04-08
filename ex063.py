numAnt = 0
numPost = 1

print('''------------------------
 Sequência de Fibonacci
------------------------''')

limite = int(input('Quantos números deseja mostrar? '))
cont = 0

while cont < limite:
    print(numAnt, end=' 🠒 ')
    numFib = numAnt + numPost
    numAnt = numPost
    numPost = numFib
    cont += 1

print('FIM')
