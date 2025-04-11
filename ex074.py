from random import choices

num = tuple(choices(range(0,10), k=5))

print('Os valores sorteados foram:', *num)
print(f'O maior valor sorteado foi: {max(num)}')
print(f'O menor valor sorteado foi: {min(num)}')

