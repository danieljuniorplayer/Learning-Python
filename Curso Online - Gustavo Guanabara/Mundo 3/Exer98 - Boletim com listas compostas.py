aluno=[[],[],[]]
cont=0
while True:
    print(f'=======Dados do {cont+1}° aluno=========')
    aluno[0].append(str(input('Digite o nome do aluno: ').strip().upper()))
    aluno[1].append(float(input('Digite a primeira nota: ')))
    aluno[2].append(float(input('Digite a segunda nota:')))


    op=str(input('Quer continuar? [S/N]: ')).strip().upper()
    if op=='N':
        break
    cont+=1
print('  ','_'*32)
print(f'Nº|_____________NOME_______________| Média')
for k in range(0,cont+1):
    print(f'{k} | {aluno[0][k]:^30} | {(aluno[1][k]+aluno[2][k])/2}')

while True:
    mostrar=int(input('Mostrar notas de qual aluno? (999-Sair): '))
    if mostrar ==999:
        break
    print(aluno[1][mostrar], aluno[2][mostrar])















'''
aluno=[[[],[]],]
print(aluno)
cont=0
while True:
    aluno[cont][0].append(str(input('Digite o nome do aluno: ').strip().upper()))
    aluno[cont][1].append(float(input('Digite a primeira nota: ')))
    aluno[cont][1].append(float(input('Digite a segunda nota:')))
    op=str(input('Quer continuar? [S/N]: ')).strip().upper()
    if op=='N':
        break
    cont+=1

print(aluno)
print(aluno[0][1][1])'''