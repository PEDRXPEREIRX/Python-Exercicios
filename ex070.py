print('-' * 20)
print(' LOJA SUPER BARATÃO ')
print('-' * 20)

nome = input('Nome do produto: ')
preco = float(input('Preço do produto: '))
total = menorValor = preco
barato = nome
valorbarato = preco
maisdemil = 0

while True:
    continuar = input('\nDeseja continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        break
    elif continuar == 'S':
        nome = input('\nNome do produto: ')
        preco = int(input('Preço do produto: '))
        total += preco
        if preco < menorValor:
            barato = nome
            valorbarato = preco
        if preco > maisdemil:
            maisdemil += 1

print('\n ----- FIM DO PROGRAMA ----- \n')
print(f'Total da compra foi R${total:.2f}\n'
      f'Temos {maisdemil} produtos custando mais de RS1000.00\n'
      f'Produto mais barato foi {barato} custando R${valorbarato:.2f}')
