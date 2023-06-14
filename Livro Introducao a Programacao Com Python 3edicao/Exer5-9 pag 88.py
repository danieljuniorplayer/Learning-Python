'''Exercício 5.9 Escreva um programa que leia dois números. Imprima a divisão
inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
os operadores de soma e subtração para calcular o resultado. Lembre-se de que
podemos entender o quociente da divisão de dois números como a quantidade de
vezes que podemos retirar o divisor do dividendo. Logo, 20 / 4 = 5, uma vez que
podemos subtrair 4 cinco vezes de 20.'''

# lê dois números
n1 = int(input('\nQual o primeiro número'))
n2 = int(input('Qual o segundo número'))
#imprime a divisao inteira
print(f'Divisão inteira: {n1}/{n2} = {n1//n2}')
#imprime o resto da divisão
print(f'Resto da divisão: {n1%n2}')

#--------------utilizando apenas soma e subtração----------------
n1 = int(n1)
n1 = int(input('\nQual o primeiro número'))
n2 = int(input('Qual o segundo número'))
#imprime a divisao inteira e o resto usando apenas (-) ou (+)
q=0                     # Define o valor inicial de q (quociente)
s=0                     # Define o valor inicial de s (subtraente)
while s <= n1:          # Enquanto n1 for menor que subtraente(s)...faça
    quociente = q       # Salva "q" em quociente, pois o "q" sofrerá alteração no incremento (q += 1)
    resto = n1 - s      # Salva "n1 - s" em resto, pois o "s" sofre alteração no incremento (s += n2)
    q += 1              # Incrementa "q = q + 1"
    s += n2             # Incrementa "s = s + n2"

print(f'Quociente/Divisão inteira: {quociente}')
print(f'Resto da divisão: {resto}')
