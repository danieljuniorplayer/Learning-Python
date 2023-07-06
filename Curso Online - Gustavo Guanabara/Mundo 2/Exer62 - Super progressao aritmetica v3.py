p = int(input(' Digite o primeiro termo da Progressão Aritmética: '))
r = int(input(' Digite a razão dessa Progressão: '))
print(' Os 10 primeiros termos da PA:\n [',end='')
t=p
c = 0
i = 10
op = True
while op:
    if c < i:
        print(f'{t}',end='')
        print(', ',end='')if c <i-1 else print(']\n','='*50)
        t = t + r
        c+=1
    else:
        qtd = int(input(' Quantos termos você quer adicionar?: '))
        if qtd == 0:
            op = False
        else:
            i = i+qtd
            print(' [', end='')
print('='*51)
print(f' No total, foram mostrados {c} Termos')
print('================== FIM PROGRAMA ===================')
