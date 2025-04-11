valores = []
for i in range(5):
    valor = int(input('Digite um valor: '))
    valores.append(valor)

print('Valores da lista:', *valores)
print(f'O maior valor da lista foi {max(valores)} na posição {valores.index(max(valores))+1}')
print(f'O menor valor da lista foi {min(valores)} na posição {valores.index(min(valores))+1}')