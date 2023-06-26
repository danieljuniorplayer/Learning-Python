A = '\033[1:34m'
Y = '\033[1:33m'
V = '\033[1:31m'
F = '\033[m'
while True:
    print('=-'*21)
    num = int(input('Digite um número inteiro para converter-lo:'))
    base =int(input('Qual será a base de conversão?\n'
                    f'{A}1{F} para {Y}Binário{F}\n'
                    f'{A}2{F} para {Y}Octal{F}\n'
                    f'{A}3{F} para {Y}Hexadecimal{F}'))
    b=0
    b = 2 if base == 1 else b
    b = 8 if base == 2 else b
    b = 16 if base == 3 else b
    n = num  # preserva o valor original salvando em "n"
    lista = str()  # cria uma lista de string chamada "lista"
    while n >= 1:  # "n" = dividendo
        r = n % b  # "r" = resto da divisão de n/8
        n = n // b  # "n" = resultado de n/8 sem ponto flutuante (divisão inteira)
        r = 'A' if r == 10 else r
        r = 'B' if r == 11 else r
        r = 'C' if r == 12 else r
        r = 'D' if r == 13 else r
        r = 'E' if r == 14 else r
        r = 'F' if r == 15 else r
        lista = lista + str(r)  # Transforma r(resto) em string, e acumula dentro da lista a cada loop
        base = 'Binário' if base == 1 else base
        base = 'Octal' if base == 2 else base
        base = 'Hexadecimal' if base == 3 else base
    print(f'\n{A}{num}{F} em {Y}{base}{F} é igual a {A}{lista[::-1]}{F}\n')  # Lê a string de traz pra frente
    op= int(input(f'{V}1{F} para {V}Continuar{F} | {V}0{F} para {V}Sair{F}'))
    if op == 0:
        print('=-'*7,'FIM PROGRAMA','-='*7)
        break