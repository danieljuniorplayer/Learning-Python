# Programa 4.3 pag 77 - Cálculo do imposto de Renda (Coreção)
"""Um problema comum é quando temos de pagar Imposto de Renda. Normalmente, pagamos o Imposto de Renda por faixa
de salário. Imagine que, para salários menores que R$ 1.000,00, não teríamos imposto a pagar, ou seja, alíquota 0%.
Para salários entre R$ 1.000,00 e R$ 3.000,00, pagaríamos 20%. Acima desses valores, a alíquota seria de 35%.
Esse problema se pareceria muito como anterior, salvo se o imposto não fosse cobrado diferentemente para cada
faixa, ou seja, quem ganha R$ 4.000,00 tem os primeiros R$ 1.000,00 isentos de imposto; com o montante entre R$1.000,00
e R$ 3.000,00 pagando 20%, e o restante pagando os 35%. Vejamos a solução:"""

# Entrada de dados
salario = float(input('Qual o seu salário?'))   
imposto = 0

# Se salario for maior que 3000 reais, 35% de imposto
if salario > 3000:
    imposto = (salario - 3000) * 0.35 + 400
    print(f'Se Você tiver o salario de R$ {salario:.2f}, você deve pagar R$ {imposto:.2f} de imposto')
# Se salario for entre 1000 e 3000 reais, 20% de imposto
elif salario > 1000:
    imposto = (salario - 1000) * 0.2
    print(f'Se Você tiver o salario de R$ {salario:.2f}, você deve pagar R$ {imposto:.2f} de imposto')
# Se salario for menor que 1000 reais, isento de imposto
else:
    print('Você não deve pagar imposto')


