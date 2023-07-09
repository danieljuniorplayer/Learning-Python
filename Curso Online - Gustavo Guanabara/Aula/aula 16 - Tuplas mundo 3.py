lanche = ('hamburger', 'pizza', 'leite','sanduba')   # tuplas
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])
# Tuplas são imutáveis
for c in lanche:
    print(c)
for c in range(0,len(lanche)):
    print(f'{lanche[c]}',c,end=', ')
print('')
for c in enumerate(lanche):
    print(c)

for pos,c in enumerate(lanche):
    print(c,pos)

print(sorted(lanche))       # organizado, ordenado

a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(sorted(c))
print(c)
print(c.count(5))           # quantas vezes aparece 5
print(c.index(5))           # que posição está 5
print(c.index(5,2))           # que posição está 5, a partir da posicao 2
pessoa=('gustavo',23,'M',75.88)  # dados de tipos diferentes numa tupla
print(pessoa)
del (pessoa)  # apaga pessoa inteira para sempre