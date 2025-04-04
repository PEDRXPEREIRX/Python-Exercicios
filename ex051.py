#Desenvolva um programa que leia o primeiro termo e a razao de uma pogressao aritmetica. No final, mostre os 10
#primeiros termos dessa progressao

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
progressao = primeiroTermo + 10 * razao

for i in range(primeiroTermo, progressao, razao):
    print(i)


