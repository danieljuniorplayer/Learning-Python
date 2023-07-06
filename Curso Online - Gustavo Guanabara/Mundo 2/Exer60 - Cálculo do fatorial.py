import sys
sys.set_int_max_str_digits(100000)
print('Program: Descobrindo Fatorial de um número')
numero = int(input('Digite um número: '))

# Utilizando for
fatorial =1
for f in range(numero,1,-1):
    fatorial *= f
print(f'Fatorial: {fatorial}')

# Utilizando while
print(f'O fatorial de {numero}! = ',end='')
c =numero
fat = 1
while c >0:
    print(f'{c}',end='')
    print(' x ' if c >1 else ' = ',end='')
    fat*=c
    c-=1
print(fat)

# Utilizando bibliote math
from math import factorial
n = int(input('Digite um numero'))
print(f'Fatorial de {n} = {factorial(n)}')
