from math import ceil, floor

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if (media < 7) & (media % 1 >= 0.5):
    media = ceil(media)

if media >= 7:
    print(f'Congratulations hermano!!! Aprovado! Nota: {media:.1f}')
else:
    print(f'Melhore! Reprovado! Nota: {media:.1f}')


# frase = 'Curso em Vídeo Python'
#
# print(frase[:14])
# print(frase[15:])
# print(frase[9::2])
# print(len(frase))
# print(frase.count('o', 0, 13))
# print(frase.find('thon'))
# print(frase.find('Android'))
# print('Curso' in frase)
# print(frase.replace('Python', 'Android'))
# print(frase.upper())
# print(frase.lower())
# print(frase.capitalize())
# print(frase.title())
#
# frase = '   Aprenda Python  '
#
# print(frase.strip())
# print(frase.rstrip())
# print(frase.lstrip())
#
# frase = 'Curso em Vídeo Python'
# print(frase.split())
#
# print(''.join(frase))
#
#
# print("""AAAAAAAAAAAAAAAAAAAAAAAAAAA
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# AAAAAAAAAAAAAAAAAAAAAAAAA""")
#
# print(frase.lower().find('vídeo'))
#
# dividido = frase.split()
# print(dividido[:3])