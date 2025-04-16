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
