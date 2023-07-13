op=1
valores=[]
while op !=0:
    valores.append(int(input('Digite um valor: ')))
    op=int(input('[1] Continuar | [0] Sair: '))
pares=[]
impares=[]
for k, v in enumerate(valores):
    if v%2==0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Valores digitados: {valores}')
print(f'Valores pares: {pares}')
print(f'Valores impares: {impares}')
