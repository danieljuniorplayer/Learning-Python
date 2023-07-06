p = int(input(' Digite o primeiro termo da Progressão Aritmética: '))
r = int(input(' Digite a razão dessa Progressão: '))
print(' Os 10 primeiros termos da PA:\n [',end='')
t=p
i=10
c = qtd= 1
while qtd!= 0:
    while c <= i:
        print(f'{t}',end='')
        print(', ',end='')if c <i else print(']\n','='*50)
        t = t + r
        c+=1
    qtd = int(input(' Quantos termos você quer adicionar?: '))
    i = i+qtd
    print(' [', end='') if qtd != 0 else print('='*51)
print(f' No total, foram mostrados {c-1} Termos')
print('================== FIM PROGRAMA ===================')