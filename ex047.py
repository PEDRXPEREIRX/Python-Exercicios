#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for i in range(1, 50):
    if (i % 2 == 0):
        print(i, end=' ')

#Resolução do Guanabara:
# for n in range(2, 51, 2):
#     print(n, end=' ')
# print('Acabou')
#
#Ao inves de usar 'if', da para inicializar o for ja
#no numero dois que é par e pular de 2 em 2 ate o 50