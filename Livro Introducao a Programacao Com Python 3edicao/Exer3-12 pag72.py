#Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = float(input('Qual a distância percorrida pelo carro em Km?'))
velocidade = float(input('Qual a velocidade média do carro em km/h'))
hora = distancia/velocidade
if hora < 1:
    minuto = hora*60
    print(f'Se voce percorrer {distancia}Km, numa velocidade de {velocidade}Km/h, voce vai levar {minuto:.0f} minutos')
else:
    print(f'Se voce percorrer {distancia}Km, numa velocidade de {velocidade}Km/h, voce vai levar {hora} horas\n')