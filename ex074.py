from random import choices

num = choices(range(0,10), k=5)
numeros = (num)

print(f'Os valores sorteados foram: ', end='')
print(*numeros)
print(f'O maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')

