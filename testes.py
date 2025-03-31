frase = 'Curso em Vídeo Python'

print(frase[:14])
print(frase[15:])
print(frase[9::2])
print(len(frase))
print(frase.count('o', 0, 13))
print(frase.find('thon'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase = '   Aprenda Python  '

print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

frase = 'Curso em Vídeo Python'
print(frase.split())

print(''.join(frase))


print("""AAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAA""")

print(frase.lower().find('vídeo'))

dividido = frase.split()
print(dividido[:3])