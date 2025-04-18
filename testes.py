jogador = {'a': 9, 'b': 4, 'c': 6}

print(sorted(jogador.items(), key=lambda x: x[1]))



#aula019
# filmes = {
#     'titulo': 'Star Wars',
#     'ano': 1977,
#     'diretor': 'George Lucas'
# }
#
# print(filmes.values()) #Mostra os valores. Ex.: Star Wars, 1977, George Lucas
# print(filmes.keys()) #Mostra as chaves. Ex.: titutlo, ano, diretor
# print(filmes.items()) #Mostra tanto as chaves quanto seus respectivos valores
#
# for k, v in filmes.items():
#      print(f'O {k} é {v}')
#
# locadora = []
# filme = {}
#
# for _ in range(3):
#     filme['titulo'] = input('Título do filme: ')
#     filme['ano'] = int(input('Ano do filme: '))
#     filme['diretor'] = input('Diretor do filme: ')
#     locadora.append(filme.copy())
#
# for i in range(len(locadora)):
#     print(locadora[i])
#     print()




#aula018
#
# teste = []
# teste.append('Pedro')
# teste.append(22)
# galera = []
# galera.append(teste[:])
# teste[0] = 'Luno'
# teste[1] = '5'
# galera.append(teste[:])
# print(galera)
#
# galera =[['Pedro', 22], ['Adriana', 25], ['Mel', 2], ['Lucca', 1]]
# for i in galera:
#     print(f'{i[0]} tem {i[1]} anos de idade.')
#
# galera = []
# dados = []
# totMai = totMen = 0
#
# for i in range(3):
#     dados.append(input('Informe seu nome: '))
#     dados.append(int(input('Informe sua idade: ')))
#     galera.append(dados[:])
#     dados.clear()
#
# for i in galera:
#     if i[1] >= 21:
#         print(f'{i[0]} é maior de idade.')
#         totMai += 1
#     else:
#         print(f'{i[0]} é menor de idade.')
#         totMen += 1
#
# print(f'Temos {totMai} pessoas maiores de idade.\n'
#       f'Temos {totMen} pessoas menores de idade.')




#aula017
# valores = [8,4,9,3,6,2,1,7,8]
# print(*valores)
# valores.sort()
# print(*valores)
# valores.sort(reverse=True)
# print(*valores)
#
# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# if 4 in num:
#     num.remove(2)
# print(num)
#
# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
#
# for cont, valor in enumerate(valores):
#     print(f'{valor} na posição {cont}')
#
# valores = []
#
# for cont in range(5):
#     valores.append(int(input('Digite um valor: ')))
#
# print(valores)
#
# a = [1,2,3,4]
# b = a
# b[2] = 8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')
#
# a = [1,2,3,4]
# b = a[:]
# b[2] = 8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')



#aula016
# pessoa = ('Pedro', 22, 'M', 90)
# del(pessoa)
# print(pessoa)

# numeros = (5, 1, 9, 24, 58, 3, 0)
# numerosOrdem = sorted(numeros)
# print(numeros)
# print(numerosOrdem)

# lanches = ('maçã', 'banana', 'sanduiche', 'suco')
#
# for pos, comida in enumerate(lanches):
#     print(f'Eu vou comer {comida} na posição {pos+1}')

# for comida in lanches:
#     print(f'Eu vou comer {comida}')

# for comida in range(0, len(lanches)):
#     print(f'Eu vou comer {lanches[comida]}')



#aula014
# resp = "SIM"
# par = 0
# impar = 0
#
# while resp != "NAO":
#     num = int(input('Informe um número: '))
#     if num % 2 == 0:
#         par += 1
#     else:
#         impar += 1
#     resp = input('Deseja continuar? [SIM / NAO] ').upper().strip()
#
# if par == 0 and impar == 0:
#     print('Não foi informado nenhum número :(')
# else:
#     print(f'Total de números pares digitados: {par}.\n'
#           f'Total de números ímpares digitados: {impar}.')




#aula013
# soma = 0
# for cont in range(0, 10):
#     num = int(input('Digite um valor: '))
#     soma += num
#
# print(f'A soma de todos números é {soma}!')




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