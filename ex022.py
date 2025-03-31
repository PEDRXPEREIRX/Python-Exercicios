nome = input('Digite seu nome completo: ')

print(f'Nome completo: {nome.strip()}')
print(f'Nome em letras maiúsculas: {nome.upper().strip()}')
print(f'Nome em letras minúsculas: {nome.lower().strip()}')
print(f'Quantidade de letras ao todo (sem considerar espaços): {len(nome.replace(' ', '').strip())}')
print(f'Quantidade de letras do primeiro nome: {len(nome.split()[0])}')