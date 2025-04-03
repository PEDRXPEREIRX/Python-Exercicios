#Crie um programa que faça o computador jogar Jokenpô com você.
# CÓDIGO FEITO POR EU MESMO

from random import choice
from time import sleep

pontuacaoMaquina = 0
pontuacaoJogador = 0
jokenpo = ['pedra', 'papel', 'tesoura']

while True:
    maquina = choice(jokenpo)
    escolha = input('Qual sua escolha: PEDRA, PAPEL ou TESOURA? \n').lower().strip()

    print('JO..')
    sleep(1)
    print('KEN..')
    sleep(1)
    print('PÔ!!!\n')

    if maquina == escolha:
        print(f'EMPATE! A máquina jogou {maquina} e você {escolha}! ')
    elif (maquina == 'pedra') and (escolha == 'tesoura'):
        print(f'Derrotado! A máquina jogou {maquina} e você jogou {escolha}! ')
        pontuacaoMaquina += 1
    elif (maquina == 'papel') and (escolha == 'pedra'):
        print(f'Derrotado! A máquina jogou {maquina} e você jogou {escolha}! ')
        pontuacaoMaquina += 1
    elif (maquina == 'tesoura') and (escolha == 'papel'):
        print(f'Derrotado! A máquina jogou {maquina} e você jogou {escolha}! ')
        pontuacaoMaquina += 1
    elif (escolha == 'pedra') and (maquina == 'tesoura'):
        print(f'Parabéns!!! Você ganhou :) - Você jogou {escolha} e a máquina jogou {maquina}! ')
        pontuacaoJogador += 1
    elif (escolha == 'papel') and (maquina == 'pedra'):
        print(f'Parabéns!!! Você ganhou :) - Você jogou {escolha} e a máquina jogou {maquina}! ')
        pontuacaoJogador += 1
    elif (escolha == 'tesoura') and (maquina == 'papel'):
        print(f'Parabéns!!! Você ganhou :) - Você jogou {escolha} e a máquina jogou {maquina}! ')
        pontuacaoJogador += 1
    else:
        print('Escolha inválida!')

    continuar = input('\nDeseja continuar jogando? [SIM] ou [NAO] ').upper().strip()
    if continuar != 'SIM':
        break

if pontuacaoJogador > pontuacaoMaquina:
    print(f'FIM DE JOGO\n'
          f'* Pontuações *\n'
          f'Máquina: {pontuacaoMaquina}\n'
          f'Jogador: {pontuacaoJogador}\n\n'
          f'Campeão: JOGADOR')
elif pontuacaoMaquina > pontuacaoJogador:
    print(f'FIM DE JOGO\n'
          f'* Pontuações *\n'
          f'Máquina: {pontuacaoMaquina}\n'
          f'Jogador: {pontuacaoJogador}\n\n'
          f'Campeão: MÁQUINA')
else:
    print(f'FIM DE JOGO\n'
          f'* Pontuações *\n'
          f'Máquina: {pontuacaoMaquina}\n'
          f'Jogador: {pontuacaoJogador}\n\n'
          f'Não houve nenhum campeão, terminou empatado!')



#CÓDIGO REAJUSTADO PELO CHAT GPT
#PEDI PARA ELE AVALIAR O MEU CÓDIGO E ELE DEIXOU DESSA FORMA
#ESTOU DEIXANDO JUNTO PARA ESTUDAR MELHOR A ESTRUTURA E MELHORAR MEUS FUTUROS CÓDIGOS
# from random import choice
# from time import sleep
#
# pontuacaoMaquina = 0
# pontuacaoJogador = 0
# jokenpo = ['pedra', 'papel', 'tesoura']
#
# while True:
#     maquina = choice(jokenpo)
#     escolha = input('Qual sua escolha: PEDRA, PAPEL ou TESOURA? \n').lower().strip()
#
#     if escolha not in jokenpo:
#         print('Escolha inválida! Tente novamente.')
#         continue
#
#     print('\nJO..')
#     sleep(1)
#     print('KEN..')
#     sleep(1)
#     print('PÔ!!!\n')
#
#     print(f'A máquina jogou {maquina} e você jogou {escolha}.')
#
#     if maquina == escolha:
#         print('EMPATE!')
#     elif (maquina == 'pedra' and escolha == 'tesoura') or \
#          (maquina == 'papel' and escolha == 'pedra') or \
#          (maquina == 'tesoura' and escolha == 'papel'):
#         print('Derrotado! A máquina venceu esta rodada.')
#         pontuacaoMaquina += 1
#     else:
#         print('Parabéns! Você venceu esta rodada.')
#         pontuacaoJogador += 1
#
#     continuar = input('\nDeseja continuar jogando? [SIM] ou [NAO] ').upper().strip()
#     if continuar != 'SIM':
#         break
#
# print(f'\nFIM DE JOGO\n'
#       f'* Pontuações *\n'
#       f'Máquina: {pontuacaoMaquina}\n'
#       f'Jogador: {pontuacaoJogador}')
#
# if pontuacaoJogador > pontuacaoMaquina:
#     print('Campeão: JOGADOR!')
# elif pontuacaoMaquina > pontuacaoJogador:
#     print('Campeão: MÁQUINA!')
# else:
#     print('Não houve campeão, terminou empatado!')