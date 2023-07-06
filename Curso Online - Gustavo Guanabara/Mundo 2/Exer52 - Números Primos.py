n = int(input('Digite um número inteiro: '))
divisiveis = []
for c in range(1,n+1):          # inicio 1, final n.
    if n/c == n//c:             # divisão com ponto flutuante e divisão sem ponto flutuante. tambem podia usar n%c ==0
        divisiveis.append(c)    # coloca na lista "divisiveis" todos divisiveis por "n"
print(f'{n} é divisível por: {divisiveis}')
if len(divisiveis) <= 2:          # se o segundo número divisivel for = "n" então...
    print(f'Potanto {n} \033[32mÉ primo! ✔\033[m')
else:
    print(f'Potanto {n} \033[31mNão é primo! ❌\033[m')