num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
soma = num1 + num2
mult = num1 * num2
div = num1 / num2
divint = num1 // num2
exp = num1 ** num2

print(f'A soma é {soma}, o produto é {mult} e a divisão é {div:.3f}!', end=' ')
print(f'A divisão inteira é {divint} e a potência é {exp}!')