from random import randint
from time import sleep

tentativas = 0
num = randint(0,10)

print('Sou seu computador', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(1)
print('Será que você consegue adivinhar qual foi?')
sleep(0.5)

resp = int(input('Qual é seu palpite? '))
tentativas += 1

while resp != num:
    if num > resp:
        print('Mais... Tente mais uma vez')
        resp = int(input('Qual é seu palpite? '))
        tentativas += 1
    elif num < resp:
        print('Menos... Tente mais uma vez')
        resp = int(input('Qual é seu palpite? '))
        tentativas += 1

if tentativas == 1:
    print(f'Acertou com {tentativas} tentativa. Parabéns!')
else:
    print(f'Acertou com {tentativas} tentativas. Parabéns!')