from time import sleep

print('Contagem regressiva para ano novo')
g = str(input('aperte enter para começar'))

for c in range(10,-1,-1):
    print(f'Contagem: {c}')
    sleep(1)
print('FELIZ ANO NOVO!!!')