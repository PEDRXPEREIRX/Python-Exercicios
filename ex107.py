from uteis import moeda

p = float(input('Informe o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p):.1f}')
print(f'O dobro de {p} é {moeda.dobro(p):.1f}')
print(f'Aumentando 10%, temos {moeda.aumentar(p):.1f}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p):.1f}')
