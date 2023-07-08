frase = str(input('Digite uma frase:')).strip().lower()
a = frase.count('a')
p = frase.find('a')
t = len(frase)
p2 = frase.rfind('a')

print(f'A letra "A" aparece {a} vezes na frase.')
print(f'A primeira letra "A" apareceu na {p+1}ª posição')
print(f'A última letra "A" apareceu na {p2+1}ª posição')