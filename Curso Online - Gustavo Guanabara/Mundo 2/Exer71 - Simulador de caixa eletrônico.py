print('='*40,'\n            CAIXA ELETRÔNICO')
print('='*40)
cin=vin=dez=um=0
valor = int(input('Qual valor será sacado? R$'))
temp = valor
while True:
    if temp >= 50:
        temp-=50
        cin+=1
    elif temp >=20:
        temp-=20
        vin+=1
    elif temp>=10:
        temp-=10
        dez+=1
    elif temp>=1:
        temp-=1
        um+=1
    else:
        break
print(f'Será impresso:\n'
      f'{cin} notas de R$50\n'
      f'{vin} notas de R$20\n'
      f'{dez} notas de R$10\n'
      f'{um} nota(s) de R$1')
