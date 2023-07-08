from random import randint
cont=0
while True:
    print('=' * 30)
    while True:
        escolha = str(input('[I] ÍMPA | [P] PAR :')).strip().upper()[0]
        jogador = int(input('Digite um número: '))
        if escolha in 'PI':
            escolha = 0 if escolha == 'P' else 1
            break
        else:
            print('\033[31mTente novamente!\033[m')
    maquina=randint(1,10)
    print(f'Maquina escolheu: {maquina}')
    soma = jogador + maquina
    print(f'Somando tudo dá: {soma} ', end='')
    resultado = soma % 2
    print('(PAR)' if resultado == 0 else '(ÍMPA)')
    print('='*30)
    if resultado == escolha:
        print('Voce acertou, tente novamente')
    else:
        print('voce errou, fim de jogo')
        break
    cont+=1
print('='*30)
print(f'Voce acertou {cont} vezes')
