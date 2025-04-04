#Crie um programa que leia o ano de nascimento de 7 pessoas, no final, mostre quantas pessoas ainda não atingiram
#a maioridade e quantas já são maiores.
maiorIdade = 0
menorIdade = 0

for i in range(0, 7):
    idade = int(input(f'Pessoa {i+1}, informe a sua idade:'))
    if idade < 18:
        menorIdade += 1
    else:
        maiorIdade += 1

print(f'Das 7 pessoas, {menorIdade} são menores de idade e {maiorIdade} são maiores de idade!')