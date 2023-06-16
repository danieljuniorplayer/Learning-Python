'''Exercício 5.13 Escreva um programa que pergunte o valor inicial de uma dívida e
o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número
de meses para que a dívida seja paga, o total pago e o total de juros pago.'''

divida_inicial = float(input('Qual é o valor da sua dívida?'))
juros = float(input('Qual é o valor do jurus mensal?'))
pago = float(input('Qual é o valor mensal que você irá pagar?\n'))
divida_atual = divida_inicial

i=0
total_pago = 0
total_juros = 0
print(f' Mês: | Total pago: | Dívida atual: | Soma dos juros pagos: ')
while divida_atual > 0:
    print(f'{i:6.0f}|   {total_pago:10.2f}|     {divida_atual:10.2f}|    {total_juros:5.2f}')
    porcentagem = round(divida_atual*juros/100,2)
    divida_atual = divida_atual + porcentagem - pago
    total_pago += pago
    total_juros += porcentagem
    i+=1

print(f'{i:6.0f}|   {total_pago+divida_atual:10.2f}|           0.00|    {total_juros:5.2f}')