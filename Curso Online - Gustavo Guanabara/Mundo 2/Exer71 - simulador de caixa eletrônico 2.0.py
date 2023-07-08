print('='*40)
print('{:^40}'.format('CAIXA ELETRÔNICO'))
print('='*40)
valor=cedulas=0      # todos recebem 0
while valor<=0:                     # Só aceita valores maiores do que 0
    valor = int(input('\nQual valor será sacado? R$'))
print('Será emitido:')
val = valor                 # salva o valor em "val" para não alterar ""valor"
sub=50                      # primeiro nota que será subtraido pelo "val"
while True:
    while val>=sub:         # enquanto "val" for >= "sub"
        val-=sub            # subtrai "val" por "sub"
        cedulas+=1          # conta quantas vezes o valor foi subtraido pelo mesmo "sub"
    if cedulas >0:          # so printa na tela se "cedulas" for maior que 0
        print(f'\033[32m{cedulas}\033[m nota(s) de R$\033[32m{sub}\033[m')
    cedulas = 0             # "cedulas" recebe zero cada vez que "sub" muda de valor
    if val >=20:
        sub= 20
    elif val>=10:
        sub= 10
    elif val>=1:
        sub= 1
    else:                   # se "val" = zero, break
        break
