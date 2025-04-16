valores = []
pares = []
impares = []

for i in range(7):
    valor = int(input('Valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

parOrd = sorted(pares)
imparOrd = sorted(impares)

valores.append(parOrd)
valores.append(imparOrd)

print(f'Os valores em ordem crescente de números PARES e ÍMPARES: \n{valores}\n'
      f'Somente os valores PARES: {parOrd}\n'
      f'Somente os valores ÍMPARES: {imparOrd}')

#Código do Curso em Vídeo - Gustavo Guanabara
# num = [[], []]
#
# for i in range(7):
#     valor = int(input(f'Digite o {i+1}º valor: '))
#     if valor % 2 == 0:
#         num[0].append(valor)
#     else:
#         num[1].append(valor)
#
# num[0].sort()
# num[1].sort()
#
# print(f'Os valores PARES digitados foram: {num[0]}\n'
#       f'Os valores ÍMPARES digitados foram: {num[1]}')
