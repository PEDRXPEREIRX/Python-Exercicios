tabela = ('Internacional', 'Corinthians', 'Ceará', 'Fortaleza', 'Botafogo', 'Flamengo', 'Palmeiras', 'Juventude', 'Fluminense', 'Grêmio', 'Vasco', 'Cruzeiro', 'Bahia', 'São Paulo', 'Bragantino', 'Santos', 'Mirassol', 'Sport', 'Atlético-MG', 'Vítoria')

print(f'\nOs 05 primeiros colocados são: {tabela[:5]}')
print(f'Os últimos 04 colocados são: {tabela[-4:]}')
print(f'Lista de todos os times em ordem alfabética: \n{sorted(tabela)}')
print(f'O Internacional está na {tabela.index('Internacional')+1}ª posição!')
