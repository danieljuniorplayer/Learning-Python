#Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos
#por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
#o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
#dia e R$ 0,15 por km rodado.

km_percorrido = float(input('Quantos quilômetro o carro percorreu? '))
qtd_dias = int(input('Quantos dias o carro foi alugado? '))

preco_a_pagar = qtd_dias*60 + km_percorrido*0.15

print(f'O preco a pagar he R${preco_a_pagar:.2f}')

