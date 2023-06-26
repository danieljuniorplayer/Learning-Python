salario = float(input('Me diga qual o seu salário mensal: R$'))
preco = float(input('Digite o valor da casa: R$'))
anos = int(input('Em quantos anos você pretende pagar a casa: '))

porcento = salario*0.30
prestacao = preco/(anos*12)
print('\nBaseado nas suas imformações...\n')
if prestacao <= porcento:
    print(f'Sua prestação foi \033[32mAPROVADO!\033[m')
    print(f'Você pagará R${prestacao:.2f} por mês')
else:
    print(f'Sua prestação foi \033[31mNEGADA!\033[m')
    print(f'\033[31mO valor da prestação ultrapassa 30% do seu salário\033[m!')
    print(f'30% do seu salário: {porcento:.2f}')
    print(f'Valor da prestção: {prestacao:.2f}')
    print('\033[31mTente Aumentar a quantidade de anos para poder ser aprovado\033[m!')
