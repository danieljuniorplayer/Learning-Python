import math
num = float(input('Digite um número'))
r = num**0.5

print(math.sqrt(num))   # raiz quadrada
print(math.ceil(num))   # arredonda pra cima
print(math.floor(num))  # arredonda pra baixo

from math import sqrt, ceil, floor
print(sqrt(num))   # raiz quadrada
print(ceil(num))   # arredonda pra cima
print(floor(num))  # arredonda pra baixo

# função round() não precisa importar
print('\n',round(num),'\n')       # +0.5 arredonda pra cima -0.5 arredonda pra baixo

from random import random,randint # radom = valores aleatórios
i = randint(1,10)
print(i)
