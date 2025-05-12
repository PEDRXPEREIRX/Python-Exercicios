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

#Código Guanabara:
# def leiaInt(msg):
#     while True:
#         try:
#             n = int(input(msg))
#         except (ValueError, TypeError):
#             print('\033[1;31mERRO: Por favor, digite um número inteiro válido!\033[m')
#             continue
#         except (KeyboardInterrupt):
#             print('\n\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
#             return 0
#         else:
#             return n
#
#
# def leiaFloat(msg):
#     while True:
#         try:
#             n = float(input(msg))
#         except (ValueError, TypeError):
#             print('\033[1;31mERRO: Por favor, digite um número real válido!\033[m')
#             continue
#         except (KeyboardInterrupt):
#             print('\n\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
#             return 0
#         else:
#             return n
#
#
# n1 = leiaInt('Digite um Inteiro: ')
# n2 = leiaFloat('Digite um Real: ')
# print(f'O valor inteiro digitado foi {n1} e o real foi {n2} :)')
