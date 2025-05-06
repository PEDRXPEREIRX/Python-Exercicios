# def aumentar(num, aumento ,cond=False):
#     inteiro = 1
#     aumento = inteiro + (aumento / 100)
#
#     if cond == True:
#         return f'R${num*aumento:.2f}'
#     else:
#         return num * aumento
#
#
# def diminuir(num, reducao, cond=False):
#     reducao = reducao / 100
#
#     if cond == True:
#         return f'R${num - (num * reducao):.2f}'
#     else:
#         return num - (num * reducao)
#
#
# def dobro(num, cond=False):
#     if cond == True:
#         return f'R${num*2:.2f}'
#     else:
#         return num*2
#
#
# def metade(num, cond=False):
#     if cond == True:
#         return f'R${num/2:.2f}'
#     else:
#         return num/2
#
#
# def moeda(num, cond=False):
#     return f'R${num:.2f}'
#
#
# def resumo(num, aumento, reducao):
#     print('-'*31)
#     print(f'{" RESUMO DO VALOR":^30}')
#     print('-'*31)
#     print(f'Preço analisado: {moeda(num):>14}')
#     print(f'Dobro do preço: {dobro(num, True):>15}')
#     print(f'Metade do preço: {metade(num, True):>14}')
#     print(f'{aumento}% de aumento: {aumentar(num, aumento, True):>15}')
#     print(f'{reducao}% de redução: {diminuir(num, reducao, True):>15}')


#Código Guanabara
def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    msg = f'{moeda}{preco:.2f}'.replace('.',',')
    return msg


def resumo(preco=0, aumento=10, reducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: {moeda(preco):>13}')
    print(f'Dobro do preço: {dobro(preco, True):>14}')
    print(f'Metade do preço: {metade(preco, True):>13}')
    print(f'{aumento}% de aumento: {aumentar(preco, aumento, True):>14}')
    print(f'{reducao}% de redução: {diminuir(preco, reducao, True):>14}')
