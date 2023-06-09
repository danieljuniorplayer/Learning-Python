#Variaveis String pag 59 livro 61
#posicionamento um caracter na string
a='daniel'
print(' ',a)
print(' ',a[2])

#Concatenação pag61
print("x"+"-"*41+"x"+a)

#Composição pag 61-65
idade=23
print('daniel tem %0.3d anos'%idade)#Marcadores
print('daniel tem {:03} anos'.format(idade))
print(f'daniel tem {idade:03} anos')

#Fatiamento de strings pag 65
print(a[0:2])
print(a[2:4])
print(a[4:6])