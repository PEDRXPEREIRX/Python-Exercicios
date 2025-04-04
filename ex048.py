#Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no
#intervalo de 1 ate 500
soma = 0
for i in range(1, 500):
    if (i % 2 == 1) and (i % 3 == 0):
        soma += i
print(f'A soma de todos números ímpares que são múltiplos de três no intervalo do Python de 1 à 500 é {soma}.')
