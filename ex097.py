def escreva(mensagem):
    tamanho = len(mensagem) + 2
    print('~'*tamanho)
    print(f' {mensagem} ')
    print('~'*tamanho)


escreva(input('Digite uma frase: '))
