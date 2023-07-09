colocados = ('Botafogo','Grêmio','Flamengo','Palmeiras','Bragantino','Fluminense','São Paulo','Internacional','Athletico-PR','Atlético-MG','Fortaleza','Cruzeiro','Cuiabá','Santos','Bahia','Corinthians','Goiás','Vasco','América-MG','Coritiba')

print('='*60)
print(f'Os 5 primeiros colocados: \n{colocados[:5]}')
print('='*60)
print(f'Os últimos 4 colocados: \n{colocados[-4:]}')
print('='*60)
print(f'Times em ordem alfabética:\n{sorted(colocados)}')
print('='*60)
print(f'O Cruzeiro está na posição: {colocados.index("Cruzeiro")+1}')  # index diz a posição que está a palavra Cruzeiro




