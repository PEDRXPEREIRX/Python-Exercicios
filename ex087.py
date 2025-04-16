matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = coluna = linha = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()

for l in range(3):
    coluna += matriz[l][2]

for c in range(3):
    if linha < matriz[1][c]:
        linha = matriz[1][c]

print(f'Soma dos valores pares: {par}\n'
      f'Soma dos valores da terceira coluna: {coluna}\n'
      f'Maior valor da segunda linha: {linha}')