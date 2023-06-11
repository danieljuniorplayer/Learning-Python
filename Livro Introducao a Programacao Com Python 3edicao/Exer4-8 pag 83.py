"""Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada."""

print('\nVocê está preste a usar uma calculadora.\n'
      'Cada tipo de operação, segue um simbolo: \n'
      'Soma..........(+);\n'
      'Subtração.....(-);\n'
      'Multiplicação.(*);\n'
      'Divisão.......(/);\n')
print('Use estes símbolos na sua calculadora.\n'
      'Aqui vai um exemplo: 3*3.\n'
      'Agora é sua vez, pode começar a digitar:')
valor = str(input())

# Descobrindo qual o primeiro valor
i = 1                           # Contador
while valor[0:i].isnumeric():   # Enquanto o valor fatiado for numerico, faça operação,
    n1 = valor[0:i]             # Salvando a string numerica em n1
    n1 = float(n1)              # Trasnformando uma string em float
    #print(n1)                  # Imprime o valor encontrado
    i += 1                      # acrecenta + 1 em i a cada loop
    operacao = valor[i-1:i]     # descobrindo qual operação a pessoa quer realizar.
    # operacao recebe o valor que vem depois dos numericos, ou seja, alfabetico


# Descobrindo qual o segundo valor
i = -1
while valor[i:].isnumeric():    # Se omitimos o final da fatia, ele sempre vai procurar o final da string
    n2 = valor[i:]              # salva o valor da string em n2
    n2 = float(n2)              # transforma n2 em float
    #print(n2)                   # imprime n2 na tela
    i -= 1                      # adiciona -1 em i a cada loop


# imprime o valor alfabetico encontrado, que esta salvo em operacao
if operacao == '+':
    print(f'{n1} + {n2} = ',n1+n2)
elif operacao == '-':
    print(f'{n1} - {n2} = ', n1-n2)
elif operacao == '*':
    print(f'{n1} x {n2} = ', n1*n2)
elif operacao == '/':
    print(f'{n1} / {n2} = ', n1/n2)
else:
    print('Escolha uma opção entre (+), (-), (*) ou (/)')

