while True:
    cont = input('1-Continuar \n0-Sair: ')
    print(cont)

    if cont == '1':
        nome = input('Digite seu nome: ')
        print('Prazer em te conhecer, {}!'.format(nome))

        if nome == 'daniel':
            print('Você digitou seu nome correto.')
        elif nome == 'Thiago':
            print('Na verdade, {} é seu irmão.'.format(nome))
        elif nome == 'raissa':
            print('Na verdade, {} é sua irmã.'.format(nome))
        else:
            print('{} é um nome não reconhecido.'.format(nome))
    elif cont == '0':
        print('Encerrando o programa...')
        break
    else:
        print('Opção inválida. Por favor, digite 1 para continuar ou 0 para sair.')

print('Fim do Programa')
