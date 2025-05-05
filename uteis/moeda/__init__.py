def aumentar(num, cond=False):
    if cond == True:
        return f'R${num*1.10:.0f},00'
    else:
        return num * 1.10


def diminuir(num, cond=False):
    if cond == True:
        return f'R${num - (num * 0.13):.0f},00'
    else:
        return num - (num * 0.13)


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


