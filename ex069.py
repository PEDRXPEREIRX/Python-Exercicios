pessoas = []
mulher20 = maiores = homens = 0
continuar = 'S'
while True:
    idade = int(input('Informe sua idade: '))
    sexo = input('Informe seu sexo: [M/F] ').upper().strip()[0]
    pessoa = {"idade": idade, "sexo": sexo}
    pessoas.append(pessoa)
    if idade > 18:
        maiores += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    if sexo == 'M':
        homens += 1
    continuar = input('\nDeseja continuar? [S/N] ').upper().strip()[0]
    if continuar != 'S':
        break

print(f'Quantidade de pessoas maiores de 18 anos: {maiores}.\n'
      f'Quantidade de homens cadastrados: {homens}.\n'
      f'Quantidade de mulheres menores de 20 anos: {mulher20}.')
