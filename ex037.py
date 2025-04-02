#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# [1] para binário [2] para octal [3] para hexadecimal

numero = int(input('Informe um número: '))
binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:].upper()

conversor = int(input('Escolha qual a \033[1;34mbase de conversão\033[m:\n'
      '\033[1;34m[1]\033[m para \033[1;33mbinário\033[m\n'
      '\033[1;34m[2]\033[m para \033[1;33moctal\033[m\n'
      '\033[1;34m[3]\033[m para \033[1;33mhexadecimal\033[m\n'
                      ''))

if conversor == 1:
    print(f'O número informado foi \033[1;34m{numero}\033[m e a base de conversão escolhida foi binária.\n'
          f'Resultado do número \033[1;34m{numero}\033[m em decimal para binário é \033[1;33m{binario}\033[m')
elif conversor == 2:
    print(f'O número informado foi \033[1;34m{numero}\033[m e a base de conversão escolhida foi octal.\n'
          f'Resultado do número \033[1;34m{numero}\033[m em decimal para octal é \033[1;33m{octal}\033[m')
elif conversor == 3:
    print(f'O número informado foi \033[1;34m{numero}\033[m e a base de conversão escolhida foi hexadecimal.\n'
          f'Resultado do número \033[1;34m{numero}\033[m em decimal para hexadecimal é \033[1;33m{hexadecimal}\033[m')
else:
    print('Opção inválida!')

