"""Exercício4.4 Escreva um programa que pergunte o salário do funcionário e calcule
o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
10%. Para os inferiores ou iguais, de 15%."""

salario = float(input('Qual o seu salário?'))
if salario > 1250:
    aumento = salario*0.1
else:
    aumento = salario*0.15
print(f'Seu salário vai ter um aumento de R$ {aumento:.2f}')