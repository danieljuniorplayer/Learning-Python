'''Exercício 5.10 Modifique o programa anterior para que aceite respostas com letras
maiúsculas e minúsculas em todas as questões.'''
questao=1       #contador
ponto=0
while questao <= 3:
    r = input(f'Qual a resposta da questão{questao}')
    if questao == 1 and (r == 'b' or r == 'B'):
        ponto+=1
    if questao == 2 and (r == 'a' or r == 'A'):
        ponto+=1
    if questao == 3 and (r == 'd' or r == 'D'):
        ponto+=1
    questao+=1
print(ponto)