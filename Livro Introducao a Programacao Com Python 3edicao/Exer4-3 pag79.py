#Exercício 4.3 Escreva um programa que leia três números e que imprima o maior e o menor.(primeira versão)
a1 = float(input('Digite o primeiro valor'))
a2 = float(input('Digite o segundo valor'))
a3 = float(input('Digite o terceiro valor'))
if a1 > a2 and a1 > a3:
    print(f'O maior valor é {a1}, ', end='')
    if a2 < a3:
        print(f'o menor valor é {a2}')
    else:
        print(f'o menor valor é {a3}')
elif a2 > a1 and a2 > a3:
    print(f'O maior valor é {a2}, ', end='')
    if a3 < a1:
        print(f'O menor valor é {a3}')
    else:
        print(f'O menor valor é {a1}')
else:
    print(f'O maior valor é {a3}, ',end='')
    if a2 < a1:
        print(f'o menor valor é {a2}')
    else:
        print(f'o menor valor é {a1}')