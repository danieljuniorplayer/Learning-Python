op=1
while op!=0:
	op=int(input('1-Continuar\n0-Sair'))
	idade=int(input('Digite sua idade'))

	if idade == 23:
			print('Você Acertou sua idade')
	elif idade==0:
		print('Essa idade não existe')
	else:
		print('Voce errou sua idade')
		
