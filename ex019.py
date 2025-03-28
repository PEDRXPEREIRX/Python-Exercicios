from random import choice

alunos = []

for i in range(1, 5):
    entrada = input(f'Digite o nome do aluno {i}: ')
    alunos.append(entrada)

alunoSorteado = choice(alunos)

print(f'O aluno sorteado foi o {alunoSorteado}!')


# alunoSorteado = randint(1, 4)
#
# if (alunoSorteado == 1):
#     print('O aluno sorteado foi o Miguel')
# elif (alunoSorteado == 2):
#     print('O aluno sorteado foi o Robin')
# elif (alunoSorteado == 3):
#     print('O aluno sorteado foi o Luno')
# elif(alunoSorteado == 4):
#     print('O aluno sorteado foi o Duke')