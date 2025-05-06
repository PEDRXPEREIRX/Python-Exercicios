def leiaDinheiro(msg):
    while True:
        entrada = input(msg)
        try:
            return float(entrada.replace(",", "."))
        except ValueError:
            print(f'\033[1;31mERRO: "{entrada}" é um valor inválido!\033[m')
