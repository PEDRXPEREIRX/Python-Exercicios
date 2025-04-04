#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostra:
#A média de idade do grupo, qual é o nome do homem mais velho, quantas mulheres tem menos de 20 anos

people = []
addAge = 0
womanSub20 = 0
olderMan = {"nome": "", "idade": 0}

for i in range (4):
    name = input(f'\nIndivíduo número {i+1}, informe seu nome: ').strip()
    age = int(input('Agora informe a sua idade: '))
    gender = input('Por último, seu gênero: [MASC] ou [FEM] ').lower().strip()

    addAge += age

    person = {"nome": name, "idade": age, "genero": gender}
    people.append(person)

    if (gender == 'masc') and (age > olderMan["idade"]):
        olderMan["nome"] = name
        olderMan["idade"] = age

    if gender == 'fem' and age < 20:
        womanSub20 += 1

averageAge = addAge / len(people)

print(f'\nResultado da pesquisa:\n')
print(f'Total de participantes: {len(people)}\n')
print(f'Média de idade do grupo: {averageAge} anos.')

if olderMan["nome"]:
    print(f'O homem mais velho do grupo se chama {olderMan["nome"]}.')
else:
    print('Não há nenhum homem no grupo.')

if womanSub20:
    print(f'Total de mulheres com menos de 20 anos: {womanSub20}.')
else:
    print('Não há mulheres com menos de 20 anos no grupo.')
