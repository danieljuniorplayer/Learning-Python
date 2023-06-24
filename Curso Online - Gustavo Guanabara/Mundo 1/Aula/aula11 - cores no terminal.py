#padrão ANSI, escape sequence

'''print('teste',\033[0;30;41m)
print('teste',\033[4;33;44m)
print('teste',\033[1;35;43m)
print('teste',\033[30;42m)
print('teste',\033[m)
print('teste',\033[7;30m)'''

print('\033[30;46mOlá mundo\033[m')
nome = 'Lucas'
i = '\33[4;34m'
f = '\33[m'
print(f'Olá! Muito prazer em te conhecer, {i}{nome}{f}!')


c31 = '\033[31m'
c32 = '\033[32m'
c33 = '\033[33m'
c34 = '\033[34m'
E = '\033[m'

def soma(n1,n2):
    print(f'A soma de {c33}{n1} + {n2} ={E} {c32}{n1+n2}{E}')
soma(4,9)

print(f'Olá, meu nome é {c33}Daniel!{E}')