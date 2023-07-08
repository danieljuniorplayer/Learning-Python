print('='*40,'\n      CADASTRE PRODUTOS NA COMPRA')
tot=acima1k=cont=menor=nomProBar=0
while True:
    print('=' * 40)
    nome = str(input('Nome: '))
    preco = float(input('Preço: R$'))
    cont += 1
    tot+= preco     # total gasto
    if preco > 1000:        # produtos acima de 1k
        acima1k+=1
    # Nome do produto mais barato
    if cont==1 or menor >= preco:
        menor=preco
        nomProBar = nome
    # condicao de parada
    op=' '
    while op not in 'SN':
        op =str(input('Quer continuar?(S/N): ')).strip().upper()[0]
    if op == 'N':
        break
print('=' * 40)
print(f'Total gastos na compra:  \033[33m{tot:.2f}\033[m')
print(f'Total de produtos acima de R$1.000,00: \033[33m{acima1k}\033[m')
print(f'O nome do produto mais barato: \033[33m{nomProBar}\033[m, custando: \033[33m{menor}\033[m')