ficha = {}
soma = 0
gol = []
ficha['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {ficha['nome']} jogou? '))

for i in range(partidas):
    gols = int(input(f'Quantos gols na partida {i+1}? '))
    gol.append(gols)
    soma += gols

ficha['gols'] = gol
ficha['total'] = soma
print('-='*30)
print(ficha)
print('-='*30)

for i, j in ficha.items():
    print(f'O campo {i} tem valor {j}')

print('-='*30)
print(f'O jogador {ficha['nome']} jogou {partidas} partidas.')

for i in range(partidas):
    print(f' -> Na partida {i+1}, fez {ficha['gols'][i]} gols.')

print(f'Foi um total de {ficha['total']} gols.')
