salario = float(input('Para realizarmos um aumento salárial, precisamos que informe o valor do seu salário atual: '))

if salario > 1250:
    print(f'Seu salário atual é R$ {salario:.2f} e com o novo aumento ficará R$ {salario * 1.10:.2f}')

elif salario <= 1250:
    print(f'Seu salário atual é R$ {salario:.2f} e com o novo aumento ficará R$ {salario * 1.15:.2f}')