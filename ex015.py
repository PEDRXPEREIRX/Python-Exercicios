totalDias = int(input('Quantos dias alugados? '))
kmRodados = float(input('Quantos Km rodados? '))
valor = (totalDias * 60) + (kmRodados * 0.15)

print(f'O total a pagar é R${valor:.2f}')