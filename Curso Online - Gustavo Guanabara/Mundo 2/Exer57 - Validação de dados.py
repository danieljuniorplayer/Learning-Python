sexo = str(input('Digite seu sexo(M/F): ')).strip().upper()[0]
while sexo not in 'MF':
    sexo= str(input('Escolha [M] masculino ou [F] feminino: ')).strip().upper()[0]
print(sexo)