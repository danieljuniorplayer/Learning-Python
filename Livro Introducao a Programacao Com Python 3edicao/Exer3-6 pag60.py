materia=[0,1,2]
i=0
while i<3:
	materia[i]=float(input(' Digite sua nota da {}ª matéria: '.format(i+1)))
	i+=1
i=0	
while i<3:
	print(' ',materia[i])
	i+=1
media=(materia[0]+materia[1]+materia[2])/3
print(' Sua media é: ',media)

if media>=7:
	print(' Parabéns voce passou de ano')
else:
	print(' Vish comédia, tu repetiu de ano kkk')