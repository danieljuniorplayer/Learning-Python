#pag45 Exercício 2.1 Converta as seguintes expressões matemáticas para que possam ser calculadas usando o interpretador Python.
n1=int(10+20*30)
print(n1)
n2=float(4**2/30)
print(n2)
n4=int(9**4+2)*6-1
print(n4)
#pag 45 Exercício 2.2 Digite a seguinte expressão no interpretador:
n5=(10%3*10**2+1-10*4/2)
print(n5)

#pag 49 Exercício 2.4 Escreva um programa que exiba o resultado de 2a x Jb, em que a vale 3 e b vale 5.
a=3; b=5
n6=int((2*a)*(3*b))
print(n6)

#pag 49 Exercício 2.5 Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela
c=7;d=8;e=9
print(c+d+9)
sal=750
au=15
print(au*sal/100+sal)
print(3*0.1)
# Teste com if------------------------------------------------------
nota=5
media=5
if nota>=media:    #modo simples com print
    print('Aprovado')
else:
    print('Reprovado')
aprovado=nota>=media
print(aprovado)   #modo alter com True
print(nota>=media)#modo simples com True

#Exercício 3.2  pag 56 Complete a tabela a seguir, respondendo True ou False. Considere
a=4;b=10;c=5.0;d=1;f=5
print(a==c)
print(a<b)
print(d>b)
print(c!=f)
print(a==b)
print(c<d)
print('---------^----------')
#3.3 pag59 Complete a tabela a seguir utilizando a = True, b = False e e = True

a=True;b=False;c=True

print(a and a)
print(b and b)
print(not c)
print(not b)
print(not a)
print(a and b)
print(b and c)
print(a or b)
print(b or c)
print(a or c)
print(c or b)
print(c or c)
print(b or b)

print('gabarito\nT,F,F,T,F,F,F,T,T,T,T,T,F')
