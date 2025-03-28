from math import radians, sin, tan, cos

angulo_graus = int(input('Digite o valor do ângulo: '))

angulo_radianos = radians(angulo_graus)

seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

print(f'Ângulo {angulo_graus}\n'
      f'Seno: {seno:.2f}\n'
      f'Cosseno: {cosseno:.2f}\n'
      f'Tangente: {tangente:.2f}')
