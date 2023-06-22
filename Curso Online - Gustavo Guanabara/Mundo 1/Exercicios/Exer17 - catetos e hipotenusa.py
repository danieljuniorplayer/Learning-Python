cateto_oposto = float(input('Qual é o comprimento do cateto oposto? '))
cateto_adjacente = float(input('Qual é o comprimento do adjacente oposto? '))
hipotenusa = (cateto_oposto**2 + cateto_adjacente**2)**0.5
print(f'A hipotenusa é: {hipotenusa:.2f}')

# utilizando a biblioteca math
from math import sqrt
oposto = float(input('Qual é o comprimento do cateto oposto? '))
adjacente = float(input('Qual é o comprimento do adjacente oposto? '))
hipotenusa = sqrt(oposto**2 + adjacente**2)
print(f'A hipotenusa é: {hipotenusa:.2f}')