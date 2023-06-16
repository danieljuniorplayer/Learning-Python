'''Exercício 5.14 Escreva um programa que leia números inteiros do teclado. O programa
deve ler os números até que o usuário digite O (zero). l o final da execução,
exiba a quantidade de números digitados, assim como a soma e a média aritmética.'''

# nesse caso, o while sempre vai estar True, portanto, loop infinito, até ser "brecado"
# se op == 0, o break interrompe o loop, o que vier após o break, não será executado
qtd = 0; soma = 0
while True:
    op = int(input('Digite um valor que será lido ou digite "0" para sair'))
    if op == 0:
        break
    qtd += 1
    soma += op
    print(op)

print(f'Quantidade de números: {qtd}')
print(f'Soma dos números: {soma}')
print(f'Média aritmética: {soma/(qtd)}')