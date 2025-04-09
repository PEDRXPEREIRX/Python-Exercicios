soma = total = 0
while True:
    num = int(input('Digite um número [999 para sair]: '))
    if num == 999:
        break
    else:
        soma += num
        total += 1

if total == 0:
    print('Nenhum número digitado.')
elif total == 1:
    print(f'O único número digitado foi {soma}')
else:
    print(f'Total de números digitados: {total}\n'
        f'Soma dos números: {soma}')
