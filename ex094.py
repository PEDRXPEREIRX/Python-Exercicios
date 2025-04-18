pessoas = []
mulheres = []
mediaGrupo = []
soma = media = 0
while True:
    nome = input('Nome: ').strip()
    sexo = input('Sexo [M/F]: ').upper().strip()[0]
    idade = int(input('Idade: ').strip())
    dados = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(dados)
    if sexo == 'F':
        mulheres.append(dados['nome'])
    stop = input('Continuar cadastrando? [S/N] ').upper().strip()[0]
    if stop == 'N':
        break

print(f'Total de pessoas cadastradas: {len(pessoas)}')
for i in range(len(pessoas)):
    print(f'[{pessoas[i]['nome']}]', end=' ')
    soma += pessoas[i]['idade']

media = soma / len(pessoas)
print()
print(f'Média de idade do grupo: {media:.0f}')
print(f'Mulheres do grupo:', *mulheres)
print(f'Pessoas com idade acima da média do grupo:')
for i in range(len(pessoas)):
    if pessoas[i]['idade'] > media:
        mediaGrupo.append(pessoas[i]['nome'])
print(*mediaGrupo)
