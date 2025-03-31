frase = input('Digite uma frase: ').lower()

print(f'Quantas vezes aparece a letra "A": {frase.count('a')}')
print(f'Em que posição ela aparece a primeira vez: {frase.find('a')}')
print(f'Em que posição ela aparece pela última vez: {frase.rfind('a')}')