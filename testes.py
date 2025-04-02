



#aula012
#
# nome = input('Informe seu nome: ').strip().lower()
#
# ESSA PARTE DAQUI EU IMPLEMENTEI COM A AJUDA DO CHATGPT PARA FAZER AS EXCECOES DOS
# NOMES "DAS", "DOS" ... (SE CHAMA LIST COMPREHENSION) EU AINDA NAO CONHECIA MAS JA VOU
# ANOTAR PARA ESTUDAR
#
# excecoes = {"das", "dos", "de", "da", "do", "e"}
#
# nomeFormatado = " ".join(
#     palavra if palavra in excecoes else palavra.capitalize()
#     for palavra in nome.split()
# )
#
# ATE AQUI
#
# if nomeFormatado.lower() == 'pedro':
#     print(f'{nomeFormatado}, que nome bonito :)')
# elif nomeFormatado.lower() == 'luno':
#     print(f'{nomeFormatado}, nome de gato safado!!!')
# elif nomeFormatado.lower() == 'duke':
#     print(f"{nomeFormatado}, nome de cachorro mijão '-'")
# else:
#     print(f'{nomeFormatado}, seja bem-vindo :)')
#
#fimAula012


# nome = 'Pedro'
# cores = {'limpa':'\033[m',
#          'azul':'\033[1;34m',
#          'amarelo':'\033[1;33m',
#          'pretobranco':'\033[7;40m'}
# print(f'Olá! Muito prazer em te conhecer, {cores['pretobranco']} {nome} {cores['limpa']}!!!')
#
# a = 3
# b = 5
# print(f'Os valores são \033[1;36m  {a}  \033[m e \033[1;31m  {b}  \033[m!')
#
# print('\033[1;30;47mOlá, Mundo!\033[m')




# from math import ceil, floor
#
# nota1 = float(input('Digite sua primeira nota: '))
# nota2 = float(input('Digite sua segunda nota: '))
# nota3 = float(input('Digite sua terceira nota: '))
#
# media = (nota1 + nota2 + nota3) / 3
#
# if (media < 7) & (media % 1 >= 0.5):
#     media = ceil(media)
#
# if media >= 7:
#     print(f'Congratulations hermano!!! Aprovado! Nota: {media:.1f}')
# else:
#     print(f'Melhore! Reprovado! Nota: {media:.1f}')



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