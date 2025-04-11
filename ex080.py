from bisect import insort

valores = []

for _ in range(5):
    valor = int(input('Digite um valor: '))
    insort(valores, valor)

print('Valores da lista em ordem:', *valores)