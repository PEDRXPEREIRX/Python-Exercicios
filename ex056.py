#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostra:
#A média de idade do grupo, qual é o nome do homem mais velho, quantas mulheres tem menos de 20 anos

pessoas = []
somaIdade = 0
mulheresSub20 = 0
homemVelho = {"nome": "", "idade": 0}

for i in range(4):
    print(f'Pessoa {i+1}:')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo: [MASC ou FEM] ').strip().lower()

    pessoa = {"nome": nome, "idade": idade, "sexo": sexo}
    pessoas.append(pessoa)

    somaIdade += idade

    if sexo == "masc" and idade > homemVelho["idade"]:
        homemVelho["nome"] = nome
        homemVelho["idade"] = idade

    if sexo == "fem" and idade < 20:
        mulheresSub20 += 1

mediaIdade = somaIdade / 4

print(f'Resultados da pesquisa:\n'
      f'\nA média de idade do grupo é {mediaIdade:.1f} anos.')

if homemVelho:
    print(f'O homem mais velho se chama {homemVelho["nome"]} com {homemVelho["idade"]} anos.')
else:
    print('Não há homens no grupo.')

if mulheresSub20:
    print(f'Há {mulheresSub20} mulheres com menos de 20 anos no grupo.')
else:
    print('Não há mulheres com menos de 20 anos no grupo.')
