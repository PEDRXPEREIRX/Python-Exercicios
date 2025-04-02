ladoA = int(input('Comprimento da reta A: '))
ladoB = int(input('Comprimento da reta B: '))
ladoC = int(input('Comprimento da reta C: '))

if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
    if (ladoA == ladoB) and (ladoB == ladoC):
        print(f'As três retas iguais formam um triângulo equilátero')
    elif (ladoA == ladoB) or (ladoB == ladoC) or (ladoA == ladoC):
        print(f'Com duas retas iguais e um diferente é formado um triângulo isósceles')
    else:
        print(f'Com todos os lados diferentes é formado um triângulo escaleno')
else:
    print(f'Não é possível formar um triângulo!')