from math import sqrt, hypot

catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

print(f'O comprimento da hipotenusa é {hipotenusa:.2f}!')

# catOposto = float(input('Digite o comprimento do cateto oposto: '))
# catAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
# hipotenusa = hypot(catOposto, catAdjacente)
#
# print(hipotenusa)