'''expressao=list()
inicio=[]
fim=[]
expressao.append(str(input('Digite uma expressão matemática: ')))
for v in range(0,len(expressao[0])):
    if '(' in expressao[0][v]:
        inicio.append(v)
    elif ')' in expressao[0][v]:
        fim.append(v)
if len(inicio) == len(fim):
    print('Os parêntese estão na ordem correta!')
else:
    print('Os parêntese Não estão fechados na ordem correta!')
print(inicio)
print(fim)'''
lista=list()
expressao=str(input('Digite uma expressão matemática: '))
for c in expressao:
    if c =='(':
        lista.append(c)
    elif c== ')':
        if len(lista) >0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista)== 0:
    print('Os parêntese estão na ordem correta!')
else:
    print('Os parêntese Não estão fechados na ordem correta!')
