from datetime import datetime

anoNascimento = int(input('Informe a data do seu nascimento: '))
anoAtual = datetime.now().year
idade = anoAtual - anoNascimento

if idade <= 9:
    print('Atleta categoria: MIRIM')
elif idade <= 14:
    print('Atleta categoria: INFANTIL')
elif idade <= 19:
    print('Atleta categoria: JUNIOR')
elif idade <= 20:
    print('Atleta categoria: SÊNIOR')
else:
    print('Atleta categoria: MASTER')