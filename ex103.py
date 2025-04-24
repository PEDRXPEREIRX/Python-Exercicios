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



#Código Guanabara
# def ficha(jog='<desconhecido>', gol=0):
#     print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')
#
#
# n = input('Nome do jogador: ')
# g = input('Número de gols: ')
# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0
# if n.strip() == '':
#     ficha(gol=g)
# else:
#     ficha(n, g)
#