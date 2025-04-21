from time import sleep


def maior(*valor):
    if len(valor) == 0:
        sleep(0.5)
        print('Analisando os valores passados...')
        sleep(0.5)
        print('-> Não foi informado nenhum valor!')
        print('='*50)
    else:
        maiorNum = 0
        print('Analisando os valores passados...')
        for i in range(len(valor)):
            if maiorNum < valor[i]:
                maiorNum = valor[i]
        for i in range(len(valor)):
            print(f'[{valor[i]}]', end=' ')
        print(f'-> Foram informados {len(valor)} valores ao todo.')
        print(f'O maior valor informado foi {maiorNum}.')
        print('='*50)

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
