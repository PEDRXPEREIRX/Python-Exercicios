num = int(input('Digite um número: '))
menorValor = maiorValor = soma = num
total = 1
resp = 'S'

while True:
    resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
    elif resp == 'S':
        num = int(input('Digite outro número: '))
        soma += num
        total += 1
        if num > maiorValor:
            maiorValor = num
        if num < menorValor:
            menorValor = num

if total == 1:
    print(f'O único número digitado foi {num}')
elif menorValor == maiorValor:
    print(f'Você digitou {total} números e os valores são iguais ({menorValor})')
else:
    media = soma / total
    print(f'Você digitou {total} números e a média foi {media:.2f}')
    print(f'O menor valor digitado foi {menorValor} e o maior foi {maiorValor}')