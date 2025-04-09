from random import randint

totVit = 0
print('=-=' * 8)
print('Vamos jogar PAR ou ÍMPAR')
print('=-=' * 8)

while True:
    num = randint(1, 100)
    valor = int(input('Digite um valor: '))
    parimpar = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    soma = num + valor
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

    if (parimpar == 'P') and (soma % 2 == 0) or (parimpar == 'I') and (soma % 2 == 1):
        totVit += 1
        print('\nVocê venceu!!!\n'
              'Continue...\n')
    else:
        break

print(f'Você jogou {valor} e o computador {num}. Total de {soma} é {resultado}.')
print(f'GAMER OVER! Você venceu {totVit} vezes.')