nomeCidade = input('Digite o nome de uma cidade: ')

print(f'Essa cidade começa com o nome Santo? {nomeCidade.split()[0].upper().strip() == 'SANTO'}')