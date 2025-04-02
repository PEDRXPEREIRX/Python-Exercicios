#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar - Se é a hora de se alistar - Se já passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime

anoNascimento = int(input('Informe o ano do seu nascimento: ').strip())
anoAtual = datetime.now().year
idade = anoAtual - anoNascimento

if idade > 18:
    alistamento = input(f'Já serviu às Forças Armadas ou foi dispensado do período obrigatório? [SIM] ou [NAO] ').upper().strip()
    if alistamento == 'SIM':
        print(f'Excelente!!!')
    elif alistamento == 'NAO':
        print(f'ARREGO!!! Se apresente em uma junta militar o mais rápido!')
elif idade < 18:
    print(f'Dentro de {18 - idade} anos você tem que se alistar, guerreiro!')
else:
    print(f'É hora de se alistar, combatente!')