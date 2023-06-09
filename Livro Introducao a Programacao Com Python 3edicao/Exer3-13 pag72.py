#pag 72
#Exercício 3.13 Escreva um programa que converta uma temperatura digitada em
#ºC em ºF. A fórmula para essa conversão é: f = 9*c/5+32
c = float(input('Digite a temperatura em ºC'))
f = (9*c)/5+32
print(f'{c} ºC equivala a {f:.2f} ºF')