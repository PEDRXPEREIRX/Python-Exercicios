def leiaInt(mensagem):
    resposta = input(mensagem)
    while not resposta.isdigit():
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        resposta = input(mensagem)
    return int(resposta)

n = leiaInt('Digite um número: ')
print(f'\nVocê digitou o número {n}')

#Código Guanabara
# def leiaInt(msg):
#     valor = 0
#     while True:
#         n = input(msg)
#         if n.isnumeric():
#             valor = int(n)
#             break
#         else:
#             print('\033[1;33mERRO! Digite um número inteiro válido!\033[m')
#     return valor
#
# n = leiaInt('Digite um número: ')
# print(f'Você acabou de digitar o número {n}.')
