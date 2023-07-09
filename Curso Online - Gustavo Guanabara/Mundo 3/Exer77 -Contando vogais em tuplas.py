palavra = ('Dessa', 'maneira', 'fica', 'claro', 'que', 'os', 'textos', 'podem', 'ser', 'curtos', 'com', 'somente', 'uma', 'palavra', 'ou', 'expresso', 'por', 'meio', 'de', 'um', 'conjunto', 'delas')
vogal = ('a', 'e', 'i', 'o', 'u')

for p in range(0, len(palavra)):            # Percorre as palavras dentro da tupla
    print(f'\nNa palavra "{palavra[p]:^8}" temos as vogais: ', end='')  # Printa a palavra que está sendo verificada
    for l in range(0, len(palavra[p])):     # Percorre as letras dentro da palavra
        for v in range(0, len(vogal)):      # Percorre as letras dentro da tupla "vogal"
            if vogal[v] in palavra[p][l]:   # Se tiver uma letra da "vogal" in/na letra da "palavra"
                print(vogal[v], end=' ')    # Imprime a vogal correspondente
