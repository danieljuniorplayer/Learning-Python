"""Exercício4.9 Escreva um programa para aprovar o empréstimo bancário para compra
de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e
a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a
30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar
dividido pelo número de meses a pagar."""

valor = float(input('Qual o valor da casa?'))
salario = float(input('Qual seu salário?'))
anos = int(input('Em quantos anos você vai pagar?'))

prestacao = valor / (anos*12)

if prestacao <= salario*0.3:
    print(f'O valor da prestação será: {prestacao:.2f}')
else:
    print('O valor da prestacao encontrado ultrapassa os 30%')
