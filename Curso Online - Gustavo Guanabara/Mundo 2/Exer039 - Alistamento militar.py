from datetime import date
print('Qual sua data de nascimento?',end='')
nasci = str(input('\033[37m(Ex: 10/10/2010)\033[m:')).strip().split(sep='/')
hoje = str(date.today()).split(sep='-')[::-1]
dia = int(hoje[0])-int(nasci[0])
mes = int(hoje[1])-int(nasci[1])
ano = int(hoje[2])-int(nasci[2])
if mes<0:
    mes*=-1
    ano-=1
if dia<0:
    dia+=30
    mes-=1
print(f'Você tem...\033[32m{ano} Anos\033[m, {mes} Mêses e {dia} Dias\n')
if ano < 18:
    print(f'Você não está apto para o alistamento militar,\n'
          f'Faltando apenas \033[32m{18-ano} anos\033[m \n'
          f'Seu alistamento será em \033[32m{int(hoje[2])+(18-ano)}\033[m')
elif ano == 18:
    print('Você deve se alista IMEDIATAMENTE')
else:
    print(f'O prezo do alistamento foi há \033[32m{ano-18}\033[m anos atrás')

