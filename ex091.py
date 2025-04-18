from random import randint
from time import sleep

jogador = {}
print('Valores sorteados:')
sleep(1)
for i in range(4):
    jogador[f'Jogador{i+1}'] = randint(1,6)
    print(f'    O jogador{i+1} tirou {jogador[f"Jogador{i+1}"]}')
    sleep(0.75)

ranking = sorted(jogador.items(), key=lambda item: item[1], reverse=True)

print('\nRanking dos jogadores:')
for pos, (nome, valor) in enumerate(ranking):
    print(f'    {pos+1}º lugar: {nome} com {valor}')
