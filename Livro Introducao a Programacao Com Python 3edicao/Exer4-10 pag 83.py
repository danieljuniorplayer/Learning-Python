'''Exercício4.10 Escreva um programa que calcule o preço a pagar pelo fornecimento
de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação:
R para residências, I para indústrias e C para comércios. Calcule o preço a
pagar de acordo com a tabela a seguir.
Preço por tipo e faixa de consumo
Tipo Faixa (kWh) Preço
Residencial
Até 500 R$ 0,40
Acima de 500 R$ 0,65
Comercial
Até 1000 R$ 0,55
Acima de 1000 R$ 0,60
Industrial
Até 5000 R$ 0,55
Acima de 5000 R$ 0,60'''

# simula o cls no pycharmy-----------------------------------------------------------------------------------
def limpar_tela():
    print("\n" * 100)
limpar_tela()

print('Sistema: Preço a pagar pelo fornecimento de energia elétrica')


tipo = str(input('Qual foi o tipo de intalação?\n'
             'R - Residências\n'
             'I - Indústrias\n'
             'C - Comércios\n'))
limpar_tela() # simula limpa tela
consumo = float(input('Qual a quantidade consumida em kWh?'))

limpar_tela()
if tipo == 'I' or tipo == 'i':
    if consumo > 5000:
        print('tera que pagar R$ 0,60')
    else:
        print('tera que pagar R$ 0,55')

elif tipo == 'C' or tipo == 'c':
    if consumo > 1000:
        print('tera que pagar R$ 0,60')
    else:
        print('tera que pagar R$ 0,55')

elif tipo == 'R' or tipo == 'r':
    if consumo > 500:
        print('tera que pagar R$ 0,65')
    else:
        print('tera que pagar R$ 0,40')

else:
    print('Escolha entre R, I ou C')

