lista = []
for c in range(0,10):
	a = int(input('Digite um valor: '))
	if c==0:
		lista.append(a)
	elif c==1:
		if lista[0] < a:
			lista.append(a)
		elif lista[0] >a:
			lista.insert(c-1,a)
	elif c>1:
		for d in range(0,len(lista)-1 ):
			if lista[d] < a < lista[d+1]:
				lista.insert(d+1,a)
			elif lista[d] > a:
				lista.insert(d,a)
			elif a > max(lista):
				lista.append(a)
			break
print(lista)


