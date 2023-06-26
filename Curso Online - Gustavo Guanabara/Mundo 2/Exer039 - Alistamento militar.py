from datetime import date
print('Qual sua data de nascimento?')
nasci = str(input('Escreva nesse formato dd/mm/aa:')).strip().split(sep='/')
hoje = str(date.today()).split(sep='-')[::-1]

dia = int(hoje[0])-int(nasci[0])
mes = int(hoje[1])-int(nasci[1])
ano = int(hoje[2])-int(nasci[2])

print(dia)
print(mes)
print(ano)
idade=[dia,mes,ano]
print(idade)


if mes<0:
    mes = mes*-1
    ano-=1
if dia<0:
    dia = dia+30
    mes-=1
idade=[dia,mes,ano]
print(idade)
if nasci == hoje:
    print('certo',nasci + hoje)

