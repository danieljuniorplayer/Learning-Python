matriz=[[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite um número para {[l,c]}: ')))
somaPares=somacoluna3=maiorlinha2=0
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]} ]',end='')
        if matriz[l][c] %2 ==0:
            somaPares+=matriz[l][c]
        if c ==2:
            somacoluna3+=matriz[l][c]
        if l ==1:
            if matriz[l][c] > maiorlinha2:
                maiorlinha2=matriz[l][c]
    print()
print(f'A soma dos valores Pares: {somaPares}')
print(f'Soma dos valores da 3ª coluna: {somacoluna3}')
print(f'O maior valor da segunda linha: {maiorlinha2}')

