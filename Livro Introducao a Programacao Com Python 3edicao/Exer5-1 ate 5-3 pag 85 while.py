#Exercício 5.1 Modifique o programa para exibir os números de 1 a 100
i=1
while i <= 100:
    print(i)
    i += 1

print('\n') # pula linha

#Exercício 5.2 Modifique o programa para exibir os números de 50 a 100.
i=50                        # definindo valor de i
while i <= 100:             # enquanto i tiver entre 50 e 100 ...
    print(i)                # imprima valor de i
    i += 1                  # some o valor de i mais 1
print('\n')

#Exercício 5.3 Faça um programa para escrever a contagem regressiva do lançamento
#de um foguete. O programa deve imprimir 10, 9, 8, ... , 1, O e Fogo! na tela.'''

import time                         # importa o modulo que traz a função time.sleep
print("Contagem regrassiva...")     # printa na tela antes da funcao ser chamada
time.sleep(1)                       # funcao chamada


i=10
while i > 0:
    print(i)
    time.sleep(1)
    i -= 1
print('0 e Fogo...!')