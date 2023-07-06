nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
media = (nota1 + nota2)/2
print(f'Sua média foi {media:.1f}')
if media >= 7:
    print('Você foi APROVADO!')
elif media >= 5:
    print('Você vai para RECUPERAÇÃO!')
else:
    print('Você foi REPROVADO!')
