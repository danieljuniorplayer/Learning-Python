n = int(input('Digite o termo para uma Fibonacci: '))
c = anterior = atual = 1    # todos recebem 1
print('[',end='')
while c <= n:
    if c <= 2:
        print(1,end=', ')
    else:
        proximo = atual + anterior
        anterior = atual
        atual = proximo
        print(proximo, end=', ')if c <n else print(proximo, end=']')    # if ternário
    c += 1