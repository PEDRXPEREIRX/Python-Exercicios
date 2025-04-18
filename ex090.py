aluno = {}
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Média de {aluno['Nome']}: '))
if aluno['Média'] < 7:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'

for i, j in aluno.items():
    print(f'{i} é igual a {j}')
