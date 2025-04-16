from time import sleep

alunos = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, nota1, nota2, media])
    continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break

print('-=-'*7)
print(f'Nº.  Nome       Média')
print('-'*21)

for i in range(len(alunos)):
    print(f'{i+1:<3}  {alunos[i][0]:10}  {alunos[i][3]:<10.1f}')

print('-'*21)

while True:
    stop = int(input('Mostrar notas de qual aluno? \nDigite o número respectivo à ele (999 interrompe) '))
    if stop == 999:
        break
    print(f'\nNotas de {alunos[stop-1][0]}: {alunos[stop-1][1]} e {alunos[stop-1][2]}\n')

sleep(1)

print('\nFinalizando...')
