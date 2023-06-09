#Exer 3.4
#Pag 58(60)
#livro introdução a programação com python
#data 03.06.23

a=[0,1,2,3] 		#listas
i=0					 #atribui 0 em i para iniciar o while
while i<4:			#enquanto i for menor que 4 faça
	letra=chr(65+i)#Transforma ASCII de um numero em letra
	a[i]=input('Didite o valor de {}: '.format(letra))#letra vai pra dentro de colchetes
	i+=1# soma i +1

i=0
while i<4:	
	print(a[i])#imprima o valor de a na posição i
	i=i+1 #soma i+1

print('Resultado: ',(a[0]>a[1])and(a[2]or a[3]))#Expressao logica > and or