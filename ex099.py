from time import sleep


def maior(num):
    if len(num) == 0:
        sleep(0.5)
        print('Analisando os valores passados...')
        sleep(0.5)
        print('-> Não foi informado nenhum valor!')
        print('='*50)
    else:
        maiorNum = 0
        print('Analisando os valores passados...')
        for i in range(len(num)):
            if maiorNum < num[i]:
                maiorNum = num[i]
        for i in range(len(num)):
            print(f'[{num[i]}]', end=' ')
        print(f'-> Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {maiorNum}.')
        print('='*50)


num = [2,9,4,5,7,1]
maior(num)
num = [4,7,0]
maior(num)
num = [1,2]
maior(num)
num = [6]
maior(num)
num = []
maior(num)
