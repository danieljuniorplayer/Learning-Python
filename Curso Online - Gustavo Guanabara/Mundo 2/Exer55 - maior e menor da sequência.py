# modo guanabara
maior = 0
menor = 0
for p in range(0, 5):
    peso = float(input(f'Digite o peso da {p + 1}ª pessoa:'))
    if p == 0:
        maior = peso
        menor = peso
    else:

        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(maior)
print(menor)

# meu modo
lista = []
for c in range(0,5):
    peso = float(input(f'Digite o peso da {c+1}ª pessoa:'))
    lista.append(peso)              # pega o peso e vai salvando na lista
lista= sorted(lista, key=float)       # ordena a lista do menor para o maior
print(lista)
print(lista[0])                     # pega o primeiro valor da lista
print(lista[len(lista)-1])          # pega o último valor da lista

#mais compacto
lst=[]  # lista vazia
for c in range(1, 6):
    peso=float(input('Peso da {}ª pessoa: '.format(c)))
    lst+=[peso]   # adc os valores de peso na lista
print('O Maior peso foi:', max(lst))  # maximo valor da lista
print('O Menor peso foi:', min(lst))  # minimo valor da lista
print('')

# mais simplificado ainda
pesos = [float(input(f'Peso da {a}º pessoa: ')) for a in range(1, 6)]
print(f'O maior peso foi de {max(pesos)}Kg\nO menor foi de {min(pesos)}Kg!')