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
