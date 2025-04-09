while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 10)
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    print('-' * 10)

print('\nFIM')