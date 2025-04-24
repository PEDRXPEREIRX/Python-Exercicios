from unicodedata import digit


def ficha(nome='', gols=''):
    if nome == '':
        n = '<desconhecido>'
    else:
        n = nome
    if gols.isdigit():
        g = int(gols)
    else:
        g = 0

    return f'O jogador {n} fez {g} gol(s).'


name = input('Nome do jogador: ')
gol = input('Número de gols: ')
print(ficha(name, gol))
