A = '\033[1:34m'
Y = '\033[1:33m'
V = '\033[1:31m'
F = '\033[m'
while True:
    print('=-'*21)
    num = int(input('Digite um número para converter-lo:'))
    op =int(input('Qual será a base de conversão?\n'
                    f'{A}1{F} para {Y}Binário{F}\n'
                    f'{A}2{F} para {Y}Octal{F}\n'
                    f'{A}3{F} para {Y}Hexadecimal{F}'))
    if op == 1:
        print(f'{A}{num}{F} em Binário é igual a {Y}{bin(num)[2:]}{F}')
    elif op == 2:
        print(f'{A}{num}{F} em Octal é igual a {Y}{oct(num)[2:]}{F}')
    elif op == 3:
        print(f'{A}{num}{F} em Hexadecimal é igual a {Y}{hex(num)[2:]}{F}')
    else:
        print(f'Escolha entre {A}1{F} e {A}3{F}')
    op = int(input(f'{V}1{F} para {V}Continuar{F} | {V}0{F} para {V}Sair{F}'))
    if op == 0:
        print('=-'*7,'FIM PROGRAMA','-='*7)
        break

