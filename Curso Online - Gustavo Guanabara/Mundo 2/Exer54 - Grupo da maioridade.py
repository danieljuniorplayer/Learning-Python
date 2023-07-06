from datetime import date
atual = date.today().year

maior=0
menor=0
for c in range(0,7):
    ano = int(input(f'Digite o ano de nascimaneto da {c+1}ª pessoa:'))
    idade = atual - ano
    if idade >=21:
        maior+=1
    else:
        menor+=1
print(f'Total de pessoas com Maioridade: {maior}')
print(f'Total de pessoas com Menoridade: {menor}')

