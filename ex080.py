valores = []

for i in range(10):
    valor = int(input('Digite um valor: '))
    if i == 0:
        print('Adicionado à lista!')
        valores.append(valor)
    elif valor > valores[-1]:
        print('Adicionado ao final da lista!')
        valores.append(valor)
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                print(f'Adicionado na posição {pos} da lista!')
                valores.insert(pos, valor)
                break
            pos += 1

print('Valores da lista em ordem:', *valores)
