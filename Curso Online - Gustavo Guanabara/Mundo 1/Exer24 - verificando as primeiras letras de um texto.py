cidade = str(input('Digite o nome de uma cidade:')).strip().upper()
resposta = 'SANTO' in cidade.split()[0]

print(f'\nAnalisando a cidade: {cidade}')
print(f'Sua cidade começa com a palavra "SANTO"?: {resposta}')
