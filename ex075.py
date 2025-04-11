numeros = []
pares = []

for i in range(5):
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)

tupla = tuple(numeros)
paresTupla = tuple(pares)

print(f'Você digitou os valores: ', *numeros)
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram: ', *paresTupla)
