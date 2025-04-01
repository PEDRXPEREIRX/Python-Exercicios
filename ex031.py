print('----------- RODOVIÁRIA VAI E VOLTA -----------')
distancia = int(input('Qual a distância da sua viagem em Km? '))


if distancia <= 200:
    distancia *=  0.5
    print(f'O valor da sua passagem ficou o total de R$ {distancia:.2f}!')
else:
    distancia *= 0.45
    print(f'O valor da sua passagem ficou o total de R$ {distancia:.2f}!')

