#Refaca o ex009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laco for
#Obs: no ex009 eu ja utilizei um laco for

tabuada = int(input('Qual valor deseja multiplicar?'))

for i in range(1, 11):
    print(f'{tabuada} X {i} = {i * tabuada}')