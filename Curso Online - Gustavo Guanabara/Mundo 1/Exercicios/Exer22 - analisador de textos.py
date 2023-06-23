
nome = str(input('Digite seu nome completo:')).strip()      # tira os espaços antes e depois

maiusculo = nome.upper()
minusculo = nome.lower()
letras_totais = len(nome) - nome.count(' ')
letras_item0 = nome.split()[0]
letras_item0 = len(letras_item0)

print(f'todas letras maiúsculas: {maiusculo}')
print(f'todas letras minúsculas: {minusculo}')
print(f'total de letras no nome : {letras_totais}')
print(f'Seu primeiro nome é "{nome.split()[0]}" e ele tem : {letras_item0} letras')

from playsound import playsound
playsound('BE TOGETHER.mp3')