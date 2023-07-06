# Definição de cores
V = '\033[32m'      # verde
F = '\033[m'

# Inicio dos inputs -----------------------------------------------------------------------------------------
f = int(input('Digite a quantidade de pessoas:'))
soma =0
listaNome=[]
listaIdade = []
listaSexo=[]
for p in range(0,f):
    nome = str(input(f'\nDigite o {V}nome{F} da {p+1}ª pessoa:')).strip().upper()
    listaNome += [nome]
    idade = int(input(f'Digite a {V}idade{F} da {p+1}ª pessoa:'))
    listaIdade += [idade]
    sexo = str(input(f'Digite o {V}sexo{F} da {p+1}ª pessoa:(M/F)')).strip().upper()
    listaSexo += [sexo]
    soma += idade

# Média de idade das pessoas ------------------------------------------------------------------------------
media = soma/f
print(f'\nA média de idade é {media}')

# Descobrir o nome do homem mais velho ---------------------------------------------------------------------
#   Descobre qual maior idade
idadeMasculina=[]
for p in range(0,f):                                # de 0 até f
    if listaSexo[p] == 'M':                         # se for Macho
        idadeMasculina+=[listaIdade[p]]             # Salva a idade na lista "idadeMasculina", incrementando
#   Descobre a posicacao em que esta a maior idade
for p in range(0,f):
    if listaSexo[p] == 'M':
        if listaIdade[p] == max(idadeMasculina):    # se for o valor máximo que está na lista "idadeMasculina"
            print(f'O Homem mais velho é {listaNome[p]}, com {listaIdade[p]} anos')

# Descobrir quantas mulheres tem menos de 20 anos -------------------------------------------------------------
m = 0
for p in range(0,f):
    if listaSexo[p] == 'F':
        if listaIdade[p] < 20:              # se idade for menor de 20 anos
            m+=1                            # acrecenta + 1 no contador
print(f'{m} mulher(s) tem menos de 20 anos')


# divide o nome da pessoa letra por letra
'''letra=[]
letra+=listaNome[0]
print(letra)'''



