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
