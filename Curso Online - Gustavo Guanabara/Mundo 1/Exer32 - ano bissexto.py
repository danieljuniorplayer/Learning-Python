anos = (input('Digite um ano:')).strip().replace(',',' ').replace('e',' ').split()
objeto = anos

print(anos)

i=0
qtd = len(anos)
while i < qtd:
    ano = int(anos[i])
    if ano%4 ==0:       # 1
        if ano%100 ==0:     # 2
            if ano%400 ==0:     # 3
                print(f'{ano}É bissexto')
            else:
                print(f'{ano} não é bissexto')
        else:
            print(f'{ano} É Bissexto')

    else:
        print(f'{ano} Não é um ano bissexto, tem (365) dias')
    i+=1

'''if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
        print(f'{ano} É ano Bissexto')'''