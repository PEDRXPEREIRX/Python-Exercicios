#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
# - a vista dinheiro ou cheque: 10% desconto / a vista cartao: 5% desconto / em 2x cartao: preco normal /
# 3x ou mais cartao: juros 20%

preco = float(input('\033[1;35mInforme o valor do produto: \033[m'))

print('\033[1;35mComo deseja realizar o pagamento?\033[m\n\n'
      '\033[1;33m[1]\033[m \033[1;32mÀ vista - dinheiro / cheque (10% de desconto)\033[m\n'
      '\033[1;33m[2]\033[m \033[1;32mÀ vista - cartão (05% de desconto)\033[m\n'
      '\033[1;33m[3]\033[m \033[1;32mParcelado em 2x (valor normal)\033[m\n'
      '\033[1;33m[4]\033[m \033[1;32mParcelado em 3x ou mais (acréscimo de 20% em juros)\033[m\n')
escolha = int(input('Digite sua opçao: '))

if escolha == 1:
    valorTotal = preco - (preco * 0.1)
    print(f'O preço do produto é {preco:.2f} e o valor total conforme forma de pagamento ficou em R$ {valorTotal:.2f}')
elif escolha == 2:
    valorTotal = preco - (preco * 0.05)
    print(f'O preço do produto é {preco:.2f} e o valor total conforme forma de pagamento ficou em R$ {valorTotal:.2f}')
elif escolha == 3:
    parcela = preco / 2
    print(f'O preço do produto ficou em R$ {preco:.2f} parcelado em 2x de R$ {parcela:.2f}')
elif escolha == 4:
    valorTotal = preco * 1.2
    numParcelas = int(input('Em quantas vezes deseja parcelar? (mínimo 03 parcelas) '))
    if numParcelas < 3:
        print(f'O número mínimo de parcelas é 03!')
    else:
        parcela = valorTotal / numParcelas
        print(f'O preço do produco é R$ {preco:.2f} e o valor total conforme forma de pagamento ficou em R$ {valorTotal:.2f} parcelado em {numParcelas}x de R$ {parcela:.2f}')
else:
    print('Opção inválida!')