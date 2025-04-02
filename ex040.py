from math import ceil

notaA = float(input('Digite a nota da prova A: '))
notaB = float(input('Digite a nota da prova B: '))
media = (notaA + notaB) / 2

if (media < 7) and (media >= 5) and (media % 1 >= 0.5):
    media = ceil(media)

if media < 5:
    print(f'Reprovado! Valor da sua média {media:.1f}')
elif media <= 6.9:
    print(f'Recuperação! Valor da sua média {media:.1f}')
else:
    print(f'Aprovado! Valor da sua média {media:.1f}')