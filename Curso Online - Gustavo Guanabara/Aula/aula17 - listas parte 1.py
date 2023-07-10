num = [2,5,9,1]
num[2] = 3
num.append(9)   # cria um novo indice e adiciona na lista
print(num)
num.sort()      # menor para o maio
print(num)
num.sort(reverse=True)  # maior para menor
print(num)

num.insert(2,0)     # adiniona o 0 e joga os outros pra frente
print(f'Na posição 2 inseri o valor 0: {num}')

num.pop()
print(f'Elimina o valor da lista: {num}')

if 4 in num:
    num.remove(4)
else:
    print(f'Não achei o número 4 para remover')

valor =list()   # ou valor = []
valor.append(5)
valor.append(9)
valor.append(4)

for v in valor:
    print(f'Mostra os valores sozinhos: {v}')
from random import randint
lista = list()
for cont in range(0,5):
    lista.append((randint(0,9)))

for c,l in enumerate(lista):
    print(f'Mostra tantos as chaves quanto os valores : {c}, {l}')

a = [2,3,4,7,9]
c = a[:]        # cria uma cópia de a
c[3]=8
print(f'Printando a depois de mudar c: {a}')
print(f'Printando c depois de mudar c: {c}')
b= a        # cria uma ligação entre a e b
b[3]= 8
print(f'Printando a depois de mudar b: {a}')
print(f'Printando b depois de mudar b: {b}')

print('A partir do momento que eu mecho em b, também altera o a:')
print('O python cria uma ligação com as listas: ')





