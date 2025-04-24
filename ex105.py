def notas(entrada):
    """
    :param entrada: recebe os valores das notas em uma lista
    :return: retorna o boletim contendo a quantidade de notas, a maior e menor nota, média e situação aprovado/reprovado
    """
    boletim = {'quantidade': len(entrada), 'maior': 0, 'menor': 0, 'media': 0}
    soma = 0
    for i in entrada:
        soma += i
        if boletim['menor'] == 0:
            boletim['menor'] = i
        elif i < boletim['menor']:
            boletim['menor'] = i
        if boletim['maior'] == 0:
            boletim['maior'] = i
        elif i > boletim['maior']:
            boletim['maior'] = i
    media = soma / len(entrada)
    boletim['media'] = round(media, 1)
    if media >= 7:
        boletim['situação'] = 'aprovado'
    else:
        boletim['situação'] = 'reprovado'
    return boletim


nota = notas([7, 8.8, 6.9, 8, 5.8])
print(nota)

#Código Guanabara
# def notas(*n, sit=False):
#     """
#     -> Função para analisar notas e situações de vários alunos.
#     :param n: nota(s) dos alunos
#     :param sit: valor opcional, indicando se deve ou não adicionar a situalção
#     :return: dicionário com várias informações sobre as notas
#     """
#     r = {}
#     r['total'] = len(n)
#     r['maior'] = max(n)
#     r['menor'] = min(n)
#     r['media'] = round(sum(n) / len(n), 1)
#     if sit:
#         if r['media'] >= 7:
#             r['situação'] = 'BOA'
#         elif r['media'] >= 5:
#             r['situação'] = 'RAZOÁVEL'
#         else:
#             r['situação'] = 'RUIM'
#     return r
#
#
# resp = notas(5.8,2.5,1.5, sit=True)
# print(resp)
# help(notas)
