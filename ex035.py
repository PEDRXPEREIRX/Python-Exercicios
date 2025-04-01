ladoA = int(input('Comprimento da reta A: '))
ladoB = int(input('Comprimento da reta B: '))
ladoC = int(input('Comprimento da reta C: '))

if ((ladoA + ladoB) > ladoC ) and ((ladoA + ladoC) > ladoB) and ((ladoB + ladoC) > ladoA):
    print('As três retas podem formar um triângulo!')
else:
    print('As três retas não são capazes de formar um triângulo!')