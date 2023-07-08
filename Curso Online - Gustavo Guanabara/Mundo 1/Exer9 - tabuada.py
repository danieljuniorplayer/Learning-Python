n1 = int(input('Digite um número para ver sua tabuada: '))
i=0
print('\033[37m=\033[m'*11)
while i < 10:
    i+=1
    print(f'{n1} x {i:2} = \033[33m{n1*i:2}\033[m')
print('\033[37m=\033[m'*11)