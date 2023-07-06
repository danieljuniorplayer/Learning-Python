a1 = int(input('Digite o primeiro termo da Progressão Aritmética: '))
r = int(input('Digite a razão dessa Progressão: '))
# primeita forma
lista= []
n=a1
for c in range(0,10):   # de 1 a 10
    lista.append(n)     # incremento
    n += r
print(lista)

# segunda forma
l = []              # criando uma lista para salvar os valores
an = a1+(10-1)*r       # encontra o décimo termo
for c in range(a1,an+r,r):   # de 1 a 10
    l.append(c)
print(l)


