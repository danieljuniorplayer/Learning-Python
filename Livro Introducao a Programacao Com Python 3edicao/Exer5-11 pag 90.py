'''Exercício 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período.'''

deposito = float(input('Qual foi o depósito inicil?\n'))
taxa = float(input('Qual é a taxa de jurus da poupança\n'))
i = 1               # contador
ganho = deposito    # acumulador

while i <= 24:
    ganho = ganho * (taxa/100) + ganho
    print(ganho)
    i+=1

