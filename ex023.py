numero = int(input('Digite um valor de 0 à 9999: '))

unidade = (numero % 10)
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f'Unidades: {unidade}\n'
      f'Dezenas: {dezena}\n'
      f'Centenas: {centena}\n'
      f'Milhares: {milhar}')
