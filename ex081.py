numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while resp not in 'SsNn':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break

num = sorted(numeros, reverse=True)
print(f'Total de números digitados: {len(numeros)}.')
print('Valores da lista em ordem decrescente:', *num)
if 5 in numeros:
    print(f'O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
