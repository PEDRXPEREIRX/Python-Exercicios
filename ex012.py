produto = int(input('Preço do produto? '))
descontoProduto = produto - (produto * 0.05)

print(f'O preço atual do produto é R${produto:.2f} e o valor com desconto fica R${descontoProduto:.2F}!')