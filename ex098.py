from time import sleep


def contador():
    print('=' * 30)
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1, 11):
        print(f'{i}', end=' ')
        sleep(0.5)
    print('FIM!')
    print('=' * 30)
    print('Contagem de 10 até 0 de 2 em 2')
    for i in range(10, -1, -2):
        print(f'{i}', end=' ')
        sleep(0.5)
    print('FIM!')
    print('='*30)
    print('Agora é sua vez de de personalizar a contagem!')
    inicio = int(input(f'{"Início:":<8}'))
    fim = int(input(f'{"Fim:":<8}'))
    passo = int(input(f'{"Passo:":<8}'))
    if inicio < fim:
        for i in range(inicio, fim+1, passo):
            print(f'{i}', end=' ')
            sleep(0.5)
        print('FIM!')
    else:
        for i in range(inicio, fim-1, - passo):
            print(f'{i}', end=' ')
            sleep(0.5)
        print('FIM!')


contador()