from random import randint
lista=()
op=int(input('Quantos números aleatórios vc quer gerar?: '))
for c in range(0,op):
    lista = lista + (randint(0,20), )  # randint numa tupla()

print(lista)

print(f'maior valor: {max(lista)}')
print(f'menor valor: {min(lista)}')
