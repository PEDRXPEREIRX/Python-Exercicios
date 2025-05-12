def leiaInt(mensagem):
    while True:
        try:
            resposta = int(input(mensagem))
            return resposta
        except ValueError:
            print('\033[1;31mERRO: Informe um valor inteiro válido!\033[m')


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c}\033[m - \033[1;34m{item}\033[m')
        c += 1
    opc = leiaInt('\033[1;32mSua Opção: \033[m')
    return opc