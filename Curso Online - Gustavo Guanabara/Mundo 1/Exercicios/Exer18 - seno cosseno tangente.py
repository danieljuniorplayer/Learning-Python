
angulo = float(input('Digite o ângulo desse triângulo'))
#seno = oposto/hipotenusa
#cosseno = adjacente/hipotenusa
#tangente = oposto/adjacente

from math import sin, cos, tan, radians

rad = radians(angulo)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print(f'seno: {seno}')
print(f'cosseno: {cosseno}')
print(f'tangente: {tangente}')

