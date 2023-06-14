
a = int(input('Qual o valor de a?'))
b = int(input('Por qual valor voce que dividir?'))
i = a/b

# / divide e mostra o resultado flutuante com casas decimais
# // divide e mostra o resultado inteiro sem casas decimais

if i // 1 == i:         # se i no formato inteiro == i no formato flutuante...
    print("inteiro")    # então imprime "inteiro"
else:                   # se não ...
    print('flutuante')  # imprime "flutuante"