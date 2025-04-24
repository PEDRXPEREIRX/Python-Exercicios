def ficha(nome='', gols=''):
    if nome == '':
        n = '<desconhecido>'
    else:
        n = nome
    if gols == '':
        g = '0'
    else:
        g = int(gols)

    return f'O jogador {n} fez {g} gol(s).'


name = input('Nome do jogador: ')
gol = input('Número de gols: ')
print(ficha(name, gol))
