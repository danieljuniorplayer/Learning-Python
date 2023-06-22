nome = str(input('Digite seu nome completo:'))

maiusculo = nome.upper()

minusculo = nome.lower()

letras_totais = nome.split()[0] + nome.split()[1] + nome.split()[2] + nome.split()[3]
letras_totais = len(letras_totais)

letras_item0 = nome.split()[0]
letras_item0 = len(letras_item0)

print(f'todas letras maiúsculas: {maiusculo}')
print(f'todas letras minúsculas: {minusculo}')
print(f'total de letras no nome : {letras_totais}')
print(f'Seu primeiro nome é "{nome.split()[0]}" e ele tem : {letras_item0} letras')
