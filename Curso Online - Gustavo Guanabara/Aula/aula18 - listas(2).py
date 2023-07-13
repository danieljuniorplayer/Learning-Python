teste=[]
teste.append('gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0]='daniel'
teste[1]= 23
galera.append(teste[:])
print(galera)

pessoas= [['joao',12],['paulo',23]]
print(pessoas)
for p in pessoas:
    print(p[0])
dados=[]
galera=[]
for d in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    dados.append(str(input('Sexo: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
print(dados)

for g in galera:
    if g[1] >=18:
        print(g[0])