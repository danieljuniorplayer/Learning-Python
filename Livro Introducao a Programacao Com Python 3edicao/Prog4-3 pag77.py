# PrograMa 4.3 - Cálculo do IMposto de Renda (forma errada)
"""Um problema comum é quando temos de pagar Imposto de Renda. Normalmente, pagamos o Imposto de Renda por faixa
de salário. Imagine que, para salários menores que R$ 1.000,00, não teríamos imposto a pagar, ou seja, alíquota 0%.
Para salários entre R$ 1.000,00 e R$ 3.000,00, pagaríamos 20%. Acima desses valores, a alíquota seria de 35%.
Esse problema se pareceria muito como anterior, salvo se o imposto não fosse cobrado diferentemente para cada
faixa, ou seja, quem ganha R$ 4.000,00 tem os primeiros R$ 1.000,00 isentos de imposto; com o montante entre R$1.000,00
e R$ 3.000,00 pagando 20%, e o restante pagando os 35%. Vejamos a solução:"""

#-----------------------------------------Entrada de dados ---------------------------------------------------
salario = float(input('Qual o seu salário?'))

#-----------------------------------Se salario for maior que 3000 reais --------------------------------------
if (salario > 3000):
    a = 1000        # parte do salario que será isento de imposto
    b = 3000        # parte do salario que será cobrado 20% de imposto
    c = 4000        # parte isenta + parte que cobra 20%

    if(salario<=4000):
        imposto = (salario-a)*20/100

        print(f'Se Você tiver o salario de {salario}, deve pagar R$ {imposto:.2f} de imposto')
    else:
        imposto = (salario-4000)*35/100+600
        print(f'Se Você tiver o salario de {salario}, deve pagar R$ {imposto:.2f} de imposto')

#--------------------------------Se salario for entre 1000 e 3000 reais -----------------------------------------
elif (salario >=1000):
    print('Você deve pagar 20% de imposto')

#--------------------------------Se salario for menor que 1000 reais --------------------------------------------
else:
    print('Você não deve pagar imposto')