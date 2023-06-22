'''Programa 5.1 - Contagem de cédulas
Vejamos como exemplo um programa que leia um valor e que imprima a quantidade
de cédulas necessárias para pagar esse mesmo valor. Para simplificar,
vamos trabalhar apenas com valores inteiros e com cédulas de R$ 50, R$ 20,
R$ 10, R$ 5 e R$ 1.
'''









# Progra~a 5.1 - Contage~ de cédulas
valor  = float(input(" Di.g i.te o va lo r a pagar:"))
cedulas= 0
atual = 100
apagar= valor
while True:
    if atual<= apagar:
        apagar -= atual
        cedulas+= 1
    else:
        print(f"{cedulas} cédula (s) de R${atual}")
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1

        elif atual == 1:
            atual = 0.50
        elif atual == 0.50 :
            atual= 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cedulas= 0