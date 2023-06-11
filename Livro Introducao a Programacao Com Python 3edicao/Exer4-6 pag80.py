""""Exercício 4.6 Escreva um programa que pergunte a distância que um passageiro
deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
para viagens de até de 200 km, e R$ 0,45 para viagens mais longas."""
distancia = float(input('Qual distância você pretende percorrer em km'))
if distancia > 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.50
print(f'Se você percorer uma distância de {distancia} km, então você pagará {preco}')