import random
print('='*11,'\033[35mJOGO DA ADVINHAÇÃO\033[m','='*11)
print('A maquina escolheu um número de 1 a 10.\n'
      'Sua missão é advinhar qual foi esse número')
print('='*42)

jogador = int(input('Digite um número de 1 a 10: '))
m = random.randint(1,10)
cont =1
while jogador != m:
    if jogador < m:
        jogador = int(input(f'Dica: +{jogador}, Tente novamente: '))
    if jogador > m:
        jogador = int(input(f'Dica: -{jogador}, Tente novamente: '))
    cont+=1

print('='*42)
print(f'Parabéns você acertou na {cont}ª tentativa! ')
print('='*42)