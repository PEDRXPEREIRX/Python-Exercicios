jogadores = []
while True:
    gol = []
    soma = 0
    nome = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    for i in range(partidas):
        gols = int(input(f'Quantos gols na {i+1}ª partida? '))
        gol.append(gols)
        soma += gols
    jogador = {'nome': nome, 'gols': gol[:], 'total': soma}
    jogadores.append(jogador)
    gol.clear()
    soma = 0
    stop = input('Continuar cadastro? [S/N] ').upper().strip()[0]
    if stop == 'N':
        break

print(f'\n{'Cód.':<7}{'Nome':<10}{'Gols':^7}{'Total':^10}')
for i in range(len(jogadores)):
    print(f'{i+1:<7}{jogadores[i]['nome']:<10}{str(jogadores[i]['gols']):^7}{jogadores[i]['total']:^10}')

while True:
    stop = int(input('\nMostrar dados de qual jogador? [999 encerra] \n'
                     'Informe seu respectivo número! \n'))
    if stop == 999:
        break
    print(f'--- LEVANTANDO DADOS DO JOGADOR "{jogadores[stop-1]['nome']}" ---')
    for i, j in enumerate(jogadores[stop-1]['gols']):
        print(f'    No jogo {i+1} fez {j} gols')
