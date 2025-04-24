def ajuda():
    solicitado = ''
    while solicitado != 'fim':
        print('\033[1;42m~' * 27)
        print('  SISTEMA DE AJUDA PyHELP  ')
        print('~' * 27)
        print('\033[m')
        solicitado = input('Função ou Biblioteca > ')
        if solicitado == 'fim':
            print('\033[1;41m~'*13)
            print('  ATÉ LOGO!  ')
            print('~'*13)
            print('\033[m')
            break
        tamanho = len(solicitado) + 36
        print('\033[1;44m~' * tamanho)
        print(f'  Acessando o manual do comando "{solicitado}" ')
        print('~' * tamanho)
        print('\033[m')
        print('\033[7;40m')
        help(solicitado)
        print('\033[m')


ajuda()

#Código Guanabara
# from time import sleep
#
# c = ('\033[m',        # 0 -> Sem cores
#      '\033[1;41m', # 1 -> vermelho
#      '\033[1;42m', # 2 -> verde
#      '\033[1;43m', # 3 -> amarelo
#      '\033[1;44m', # 4 -> azul
#      '\033[1;45m', # 5 -> roxo
#      '\033[7;40m')    # 6 -> branco
#
#
# def ajuda(com):
#     titulo(f'Acessando o manual do comando "{com}"', 4)
#     print(c[6], end='')
#     help(com)
#     print(c[0], end='')
#     sleep(2)
#
#
# def titulo(msg, cor=0):
#     tam = len(msg) + 4
#     print(c[cor], end='')
#     print('~' * tam)
#     print(f'  {msg}')
#     print('~' * tam)
#     print(c[0], end='')
#     sleep(1)
#
#
# comando = ''
# while True:
#     titulo('SISTEMA DE AJUDA PyHELP', 2)
#     comando = input('Função ou Biblioteca > ')
#     if comando.upper() == 'FIM':
#         break
#     else:
#         ajuda(comando)
#
# titulo('ATÉ LOGO', 1)
