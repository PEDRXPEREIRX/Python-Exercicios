pessoas = []
dados = []
maiorPesoNome = []
menorPesoNome = []

dados.append(input('Informe seu nome: '))
peso = int(input('Informe seu peso: '))
dados.append(peso)
pessoas.append(dados[:])

maiorPesoKg = menorPesoKg = peso
maiorPesoNome.append(dados[0])
menorPesoNome.append(dados[0])

dados.clear()

while True:
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
    dados.append(input('Informe seu nome: '))
    peso = int(input('Informe seu peso: '))
    dados.append(peso)
    pessoas.append(dados[:])

    if peso == maiorPesoKg:
        maiorPesoNome.append(dados[0])
    elif peso > maiorPesoKg:
        maiorPesoNome.clear()
        maiorPesoKg = peso
        maiorPesoNome.append(dados[0])

    if peso == menorPesoKg:
        menorPesoNome.append(dados[0])
    elif peso < menorPesoKg:
        menorPesoNome.clear()
        menorPesoKg = peso
        menorPesoNome.append(dados[0])

    dados.clear()

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
if maiorPesoKg == menorPesoKg:
    print(f'Ambos tem o mesmo peso ({maiorPesoKg:.1f}Kg), peso de {maiorPesoNome}')
else:
    print(f'O maior peso foi de {maiorPesoKg:.1f}Kg. Peso de {maiorPesoNome}')
    print(f'O menor peso foi de {menorPesoKg:.1f}Kg. Peso de {menorPesoNome}')

#Resolução do Curso em Vídeo - Gustavo Guanabara
# pessoas = []
# dados = []
# maiorKg = menorKg = 0
#
# while True:
#     dados.append(input('Nome: '))
#     dados.append(float(input('Peso: ')))
#     if len(pessoas) == 0:
#         maiorKg = menorKg = dados[1]
#     else:
#         if dados[1] > maiorKg:
#             maiorKg = dados[1]
#         if dados[1] < menorKg:
#             menorKg = dados[1]
#     pessoas.append(dados[:])
#     dados.clear()
#     continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
#     if continuar in 'N':
#         break
#
# print()
# print(f'O maior peso foi de {maiorKg:.1f}Kg.', end=' ')
# for i in pessoas:
#     if i[1] == maiorKg:
#         print(f'"{i[0]}"', end=' ')
# print(f'\nO menor peso foi de {menorKg:.1f}Kg.', end=' ')
# for i in pessoas:
#     if i[1] == menorKg:
#         print(f'"{i[0]}"', end=' ')
