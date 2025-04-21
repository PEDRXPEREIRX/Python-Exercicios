def area():
    print(f'{"CONTROLE DE TERRENOS":^30}')
    print('-' * 30)
    largura = float(input('Largura [m]: '))
    altura = float(input('Altura [m]: '))
    total = largura * altura
    print(f'A área de um terreno {largura:.1f} x {altura:.1f} é de {total:.1f}m²')


area()
