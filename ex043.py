altura = float(input('Informe sua altura em centímetros (cm): '))
altura /= 100
altura **= 2
peso = float(input('Inform seu peso em kilogramas (kg): '))
imc = peso / altura

if imc < 18.5:
    print(f'Resultado IMC: {imc:.2f} - Abaixo do peso')
elif imc <= 25:
    print(f'Resultado IMC: {imc:.2f} - Peso ideal')
elif imc <= 30:
    print(f'Resultado IMC: {imc:.2f} - Sobrepeso')
elif imc <= 40:
    print(f'Resultado IMC: {imc:.2f} - Obesidade')
else:
    print(f'Resultado IMC: {imc:.2f} - Obesidade mórbida')
