#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
#a ser sacada (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

while True:
    valor = int(input('Informe o valor do saque: '))

    cem = valor // 100
    sobra = valor - (cem * 100)
    cinquenta = sobra // 50
    sobra -= cinquenta * 50
    vinte = sobra // 20
    sobra -= vinte * 20
    dez = sobra // 10
    sobra -= dez * 10
    cinco = sobra // 5
    sobra -= cinco * 5
    um = sobra

    if cem > 0:
        print(f'Total de {cem} cédulas de R$100')
    if cinquenta > 0:
        print(f'Total de {cinquenta} cédulas de R$50')
    if vinte > 0:
        print(f'Total de {vinte} cédulas de R$20')
    if dez > 0:
        print(f'Total de {dez} cédulas de R$10')
    if cinco > 0:
        print(f'Total de {cinco} cédulas de R$5')
    if um > 0:
        print(f'Total de {um} cédulas de R$1')

    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while continuar not in 'SsNn':
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
