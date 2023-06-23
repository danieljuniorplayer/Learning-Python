a = int(input('Digite o primeiro valor'))
b = int(input('Digite o segundo valor'))
c = int(input('Digite o terceiro valor'))

if a>=b and a>=c:
    print(f'{a} é o maior valor')
    if c<b:
        print(f'{c} é o menor valor')
    else:
        print(f'{b} é o menor valor')
elif b>=c and b>=a:
    print(f'{b} é o maior valor')
    if a<c:
        print(f'{a} é o menor valor')
    else:
        print(f'{c} é o menor valor')
else:
    print(f'{c} é o maior valor')
    if b<a:
        print(f'{b} é o menor valor')
    else:
        print(f'{a} é o menor valor')

