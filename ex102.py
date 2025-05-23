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



#Código Guanabara
# def fatorial(n, show=False):
#     """
#     -> Calcula o fatorial de um número.
#     :param n: O número a ser calculado.
#     :param show: (opcional) Mostrar ou não a conta.
#     :return: O valor do fatorial de um número n.
#     """
#     f = 1
#     for c in range(n, 0, -1):
#         if show:
#             print(c, end='')
#             if c > 1:
#                 print(' x ', end='')
#             else:
#                 print(' = ', end='')
#         f *= c
#     return f
#
#
# print(fatorial(5, show=True))
# help(fatorial)