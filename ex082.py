ambos = []
par = []
impar = []

for _ in range(5):
    valor = int(input('Digite um valor: '))
    ambos.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print(f'{"Conteúdo da lista geral: ":<23}', *ambos, f'\n'
      f'{"Conteúdo da lista PAR: ":<25}', *par, f'\n'
      f'{"Conteúdo da lista ÍMPAR: ":<23}', *impar)
