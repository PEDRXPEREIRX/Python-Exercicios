# def leiaDinheiro(msg):
#     while True:
#         entrada = input(msg)
#         try:
#             return float(entrada.replace(",", "."))
#         except ValueError:
#             print(f'\033[1;31mERRO: "{entrada}" é um valor inválido!\033[m')

#Código Guanabara
def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[1;31mERRO: "{entrada}" é um valor inválido!\033[m')
        else:
            valido = True
            return float(entrada)
