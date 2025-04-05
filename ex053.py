#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo
#Ex.: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA

frase = input('Digite uma frase: ')
fraseFormatada = frase.lower().replace(' ', '')
parametro = fraseFormatada[::-1]

print(f'A frase "{frase}" ao inverso é "{parametro.capitalize()}"')
if fraseFormatada == parametro:
    print(f'A frase "{frase}" é um palíndromo')
else:
    print(f'A frase "{frase}" não é um palíndromo')


# Código do Guanabara utilizando laço 'for'
# frase = input('Digite uma frase: ').strip()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
#
# for letra in range(len(junto) -1, -1, -1):
#     inverso += junto[letra]
#
# if inverso == junto:
#     print(f'Temos um palíndromo.')
# else:
#     print(f'A frase digitada não é um palíndromo.')
