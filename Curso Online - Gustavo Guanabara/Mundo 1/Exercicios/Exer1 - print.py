

while True:
    cont = str(input('1-Continuar \n0-Sair '))
    print(cont)
    print(type(cont))       # mostra qual tipo primitivo pertence
    print(cont.isnumeric()) # mostra se o valor pode ser transformado em numero


    if cont == 0:
        print('Fim Do Programa')
        break
    else:
        nome=input('Digite seu nome')
        print('Prazer em te conhecer {}!'.format(nome))

    if nome == 'daniel':
         print('Voce digitou seu nome correto')
    elif nome == 'Thiago':
        print('Na verdade {} é seu irmão'.format(nome))
    elif nome=='raissa':
        print('na verdade {} é sua irmã'.format(nome))
    else:
            print('{} é um nome não reconhecido'.format(nome))

