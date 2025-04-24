from datetime import datetime


def voto(idade):
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA!')
    elif idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    elif idade >= 18 and idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    else:
        print(f'Com {idade} anos: VOTO OPCIONAL!')


nascimento = datetime.now().year - int(input('Em que ano você nasceu? '))
voto(nascimento)
