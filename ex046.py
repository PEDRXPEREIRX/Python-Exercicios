#Faca um programa que mostre na tela uma contagem regressiva de 10 até 0, com uma pausa de 1 segundo entre eles

from time import sleep

for i in range(10, -1, -1):
    print(i)
    sleep(1)

print('BOOOOOOOMMMMM')