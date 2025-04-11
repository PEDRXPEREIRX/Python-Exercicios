#Fiz de dois jeitos, um do jeito que o Guanabara deu no exemplo da proposta do exercício
#e outro da forma que pensei primeiro

valores = []
for i in range(10):
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor já digitado!', end=' ')
        continue
    valores.append(valor)

valores.sort()
print('Os valores digitados em ordem crescente foram', *valores)

# valores = []
# resp = 'S'
# while True:
#     valor = int(input('Digite um valor: '))
#     if valor not in valores:
#         valores.append(valor)
#     resp = input('Quer continuar? [S/N] ').upper().strip()[0]
#     while resp not in 'SsNn':
#         resp = input('Quer continuar? [S/N] ').upper().strip()[0]
#     if resp == 'N':
#         break
#
# valores.sort()
# print('Os valores digitados em ordem crescente foram', *valores)
