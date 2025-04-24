def fatorial(num = 1, show=None):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    if show == True:
        for i in range(num, 1, -1):
            print(f'{i} x', end=' ')
        print('1 =', f)
    else:
        print(f)


fatorial(5, show=True)
