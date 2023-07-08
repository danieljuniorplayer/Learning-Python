salario = float(input('Digite seu salário atual: R$'))

if salario > 1250:
    aumento = salario*0.10+salario
    print(f'Seu salário mais 10% vai valer: R${aumento:.2f}')
else:
    aumento = salario*0.15+salario
    print(f'Seu salário mais 15% vai valer: R${aumento:.2f}')