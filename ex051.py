#Desenvolva um programa que leia o primeiro termo e a razao de uma pogressao aritmetica. No final, mostre os 10
#primeiros termos dessa progressao

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiroTermo + (10 - 1) * razao

for i in range(primeiroTermo, decimo + razao, razao):
    print(i)


