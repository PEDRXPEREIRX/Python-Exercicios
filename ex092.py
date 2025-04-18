from datetime import datetime

dados = {}
dados['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('N° carteira de trabalho: (0 não tem) '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = ((datetime.now().year - nascimento) - (datetime.now().year - dados['contratação'])) + 35

print('-=-'*10)
print(dados)
for c, v in dados.items():
    print(f'{c} tem valor {v}')