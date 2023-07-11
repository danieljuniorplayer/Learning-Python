lista = []
for c in range(0,5):
	a = int(input('Digite um valor: '))
	while a in lista:
		print(f'{a} já tem na lista, tente novamente...')
		a=int(input(f'Digite um valor: '))
	if c==0 :
		lista.append(a)
	elif c==1:
		if lista[0] < a:
			lista.append(a)
		elif lista[0] >a:
			lista.insert(c-1,a)
	elif c>1:
		for p, d in enumerate(lista):
			if a < d:
				lista.insert(p,a)
			elif a > max(lista):
				lista.append(a)
			elif d< a < lista[p+1]:
				lista.insert(p+1,a)
			break
	print(f'{a} vai para posição: {lista.index(a)}')
print(lista)