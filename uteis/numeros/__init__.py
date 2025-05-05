def fatorial(n, show=False):
    f = 1
    for c in range(1, n+1):
        f *= c
        if show:
            print(f'{c}', end='')
            if c == n:
                print(' = ', end='')
            else:
                print(' x ', end='')
    return f


def dobro(n):
    return n*2


def triplo(n):
    return n*3
