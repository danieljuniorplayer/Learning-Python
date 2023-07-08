#programa - sorteando alunos
a = [0, 1, 2, 3]
a[0] = str(input('Nome do primeiro aluno: '))
a[1] = input('Nome do segundo aluno: ')
a[2] = input('Nome do terceiro aluno: ')
a[3] = input('Nome do quarto aluno: ')
from random import randint
i = randint(0,3)
print(f'O aluno sorteado foi: {a[i]}')
