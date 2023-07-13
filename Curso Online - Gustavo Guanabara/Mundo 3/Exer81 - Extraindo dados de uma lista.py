lista=[]
a= 0
print('Acrecente valores ou digite: 000 Para Sair:')
while True:
    valor= str(input('Digite um valor'))
    if valor == '000':
        break
    else:
        valor= int(valor)
        if a == 0 or valor <= min(lista):
            lista.append(valor)
            print(lista)
        for k, v in enumerate(lista):
            if v < valor:
                lista.insert(k,valor)
                break
    a+=1
print(f'Você digitou {a} números')
print(lista)
print(f'O número 5 está na lista.' if 5 in lista else 'O número 5 não está na lista.')
