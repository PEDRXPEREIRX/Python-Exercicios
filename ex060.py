num = int(input('Informe um número: '))
aux = num
fac = 1

# print(f'{num}! = ', end='')
# while aux > 0:
#     print(f'{aux}', end='')
#     fac *= aux
#     print(' x ' if aux > 1 else ' = ', end='')
#     aux -= 1
#
# print(fac)

print(f'{num}! = ', end='')
for aux in range(aux, 0, -1):
    print(f'{aux}', end='')
    print(' x ' if aux > 1 else ' = ', end='')
    fac *= aux

print(fac)

