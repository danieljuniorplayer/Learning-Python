'''Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado da
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação
de dois números como somas sucessivas de um deles. Assim, 4 x 5 = 5 +
5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.'''

n1 = int(input('Entre com o primeiro número'))
n2 = int(input('Entre com o segundo número'))
i = 1
resul = 0
while i <= n2:
    resul = resul + n1
    i+=1
print(resul)