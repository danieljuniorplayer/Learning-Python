salario = float(input('Qual é o salário do Funcionário? R$'))
reajuste = salario + (salario*0.15)
verde = '\033[32m'
amarelo = '\033[33m'
F = '\033[m'
print(f'Um funcionário que ganhava R${verde}{salario:.2f}{F}, com {amarelo}15%{F} de aumento, passa a ganhar R${verde}{reajuste:.2f}{F}')