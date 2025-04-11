valores = []
maior = menor = 0
for i in range(5):
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    if i == 0:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print('Valores da lista:', *valores)
print(f'O maior valor da lista foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1}... ', end='')
print(f'\nO menor valor da lista foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i+1}... ', end='')
print()