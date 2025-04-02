#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
#da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calce o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorImovel = float(input('Informe o valor do imóvel: ').strip())
salario = float(input('Informe o seu salário bruto: ').strip())
meses = int(input('Informe em quantos anos deseja quitar o empréstimo: ').strip())
meses *= 12
prestacao = valorImovel / meses

if prestacao > (salario * 0.3):
    print(f'O valor excede 30% do seu salário (R$ {prestacao:.2f}), portanto, empréstimo negado!')
else:
    print(f'Parabéns, empréstimo aprovado! Valor da prestação mensal ficou em R$ {prestacao:.2f} e será pago em {meses} meses!')