n = 1
impa = par = 0
while n!=0:
    n = int(input('Digite um valor acima de zero: '))
    if n!=0:
        if n%2 ==0:
            par+=1
        else:
            impa+=1
print(f'Quantidade de valores pares: {par}')
print(f'Quantidade de valores impares: {impa}')