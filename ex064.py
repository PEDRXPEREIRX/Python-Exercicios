num = soma = total = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
        total += 1

if total == 0:
    print('Nenhum número digitado.')
elif total == 1:
    print(f'Você digitou um único número com valor {soma}.')
else:
    print(f'Você digitou {total} números e a soma entre eles foi {soma}.')