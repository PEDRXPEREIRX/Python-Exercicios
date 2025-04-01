from random import choice

continuar = 'SIM'
numeros = [0, 1, 2, 3, 4 , 5]

while True:
    numeroAleatorio = int(input('Entre 0 e 5, tenter adivinhar o número aleatório que a máquina escolheu: ').strip())
    numeroSorteado = choice(numeros)
    if numeroSorteado == numeroAleatorio:
        print(f'Parabéns!!! Você acertou o número {numeroSorteado}!!!')
    else:
        print(f'Não foi dessa vez! O número era {numeroSorteado}')

    continuar = input('Deseja continuar? Digite SIM ou NAO ').strip().upper()
    if continuar == 'NAO':
        break