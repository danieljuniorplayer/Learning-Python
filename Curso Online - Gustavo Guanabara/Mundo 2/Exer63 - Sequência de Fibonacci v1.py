n = int(input('Digite o termo para uma Fibonacci: '))
c=3
anterior = atual = 1    # todos recebem 1
print('[1, 1, ',end='')
while c <=n:
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    print(proximo, end=', ') if c < n else print(proximo, end=']')  # if ternário
    c += 1