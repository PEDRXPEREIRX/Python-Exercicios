numA = int(input('Primeiro valor: '))
numB = int(input('Segundo valor: '))

while True:
    escolha = int(input('\n[1] SOMAR\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] SAIR DO PROGRAMA\n\n'))

    if escolha == 1:
        print(f'\nA soma entre {numA} + {numB} é {numA + numB}')
    elif escolha == 2:
        print(f'\nO resultado de {numA} x {numB} é {numA * numB}')
    elif escolha == 3:
        if numA > numB:
            print(f'\nEntre {numA} e {numB} o maior é {numA}')
        elif numB > numA:
            print(f'\nEntre {numA} e {numB} o maior é {numB}')
        else:
            print(f'\nOs dois números são iguais ({numA})')
    elif escolha == 4:
        numA = int(input('Primeiro valor: '))
        numB = int(input('Segundo valor: '))
    elif escolha == 5:
        break
    else:
        print('\nOpção inválida. Tente novamente.')

print('\nPrograma finalizado!!!')