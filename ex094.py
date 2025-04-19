pessoas = []
soma = media = 0
while True:
    nome = input('Nome: ').strip()
    sexo = input('Sexo [M/F]: ').upper().strip()[0]
    idade = int(input('Idade: ').strip())
    dados = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(dados)
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
print(f'Mulheres do grupo:', end=' ')
for i in pessoas:
    if i['sexo'] == 'F':
        print(f'[{i['nome']}]', end=' ')
print()
print(f'Pessoas com idade acima da média do grupo:', end=' ')
for i in pessoas:
    if i['idade'] > media:
        print(f'[{i['nome']}]', end=' ')
print()