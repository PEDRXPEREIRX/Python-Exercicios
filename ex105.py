def notas(entrada):
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
