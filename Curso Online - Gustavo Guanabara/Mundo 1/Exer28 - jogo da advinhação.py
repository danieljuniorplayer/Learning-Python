from random import randint
from time import sleep
jogador = int(input('Pense em um número entre 0 e 3:'))
i = randint(0,3)

print('PROCESSANDO...')
sleep(1)

if i == jogador:
    print(f'Você Acertou, eu escolhi {i}, parabéns!')
else:
    print(f'Você Errou, eu escolhi {i}')