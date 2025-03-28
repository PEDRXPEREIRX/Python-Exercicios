from random import shuffle

alunos = []

for i in range(1, 5):
    entrada = input('Digite o nome do aluno: ')
    alunos.append(entrada)

shuffle(alunos)

print(f'A ordem da apresentação será: {alunos}')