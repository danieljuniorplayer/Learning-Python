produtos = (('macarrão',13.89),('arroz',14.59), ('feijão',9.29), ('iorgute',8.32), ('sal',1.89), ('abacaxi',13.45), ('banana',6.89), ('carne',34.49), ('notbook',3431.89), ('micro-ondas',1323.72), )
print('='*40,f'\n{"LISTAGEM DE PRODUTOS":^40}')
print('='*40)
for c in range(0,len(produtos)):
    print(f'{produtos[c][0]:.<30}R${produtos[c][1]:>8}')

