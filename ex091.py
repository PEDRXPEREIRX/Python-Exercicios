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

#Resolução Curso em Vídeo - Guanabara
# from random import randint
# from time import sleep
# from operator import itemgetter
#
# jogo = {'jogador1': randint(1,6),
#         'jogador2': randint(1,6),
#         'jogador3': randint(1,6),
#         'jogador4': randint(1,6)}
#
# print('Valores sorteados: ')
# for k, v in jogo.items():
#     print(f'{k} tirou {v} no dado.')
#     sleep(1)
#
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print()
# for i, v in enumerate(ranking):
#     print(f'{i+1}º lugar: {v[0]} com {v[1]}!')
#     sleep(0.5)
