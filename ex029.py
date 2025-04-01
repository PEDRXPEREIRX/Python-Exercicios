velocidade = int(input('Qual a velocidade que o carro passou no radar? '))

if velocidade > 80:
    print(f'Velocidade máxima da via permitida é 80Km/h! Você foi multado estando em {velocidade} Km/h :(')
    multa = (velocidade - 80) * 7
    print(f'O valor da multa é R$ 7,00 por cada Km acima da velocidade permitida, ficando o total de R$ {multa},00')
else:
    print(f'Sua velocidade era de {velocidade} Km/h em uma via com limite de 80 Km/h! Você NÃO foi multado, parabéns :)')