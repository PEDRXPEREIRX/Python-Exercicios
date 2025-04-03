#Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice

while True:
    jokenpo = ['pedra', 'papel', 'tesoura']
    jokenpo = choice(jokenpo)
    escolha = input('Qual sua escolha: pedra, papel ou tesoura? ').lower().strip()

    if jokenpo == escolha:
        print(f'A máquina jogou {jokenpo} e você {escolha}! Nesse caso, deu empate!')
    elif (jokenpo == 'pedra') and (escolha == 'tesoura'):
        print(f'A máquina jogou {jokenpo} e você jogou {escolha}! Portanto, você perdeu!')
    elif (jokenpo == 'papel') and (escolha == 'pedra'):
        print(f'A máquina jogou {jokenpo} e você jogou {escolha}! Portanto, você perdeu!')
    elif (jokenpo == 'tesoura') and (escolha == 'papel'):
        print(f'A máquina jogou {jokenpo} e você jogou {escolha}! Portanto, você perdeu!')
    elif (escolha == 'pedra') and (jokenpo == 'tesoura'):
        print(f'Você jogou {escolha} e a máquina jogou {jokenpo}! Parabéns!!! Você ganhou :)')
    elif (escolha == 'papel') and (jokenpo == 'pedra'):
        print(f'Você jogou {escolha} e a máquina jogou {jokenpo}! Parabéns!!! Você ganhou :)')
    elif (escolha == 'tesoura') and (jokenpo == 'papel'):
        print(f'Você jogou {escolha} e a máquina jogou {jokenpo}! Parabéns!!! Você ganhou :)')
    else:
        print('Escolha inválida!')

    continuar = input('Deseja continuar jogando? [SIM] ou [NAO] ').upper().strip()
    if continuar != 'SIM':
        break