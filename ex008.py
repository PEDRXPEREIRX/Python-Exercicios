valor = int(input('Digite um valor em metros: '))

centimetros = valor * 100
milimetros = valor * 1000
decimetros = valor * 10
decametros = valor * 0.1
hectometros = valor * 0.01
kilometros = valor * 0.001

print(f'{valor:.1f} metros\n'
      f'{centimetros:.1f} centimetros\n'
      f'{milimetros:.1f} milimetros\n'
      f'{decimetros:.1f} decimetros\n'
      f'{decametros:.1f} decametros\n'
      f'{hectometros:.1f} hectometros\n'
      f'{kilometros:.1f} kilometros')
