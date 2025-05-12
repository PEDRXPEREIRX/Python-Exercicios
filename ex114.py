import requests, webbrowser

def verificar_site(url):
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            print(f'\033[1;32m[OK] O site {url} está acessível.\033[m')
            webbrowser.open(url)
        else:
            print(f'\033[1;33m[ALERTA] O site respondeu com status {resposta.status_code}\033[m')
    except requests.RequestException:
        print(f'\033[1;31m[ERRO] Não foi possível acessar o site {url}.\033[m')


verificar_site('https://www.pudim.com.br')

#Código Guanabara
# import urllib, urllib.request
# try:
#     site = urllib.request.urlopen('https://www.pudim.com.br')
# except:
#     print('O site "Pudim" não está acessível no momento.')
