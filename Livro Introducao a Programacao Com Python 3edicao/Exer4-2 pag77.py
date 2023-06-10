#Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um
#usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi
#multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade = int(input('Qual foi a velocidade do carro em km/h?'))
if (velocidade > 80):               #Se velocidade for maior que 80, então receberá multa
    multa = (velocidade - 80) * 5     #calcula valor da multa -> 5 reais a cada 1 km/h acima de 80km/h
    print(f'Você foi multado em R${multa:.2f}')
else:
    print('Parabéns, você não foi multado. ',end='') # end='' faz com que a proxima linha não seja pulada
    print("Tenha uma ótima viagem!")