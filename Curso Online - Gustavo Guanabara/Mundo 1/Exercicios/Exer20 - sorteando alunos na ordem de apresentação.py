#programa - sorteando ordem de apresentação dos alunos
import random

aluno = [0, 1, 2, 3]
aluno[0] = input('Nome do primeiro aluno: ')
aluno[1] = input('Nome do segundo aluno: ')
aluno[2] = input('Nome do terceiro aluno: ')
aluno[3] = input('Nome do quarto aluno: ')

from random import randint, sample
sorteado = sample(range(0,4),4)
print(sorteado)

i=0
while i < 4:
    print(f'{i+1}° aluno: {aluno[sorteado[i]]}')
    i+=1



