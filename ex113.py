def leiaInt(mensagem):
    while True:
        try:
            resposta = int(input(mensagem))
            return resposta
        except ValueError:
            print('\033[1;31mERRO: Informe um valor inteiro válido!\033[m')


def leiaFloat(mensagem):
    while True:
        try:
            resposta = float(input(mensagem).replace(',','.'))
            return resposta
        except ValueError:
            print('\033[1;31mERRO: Informe um valor real válido!\033[m')


numI = leiaInt('Digite um Inteiro: ')
numR = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {numI} e o valor real foi {numR}'.replace('.',','))
