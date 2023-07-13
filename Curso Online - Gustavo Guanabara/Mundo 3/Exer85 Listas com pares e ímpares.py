numeros=[[],[]]
for n in range(0,7):
    a = int(input(f'Digite o {n+1} valor: '))
    numeros[0].append(a) if a % 2==0 else numeros[1].append(a)
print(f'Os valores pares foram: {sorted(numeros[0])}')
print(f'Os valores ímpares foram: {sorted(numeros[1])}')
