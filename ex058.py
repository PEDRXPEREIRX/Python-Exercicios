from random import randint
from time import sleep

print('Sou seu computador', end='')
sleep(0.5)
for _ in range(3):
    print('.', end='')
    sleep(0.5)
print('\nAcabei de pensar em um número entre 0 e 10.')
sleep(1)
print('Será que você consegue adivinhar qual foi?')
sleep(0.5)

num = randint(0,10)
tentativas = 0

while True:
    resp = int(input('Qual é seu palpite? '))
    tentativas += 1
    if num == resp:
        break
    else:
        if num > resp:
            print('Mais... Tente mais uma vez')
        else:
            print('Menos... Tente mais uma vez')

if tentativas == 1:
    print(f'Acertou com {tentativas} tentativa. Parabéns!')
else:
    print(f'Acertou com {tentativas} tentativas. Parabéns!')