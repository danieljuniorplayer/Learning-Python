a = int(input('Digite o primeiro valor'))
b = int(input('Digite o segundo valor'))
c = int(input('Digite o terceiro valor'))

menor = a
if b<=a and b<=c:
    menor = b
if c<=a and c<=b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

if menor == maior:
    print('Os 3 valores são iguais.')
else:
    print(f'Maior: {maior}')
    print(f'menor: {menor}')
# ou também com a função sort
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um último número: '))
l = [n1, n2, n3]
l.sort() # ordena os números da lista em ordem crescente, tornando  o programa mais compacto
print(f'''O maior número é {l[2]} e 
O menor número é {l[0]}''')