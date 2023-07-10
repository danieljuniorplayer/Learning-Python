num = list()
for n in range(0,5):
    num.append(int(input(f'Digite um valor para posião {n+1}: ')))

print(num)

print(f'\nO maior valor: {max(num)}, está na posição: ',end='')
for c,n in enumerate(num):
    if n == max(num):
        print(f' {c+1}',end='')
print(f'\nO menor valor: {min(num)}, está na posição: ',end='')
for c,n in enumerate(num):
    if n == min(num):
        print(f' {c+1}', end='')
