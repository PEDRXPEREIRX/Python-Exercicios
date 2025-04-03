#Crie um programa que faça o computador jogar Jokenpô com você.
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