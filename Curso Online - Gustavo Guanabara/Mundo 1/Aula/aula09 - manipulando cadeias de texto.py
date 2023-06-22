print('''Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento
de String, Análise com len(), count(), find(), transformações com replace(), 
upper(), lower(), capitalize(), title(), strip(), junção com join()''')

frase = '   Curso em Vídeo Python   '
print(frase[0::2])                              # inicio 0, até fim, pulando 2 em 2
print(frase.count('o'))                         # conta quantas vezes aparece a frase o
print(frase.upper().count('O'))                 # transfor o "o" em maiúsculo e conta quantos tem
print(len(frase))                               # Mostra a quantidade de caracteres ou letras
print(len(frase.strip()))                       # remove os espaços indesejaveis e mostra a quantidade de caracteres
print(frase.replace('Python','Android'))        # Mostra a frase como ficaria trocando Python por Android
print('Curso' in frase)                         # tem palavra Curso na frase?
print(frase.find('Curso'))                      # Qual posição esta a palavra curso?
print(frase.lower().find('vídeo'))              # transforma a frase em minúscula e diz onde começa a palavra 'video'
print(frase.split())                            # cria uma lista com varias strings,
lista = frase.split()
print(lista[2])                                 # imprime o terceriro Item da lista
print(lista[2][::2])                            # no terceiro item, me mostra todos os valores pulando de 1 em 1