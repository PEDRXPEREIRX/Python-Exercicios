nome = input('Digite seu nome completo: ')

print(f'Primeiro nome: {nome.split()[0].strip()}')
print(f'Último nome: {nome.split()[-1].strip()}')