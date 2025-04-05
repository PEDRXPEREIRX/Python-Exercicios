#Crie um programa que leia o ano de nascimento de 7 pessoas, no final, mostre quantas pessoas ainda não atingiram
#a maioridade e quantas já são maiores.
from datetime import datetime

maiorIdade = 0
menorIdade = 0
anoAtual = datetime.now().year

for i in range(0, 7):
    anoNascimento = int(input(f'Pessoa {i+1}, informe a sua data de nascimento:'))
    idade = anoAtual - anoNascimento
    if idade < 18:
        menorIdade += 1
    else:
        maiorIdade += 1

if maiorIdade == 7:
    print('Todas pessoas são maiores de idade.')
elif menorIdade == 7:
    print('Todas pessoas são menores de idade.')
else:
    print(f'Das 7 pessoas, {menorIdade} são menores de idade e {maiorIdade} são maiores de idade!')