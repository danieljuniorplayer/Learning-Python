a = int(input('Digite o primeiro valor'))
b = int(input('Digite o segundo valor'))
c = int(input('Digite o terceiro valor'))

if a>=b and a>=c:
    print(f'{a} é o maior valor')
    if b>c:
        print(f'{c} é o menor valor')
    else:
        print(f'{b} é o menor valor')
else:
    if b>c:
        print(f'{b} é o maior valor')
    else:
        print(f'{c} é o maior valor')
    print(f'{a} é o menor valor')