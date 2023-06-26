n1 = float(input('Digite um número: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)     # rais quadrada
r = pow(n1,1/2)     # rais quadrada

print(f'O dobro de {n1} é \033[36m{d}\033[m\n'
      f'O triplo é \033[36m{t}\033[m\n'
      f'A raiz quadrada é \033[36m{r:.2f}\033[m\n')