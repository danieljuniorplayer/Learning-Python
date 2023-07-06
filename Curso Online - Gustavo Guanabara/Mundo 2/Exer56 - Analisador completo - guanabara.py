# Definição de cores
V = '\033[32m'      # verde
F = '\033[m'
f = int(input('Digite a quantidade de pessoas:'))
soma =0
maiorIdadeMasculina=0
nomeVelho=''
mulherMenor20= 0
for p in range(0,f):
    print(f'|-----Dados da {p+1}ª pessoa ------|')
    nome = str(input(f'| Nome: ')).strip()
    idade = int(input(f'| Idade: '))
    sexo = str(input(f'| Sexo(M/F): ')).strip()
    soma+=idade
    if p == 0 and sexo in 'mM':
        maiorIdadeMasculina = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeMasculina:
        maiorIdadeMasculina = idade
        nomeVelho = nome
    if sexo in 'fF' and idade < 20:
        mulherMenor20 += 1

media = soma/f
print(f'Média de idade: {media:.2f}')
print(f'Nome do Homem mais velho: {nomeVelho} e tem {maiorIdadeMasculina} anos')
print(f'Ao todo {mulherMenor20} mulher(s) tem menos de 20 anos')