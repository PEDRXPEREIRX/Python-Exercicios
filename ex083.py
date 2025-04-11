expr = input('Digite a expressão: ')
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(1)
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está incorreta!')
