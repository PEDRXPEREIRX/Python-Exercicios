from random import sample
from time import sleep

jogos = []
print('-'*27)
print(f'{'M E G A   S E N A':^27}')
print('-'*27)
quant = int(input('Quantos jogos deseja gerar? '))

for i in range(quant):
    numeros = sample(range(1,60), 6)
    numeros.sort()
    jogos.append(numeros)

print(f'\n-=-= SORTEANDO {quant} JOGOS =-=-')
for i in range(quant):
    sleep(1)
    jogo_formatado = ' '.join(f'{n:02d}' for n in jogos[i])
    print(f'Jogo {i+1}: {jogo_formatado}')

print()
print('-'*27)
print(f'{'< B O A   S O R T E >':^27}')
print('-'*27)
