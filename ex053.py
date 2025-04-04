#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo
#Ex.: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA

frase = input('Digite uma frase: ')
fraseFormatada = frase.lower().replace(' ', '')

parametro = fraseFormatada[::-1]
if fraseFormatada == parametro:
    print(f'A frase "{frase}" é um palíndromo')
else:
    print(f'A frase "{frase}" não é um palíndromo')
