from random import sample,randint
import time

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
numeros=[]
for j in range(0,jogos):
    for c in range(0,6):
        while True:
            n = randint(1,60)
            if n not in numeros:
                numeros.append(n)
                break
    print(f'Jogo {j+1}: {numeros}')
    numeros.clear()
    time.sleep(0.5)

# simplificado
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for j in range(0,jogos):
    print(f'{j+1}° jogo: ',(sample(range(1, 60), 6)))
    time.sleep(0.5)