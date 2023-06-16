'''deposito = float(input('Qual foi o depósito inicil?\n'))
taxa = float(input('Qual é a taxa de jurus da poupança\n'))
i = 1               # contador
ganho = deposito    # acumulador

while i <= 24:
    ganho = ganho * (taxa/100) + ganho
    print(ganho)
    i+=1
'''

#Exercício 5.12 Altere o programa anterior de forma a perguntar também o valor
#depositado mensalmente. Esse valor será depositado no início de cada mês, e você
#deve considerá-lo para o cálculo de juros do mês seguinte.

deposito = float(input('Qual foi o depósito inicil?\n'))
taxa = float(input('Qual é a taxa de jurus da poupança\n'))
mensal = float(input('Qual vai ser seu deposito mensal?\n'))
i = 1               # contador
ganho = deposito    # acumulador

while i <= 24:
    ganho = (ganho + mensal) * (taxa/100) + (ganho + mensal)
    print(f'{ganho:.2f}')
    i+=1