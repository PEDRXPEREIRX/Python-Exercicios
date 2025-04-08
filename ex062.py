from ex051 import primeiroTermo

print('Gerador de PA')
print('-=-=-=-=-=-=-')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
resp = 10

while resp != 0:
    total += resp
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
        print('PAUSA' if cont > 10 else '', end='')
    resp = int(input('\nQuantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')