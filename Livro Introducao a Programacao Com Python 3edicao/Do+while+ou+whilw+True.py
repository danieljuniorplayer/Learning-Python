

while True:
    op=int(input('1-Continuar\n0-Sair\n'))
    
    if op == 1:
        idade=int(input('Digite sua idade'))

        if idade == 23:
            print('Você Acertou sua idade')
        elif idade==0:
            print('Essa idade não existe')
        else:
            print('Voce errou sua idade')
    elif op!=0:
        print('Escolha entre 1 e 0\n')
    else:
        print('Fim Sistema')
        break
    


		
    