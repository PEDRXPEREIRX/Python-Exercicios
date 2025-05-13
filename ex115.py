#Código criado com o ChatGPT!!!
#
# from uteis.utilidadesCeV import ex115
#
# ex115.main()

#Código Guanabara

from uteis.utilidadesCeV.ex115.lib.interface import *
from uteis.utilidadesCeV.ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Cadastros', 'Cadastrar', 'Sair do Sistema'])
    match resposta:
        case 1:
            lerArquivo(arq)
        case 2:
            cabecalho('Opção 2')
        case 3:
            cabecalho('Saindo do sistema ... Até logo')
            sleep(1)
            break
        case _:
            print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(1)




