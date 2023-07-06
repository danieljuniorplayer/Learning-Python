from datetime import date
nasci = str(input('Qual sua data de nascimento?\033[37m(Ex: 10/10/2010)\033[m:')).strip().split(sep='/')
dia = date.today().day - int(nasci[0])
mes = date.today().month - int(nasci[1])
ano = date.today().year - int(nasci[2])

if mes<0:
    mes*=-1
    ano-=1
if dia<0:
    dia+=30
    mes-=1
print(f'Você tem...\033[32m{ano} Anos\033[m, {mes} Mêses e {dia} Dias\n')
if ano < 18:
    print(f'Você não está apto para o alistamento militar')
    print(f'Faltando apenas \033[32m{18-ano} anos\033[m')
    print(f'Seu alistamento será em \033[32m{int(hoje[2])+(18-ano)}\033[m')
elif ano == 18:
    print('Você deve se alista IMEDIATAMENTE')
else:
    print(f'O prezo do alistamento foi há \033[32m{ano-18}\033[m anos atrás')
print('\n','-'*15,'FIM PROGRAMA','-'*15)

