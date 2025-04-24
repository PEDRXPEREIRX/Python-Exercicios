def leiaInt(mensagem):
    resposta = input(mensagem)
    while not resposta.isdigit():
        print('ERRO! Digite um número inteiro válido.')
        resposta = input(mensagem)
    return int(resposta)

n = leiaInt('Digite um número: ')
print(f'\nVocê digitou o número {n}')
