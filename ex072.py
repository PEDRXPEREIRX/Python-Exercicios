numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: (999 para sair) '))
    if num == 999:
        break
    while num not in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20):
        num = int(input('Tente Novamente! \nDigite um número entre 0 e 20: (999 para sair) '))
    print(numeros[num])
