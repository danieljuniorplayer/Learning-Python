matriz=[[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite um número para {[l,c]}: ')))
somaPares=somaImpares=0
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]} ]',end='')

    print()

