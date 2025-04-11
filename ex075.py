numeros = []
pares = []
tres = 0

for i in range(5):
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num == 3:
        tres += 1
    if num % 2 == 0:
        pares.append(num)

tupla = tuple(numeros)
paresTupla = tuple(pares)

print(f'Você digitou os valores: ', end='')
print(*numeros)
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if tres == 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
print(f'Os valores pares digitados foram: ', end='')
print(*paresTupla)
