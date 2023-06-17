'''Exercício 5.15 Escreva um programa para controlar uma pequena máquina registradora.
Você deve solicitar ao usuário que digite o código do produto e a quantidade
comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto:
Código, Preço   Código, Preço
1       0,50    5       7,00
2       1,00    9       8,00
3       4,00
Seu programa deve exibir o total das compras depois que o usuário digitar O.
Qualquer outro código deve gerar a mensagem de erro "Código inválido'''
total = 0
while True:
    codigo = int(input('Digite o código do produto, ou "0" para Sair'))
    if codigo == 0:
        break
    quantidade = int(input('Digite a quantidade: '))
    if codigo == 1:
        total += (0.50 * quantidade)
    elif codigo == 2:
        total += (1 * quantidade)
    elif codigo == 3:
        total += (4 * quantidade)
    elif codigo == 5:
        total += (7 * quantidade)
    elif codigo == 9:
        total += (8 * quantidade)
    else:
        print(' '*10,f'Código inválido, ({codigo})')

print(total)
