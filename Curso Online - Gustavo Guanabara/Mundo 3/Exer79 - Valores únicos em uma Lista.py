lista=[]
print('Adicione valores a lista ou digite: \033[31m000 para Sair\033[m')
while True:
    a = str(input('Digite um valor: '))
    if a == '000':
        break
    elif int(a) in lista:
        print(f'\033[31m{int(a)} \033[mjá tem na lista, Digite um valor diferente...')
    else:
        lista.append(int(a))
print(sorted(lista))

