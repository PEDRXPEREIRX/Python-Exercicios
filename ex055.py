#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


maiorPeso = 0
menorPeso = 0

for i in range(0,5):
    peso = int(input(f'Pessoa {i+1}, informe o seu peso: '))

    if i == 0:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso


print(f'O menor peso foi {menorPeso} e o maior foi {maiorPeso}')