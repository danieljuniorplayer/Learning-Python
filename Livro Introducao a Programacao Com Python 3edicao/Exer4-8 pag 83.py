"""Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada."""


n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
op = int(input('Qual operação você deseja realizar com esses 2 valores?\n'
      '1-Soma\n'
      '2-Subtração\n'
      '3-Multiplicaçao\n'
      '4-Divisão\n'))
if op == 1:
    print(f'A soma de {n1} + {n2} = ', n1+n2)
elif op == 2:
    print(f'A soma de {n1} - {n2} = ', n1-n2)
elif op == 3:
    print(f'A soma de {n1} x {n2} = ', n1*n2)
elif op == 4:
    print(f'A soma de {n1} ÷ {n2} = ', n1/n2)
else:
    print('Escolha uma opção entre 1 e 4')