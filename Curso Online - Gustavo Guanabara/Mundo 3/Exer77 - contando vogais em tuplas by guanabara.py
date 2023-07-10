palavra = ('Dessa', 'maneira', 'fica', 'claro', 'que', 'os', 'textos', 'podem', 'ser', 'curtos', 'com', 'somente', 'uma', 'palavra', 'ou', 'expresso', 'por', 'meio', 'de', 'um', 'conjunto', 'delas')

for p in palavra:
    print(f'\nA palavra: "{p}" tem as vogais: ',end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end='')