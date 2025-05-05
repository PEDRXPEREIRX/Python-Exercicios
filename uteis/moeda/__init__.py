def aumentar(num, aumento ,cond=False):
    inteiro = 1
    aumento = inteiro + (aumento / 100)

    if cond == True:
        return f'R${num*aumento:.0f},00'
    else:
        return num * aumento


def diminuir(num, reducao, cond=False):
    reducao = reducao / 100

    if cond == True:
        return f'R${num - (num * reducao):.0f},00'
    else:
        return num - (num * reducao)


def dobro(num, cond=False):
    if cond == True:
        return f'R${num*2:.0f},00'
    else:
        return num*2


def metade(num, cond=False):
    if cond == True:
        return f'R${num/2:.0f},00'
    else:
        return num/2


def moeda(num, cond=False):
    return f'R${num:.0f},00'


def resumo(num, aumento, reducao):
    print('-'*31)
    print(f'{" RESUMO DO VALOR":^30}')
    print('-'*31)
    print(f'Preço analisado: {moeda(num):>14}')
    print(f'Dobro do preço: {dobro(num, True):>15}')
    print(f'Metade do preço: {metade(num, True):>14}')
    print(f'{aumento}% de aumento: {aumentar(num, aumento, True):>15}')
    print(f'{reducao}% de redução: {diminuir(num, reducao, True):>15}')