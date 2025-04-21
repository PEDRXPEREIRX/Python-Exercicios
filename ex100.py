from random import sample


def sorteia(lista):
    print('Sorteando 05 valores da lista:', end=' ')
    lista.clear()
    lista.extend(sample(range(0, 10), 5))
    for i in range(len(lista)):
        print(f'{lista[i]}', end=' ')
    print()


def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
