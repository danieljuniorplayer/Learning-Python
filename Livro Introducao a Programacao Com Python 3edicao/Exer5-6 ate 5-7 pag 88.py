'''n = int(input( "Tabuada de:"))
X = 1
while x <= 10:
print(n + x)
X = X + 1'''
#Exercício 5.6 Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4,..

n = int(input('\nTabuada de:'))
x=1
while x <= 10:
    print(f'{n}x{x}={n*x}, ',end='')
    x+=1

#Exercício 5.7 Modifique o programa anterior de forma que o usuário também
#digite o início e o fim da tabuada, em vez de começar com 1 e 10.

x = int(input('\nTabuada de:'))
a = int(input('Você quer que comece a multiplicar a partir de qual valor?'))
b = int(input('Você quer que termine a multiplição em qual valor?'))
while a <= b:
    print(f'{x}x{a}={x*a}, ',end='')
    a+=1