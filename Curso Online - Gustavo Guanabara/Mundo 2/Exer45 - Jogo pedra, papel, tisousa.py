A = '\033[34m'; R = '\033[31m'; Y = '\033[33m'; E = '\033[m'
from random import randint
from time import sleep
itens = 'PEDRA','PAPEL','TESOURA'

while True:
    print('-' * 45)
    print('JOGO: JOKENPÔ')
    jogador = int(input(f'{Y}[1] PEDRA\n'f'[2] PAPEL\n'f'[3] TESOURA{E}\n'
                        'Escolha uma das opções:')) -1
    print('-' * 15,end='')
    sleep(0.5)
    print('-' * 15,end='')
    sleep(0.5)
    print('-' * 15)
    maquina = randint(0, 2)
    op = True
    if jogador != 0 and jogador != 1 and jogador !=2:
        op = False
        print(f'Opção {R}INVÁLIDA{E}, devia escolher entre {Y}1 a 3{E}!')
    if op:
        print(f'A Sua escolha foi  {Y}{itens[jogador]}{E}')
        print(f'A Maquina escolheu {Y}{itens[maquina]}{E}')
        if maquina == jogador:                              # Empate
            print(f'{Y}DEU EMPATE!{E}')
        elif maquina+1 == jogador or maquina-2 == jogador:  # jogador ganha
            print(f'{A}VOCÊ GANHOU!{E}')
        else:                                               # Máquina ganha
            print(f'{R}MAQUINA GANHOU!{E}')
    print('-' * 45)
    op = int(input('[1] CONTINUAR | [0] SAIR'))
    if op == 0:
        break
print('-'*17,f'{A}FIM JOGO{E}','-'*18)






