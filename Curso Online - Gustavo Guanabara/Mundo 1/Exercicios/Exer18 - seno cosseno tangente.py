
angulo = float(input('Digite o ângulo desse triângulo'))
from math import sin, cos, tan, radians     # radiano é necessário para converter o grau
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'seno: {seno:.2f}')
print(f'cosseno: {cosseno:.2f}')
print(f'tangente: {tangente:.2f}')

