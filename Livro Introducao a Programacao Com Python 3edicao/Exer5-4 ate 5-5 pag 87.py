# Exercício 5.4 Modifique o programa anterior para imprimir de 1 até o número
# digitado pelo usuário, mas, dessa vez, apenas os números ímpares.
x = 7
print(x % 2)  # % Módulo ou resto de x dividido pra 2, se for 0 é par, se for 1 é ímpa

x = int(input('Até qual numero você quer imprimir?'))
i = 1
while i <= x:
    if i % 2 == 1:  # Módulo ou resto, se o resto de i/2 = 1 (ímpa)...
        print(i, end='')  # imprime o volar impa. end='' imprime os valores sem pular linha.
    else:  # se não for impa...
        print(end=' ')  # imprime um espaço, sem pula linha
    i += 1

# Exercício 5.5 Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.
x = int(input('\nAté qual numero você quer imprimir?\n'))
print('Os valores abaixo todos são impares.\n'
      'Os valores com parenteses são multiplos de 3\n')
i = 1
while i <= x:
    if i % 2 == 1:                  # Módulo ou resto, se o resto de i/2 = 1 (ímpa)...
        if i // 3 == i / 3:         # criar operacao que mostra os numeros  multiplos de 3
            print(f'({i})',end='')  # imprime o volar impa. end='' imprime os valores sem pular linha.
        else:
            print(i,end='')

    else:                        # se não for impa...
        print(end=' ')          # imprime um espaço, sem pula linha
    i += 1
