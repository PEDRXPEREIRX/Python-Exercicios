#Código criado com o ChatGPT!!!

def menu():
    print('-'*40)
    print('MENU PRINCIPAL'.center(40))
    print('-'*40)
    print('1 - Cadastrar nova pessoa')
    print('2 - Listas pessoas cadastradas')
    print('3 - Deletar uma pessoa cadastrada')
    print('0 - Sair')
    print('-'*40)


def cadastrar_pessoa():
    nome = input('Nome: ').strip().title()

    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            print('\033[1;32mPor favor, digite uma idade válida.\033m')

    nova_linha = f'{nome};{idade}'

    try:
        with open('pessoas.txt', 'r', encoding='utf-8') as arquivo:
            linhas = [linha.strip() for linha in arquivo.readlines()]
    except FileNotFoundError:
        linhas = []

    if nova_linha in linhas:
        print(f'\033[1;33m[!] {nome} com {idade} anos já está cadastrado.\033[m')
    else:
        with open('pessoas.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(nova_linha + '\n')
        print(f'\033[1;32mPessoa {nome} cadastrada com sucesso!\033[m')


def listar_pessoas():
    print('-'*40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-'*40)
    try:
        with open('pessoas.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print('Nenhuma pessoa cadastrada.')
            else:
                print(f'{"NOME":<30}{"IDADE":>8}')
                print('-'*40)
                for linha in linhas:
                    partes = linha.strip().split(';')
                    if len(partes) == 2:
                        nome, idade = partes
                        print(f'{nome:<30}{idade:>8} anos')
                    else:
                        print(f'Linha ignorada por estar mal formatada.')
    except FileNotFoundError:
        print('\033[1;33mNenhum cadastro encontrado. Cadastre alguém primeiro.\033[m')


def deletar_pessoa():
    try:
        with open('pessoas.txt', 'r', encoding='utf-8') as arquivo:
            linhas = [linha.strip() for linha in arquivo.readlines() if linha.strip()]
    except FileNotFoundError:
        print('\033[33mNenhum cadastro encontrado para deletar.\033[m')
        return

    if not linhas:
        print('\033[33mNenhuma pessoa cadastrada.\033[m')
        return

    print('-' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-' * 40)
    for i, linha in enumerate(linhas, start=1):
        nome, idade = linha.split(';')
        print(f'{i} - {nome:<30} {idade} anos')

    try:
        escolha = int(input('\nDigite o número da pessoa a deletar (0 para cancelar): '))
        if escolha == 0:
            print('\033[34mOperação cancelada.\033[m')
            return
        if 1 <= escolha <= len(linhas):
            removida = linhas.pop(escolha - 1)
            with open('pessoas.txt', 'w', encoding='utf-8') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')
            nome, idade = removida.split(';')
            print(f'\033[32mPessoa {nome} removida com sucesso!\033[m')
        else:
            print('\033[31mNúmero inválido.\033[m')
    except ValueError:
        print('\033[31mEntrada inválida. Digite um número válido.\033[m')


def main():
    while True:
        menu()
        opcao = input('Sua opção: ').strip()
        match opcao:
            case '1':
                cadastrar_pessoa()
            case '2':
                listar_pessoas()
            case '3':
                deletar_pessoa()
            case '0':
                print('\033[1;34mSaindo do sistema... Até logo!\033[m')
                break
            case _:
                print('\033[1;31mOpção inválida! Tente novamente.\033[m')


if __name__ == '__main__':
    main()
