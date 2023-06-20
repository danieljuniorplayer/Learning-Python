'''Programa 5.1 - Contagem de cédulas
Vejamos como exemplo um programa que leia um valor e que imprima a quantidade
de cédulas necessárias para pagar esse mesmo valor. Para simplificar,
vamos trabalhar apenas com valores inteiros e com cédulas de R$ 50, R$ 20,
R$ 10, R$ 5 e R$ 1.
'''
valor = float(input('Digite o valor que deve ser pago'))
apagar = valor
qtd = 0
print('Notas necessárias:')
while True:
    q = qtd
    qtd += 1
    if apagar >= 50:
        apagar-=50
        print(f'R$50.00')
    elif apagar >= 20:
        apagar -= 20
        print('R$20.00')
    elif apagar >= 10:
        apagar -= 10
        print('R$10.00')
    elif apagar >= 5:
        apagar -= 5
        print('R$5.00')
    elif apagar >= 1:
        apagar -= 1
        print('R$1.00')
    else:
        break

print(f'Total de notas: {q}')

# Progra~a 5.1 - Contage~ de cédulas
valor  = int(input(" Di.g i.te o va lo r a pagar:"))
cedulas= 0
atual = 50
apagar= valor
while True:
    if atual<= apagar:
        apagar -= atual
        cedulas+= 1
    else:
        print(f"{cedulas} cédula (s) de R${atual}")
        if apagar == 0:
            break
        if atual== 50 :
            atual= 20
        elif atual == 20:
            atual= 10
        elif atual== 10:
            atual = 5
        elif atual== 5:
            atual= 1
        cedulas= 0