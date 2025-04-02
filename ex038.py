#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior - O segundo valor é maior - Não existe valor maior, os dois são iguais

numA = int(input('Digite o valor A: '))
numB = int(input('Digite o valor B: '))

if numA > numB:
    print(f'O valor A ({numA}) é maior que o valor B ({numB})')
elif numB > numA:
    print(f'O valor B ({numB}) é maior que o valor A ({numA})')
else:
    print(f'O valor A ({numA}) e o valor B ({numB}) são iguais!')