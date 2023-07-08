while True:
    n = int(input('Digite um número positivo para saber sua Tabuada: ou\n'
                  'Qualquer Numero \033[31mnegativo\033[m para Sair: '))
    if n <0:
        break
    for c in range(1,11):
        print(f'|{n:<2} x {c:^3}={n*c:>3}|')