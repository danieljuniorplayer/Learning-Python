distancia = float(input('Qual foi a distância da viagem em kilometros?: '))

'''if distancia > 200:
    print(f'O valor da passagem cobrado vai ser R${distancia*0.45}')
else:
    print(f'O valor da passagem cobrado vai ser R${distancia * 0.50}')'''

'''print(f'O valor da passagem cobrado vai ser R$',end='')
print(f'{distancia*0.45:.2f}')if distancia>200 else print(f'{distancia*0.50:.2f}')'''

preco = distancia*0.45 if distancia>200 else distancia*50
print(f'O valor da passagem cobrado vai ser R${preco:.2f}')