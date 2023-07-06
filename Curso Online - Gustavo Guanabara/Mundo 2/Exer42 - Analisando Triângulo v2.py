lado1 = float(input('Digite o comprimento do primeiro lado:'))
lado2 = float(input('Digite o comprimento do segundo lado:'))
lado3 = float(input('Digite o comprimento do terceiro lado:'))

if lado1+lado2 > lado3 and lado2+lado3 > lado1 and lado3+lado1 > lado2:
    print(f'Essas retas formam um triângulo!')
    if lado1 == lado2 == lado3:
        print(f'Esse triângolo é Equilátero: todas os lados são iguais')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print(f'Esse triângulo é Isóceles: dois lados iguais')
    else:
        print(f'Esse triângulo é Escaleno: todos os lados diferentes')
else:
    print(f'Essas retas não formam um triângulo!')
