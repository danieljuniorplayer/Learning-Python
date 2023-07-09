tupla=pares=()
for c in range(0,4):
    valores=int(input('Digite um valor: '))
    tupla+=(valores, )
    if valores%2 ==0:
        pares+=(valores,)
print(f'Total: {tupla}')
print(f'O número nove apareceu: {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeirto valor 3, está na posição: {tupla.index(3)+1}')
else:
    print('O valor 3 não foi digitado!')
print(f'Os valores pares são: {pares}')
