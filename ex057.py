resp = input('Informe seu sexo: [M/F] ').upper().strip()

if resp == 'M' or resp == 'F':
    print(f'Sexo {resp} registrado com sucesso')
else:
    while resp != 'M' and resp != 'F':
        resp = input('Dados inválidos: Por favor, informe o seu sexo: [M/F] ').upper().strip()
        if resp == 'M' or resp == 'F':
            print(f'Sexo {resp} registrado com sucesso')
            break

#Pedi para o ChatGPT avaliar o código e ele me passou um código corrigido e mais limpo:
# resp = input('Informe seu sexo: [M/F] ').upper().strip()[0]
#
# while resp not in ['M', 'F']:
#     resp = input('Dados inválidos: Por favor, informe o seu sexo: [M/F] ').upper().strip()
#
# print(f'Sexo {resp} registrado com sucesso')