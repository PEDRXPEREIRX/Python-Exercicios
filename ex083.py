
expressao = input('Digite a expressão: ')
if expressao.count('(') == expressao.count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')