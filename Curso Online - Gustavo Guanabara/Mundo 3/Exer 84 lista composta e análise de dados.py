dados_pessoas= list()
pessoas=[]
pessoaMaisPesada=[]
pessoaMaisLeve=[]
cont=maximo=minimo=0
while True:
    dados_pessoas.append(str(input('Nome: ')))
    dados_pessoas.append(float(input('Peso: ')))
    pessoas.append(dados_pessoas[:])
    dados_pessoas.clear()
    if cont == 0 or pessoas[cont][1] > maximo:
        maximo=pessoas[cont][1]
    if cont == 0 or pessoas[cont][1] < minimo:
        minimo=pessoas[cont][1]
    op= int(input('[1] Continuar | [0] Sair:'))
    if op==0:
        break
    cont+=1
print(f'Foram cadastradas: {cont+1} pessoas.')
print(f'Pessoas mais pesadas: ',end='')
for k,p in enumerate(pessoas):
    if p[1] == maximo:
        print(pessoas[k][:],end='')
print(f'\nPessoas mais leves: ',end='')
for k,p in enumerate(pessoas):
    if p[1] == minimo:
        print(pessoas[k][:],end='')
